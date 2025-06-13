import sqlite3, pandas as pd, streamlit as st

DB_PATH = "data/clean/data.db"
SQL_DIR = "sql"

def load(sql_file: str) -> pd.DataFrame:
    with sqlite3.connect(DB_PATH) as conn, open(f"{SQL_DIR}/{sql_file}") as f:
        return pd.read_sql_query(f.read(), conn)

def main():
    st.title("NYC Collisions Dashboard")

    df = load("01_filter.sql")  # filters injurious crashes
    df["crash_datetime"] = pd.to_datetime(df["crash_datetime"])
    df["borough"] = df["borough"].fillna("UNKNOWN")

    # Controls:
    st.sidebar.header("Filter Options")
    min_date = df["crash_datetime"].dt.date.min()
    max_date = df["crash_datetime"].dt.date.max()
    start_date, end_date = st.sidebar.date_input(
        "Date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )
    
    boroughs = sorted(df["borough"].unique())
    selected = st.sidebar.multiselect("Boroughs", boroughs, default=boroughs)



    mask = (
        (df["crash_datetime"].dt.date >= start_date) &
        (df["crash_datetime"].dt.date <= end_date) &
        (df["borough"].isin(selected))
    )
    df_filt = df.loc[mask]
    
    st.write(f"**Incidents (injuries/fatalities):** {len(df_filt):,}")

    # Charts:
    # Injuries by borough
    df_agg = load("02_aggregate.sql")
    df_agg["borough"] = df_agg["borough"].fillna("UNKNOWN")
    st.subheader("Total Injuries by Borough")
    st.bar_chart(
        df_agg[df_agg["borough"].isin(selected)]
        .set_index("borough")["total_injuries"]
    )

    # Crashes by hour
    df_hour = load("03_time_analysis.sql")
    st.subheader("Crashes by Hour (AM/PM)")
    st.line_chart(
        df_hour.set_index("hour_label")["crash_count"]
    )

    # ———————— Map ————————
    st.subheader("Crash Locations Map")
    # Drop rows missing coords
    coords = df_filt[["latitude", "longitude"]].dropna()
    st.map(coords)

    # ———————— Sample Data ————————
    st.subheader("Sample of Filtered Records")
    st.dataframe(df_filt.head(10))

if __name__ == "__main__":
    main()