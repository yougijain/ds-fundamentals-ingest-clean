import sqlite3, pandas as pd, streamlit as st
import pydeck as pdk # heatmap support, to replace dot map

DB_PATH = "data/clean/data.db"
SQL_DIR = "sql"

@st.cache_data(ttl=600)
def load(sql_file: str) -> pd.DataFrame:
    with sqlite3.connect(DB_PATH) as conn, open(f"{SQL_DIR}/{sql_file}") as f:
        return pd.read_sql_query(f.read(), conn)

def main():
    st.title("NYC Collisions Dashboard")

    df = load("01_filter.sql")
    df["crash_datetime"] = pd.to_datetime(df["crash_datetime"])
    df["borough"] = df["borough"].fillna("UNKNOWN")

    st.sidebar.header("Filter Options")
    min_date = df["crash_datetime"].dt.date.min()
    max_date = df["crash_datetime"].dt.date.max()
    start_date, end_date = st.sidebar.date_input(
        "Date range", (min_date, max_date), min_value=min_date, max_value=max_date
    )
    boroughs = sorted(df["borough"].unique())
    selected = st.sidebar.multiselect("Boroughs", boroughs, default=boroughs)

    mask = (
        (df["crash_datetime"].dt.date >= start_date) &
        (df["crash_datetime"].dt.date <= end_date) &
        (df["borough"].isin(selected))
    )
    df_filt = df.loc[mask].dropna(subset=["latitude", "longitude"])

    st.write(f"**Incidents (injuries/fatalities):** {len(df_filt):,}")

    df2 = load("02_aggregate.sql").assign(borough=lambda d: d["borough"].fillna("UNKNOWN"))
    st.subheader("Total Injuries by Borough")
    st.bar_chart(df2[df2["borough"].isin(selected)].set_index("borough")["total_injuries"])

    df3 = load("03_time_analysis.sql")
    st.subheader("Crashes by Hour (AM/PM)")
    st.line_chart(df3.set_index("hour_label")["crash_count"])

    st.subheader("Crash Heatmap")
    midpoint = (40.7128, -74.0060)
    layer = pdk.Layer(
        "HeatmapLayer",
        df_filt,
        get_position=["longitude", "latitude"],
        radius_pixels=50,
    )
    view_state = pdk.ViewState(
        latitude=midpoint[0], longitude=midpoint[1], zoom=10, pitch=0
    )
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

    st.subheader("Sample of Filtered Records")
    st.dataframe(df_filt.head(10))

if __name__ == "__main__":
    main()