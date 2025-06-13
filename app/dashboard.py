
import sqlite3, pandas as pd, streamlit as st

DB_PATH = "data/clean/data.db"
SQL_DIR = "sql"

def load(sql_file):
    with sqlite3.connect(DB_PATH) as conn, open(f"{SQL_DIR}/{sql_file}") as f:
        return pd.read_sql_query(f.read(), conn)

st.title("NYC Collisions Dashboard")

# 02 borough injuries
df2 = load("02_aggregate.sql")
st.subheader("Total Injuries by Borough")
st.bar_chart(df2.set_index("borough")["total_injuries"])

# 03 hourly crashes
df3 = load("03_time_analysis.sql")
st.subheader("Crashes by Hour (AM/PM)")
st.line_chart(df3.set_index("hour_label")["crash_count"])


df1 = load("01_filter.sql")
df1["borough"] = df1["borough"].fillna("UNKNOWN")
st.write(f"TOTAL # of Incidents w/ injuries/fatalities: {len(df1):,}")
st.write(f"What the data looks like: ")
st.dataframe(df1.head())