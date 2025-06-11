import sqlite3
import pandas as pd
from pathlib import Path

clean_csv_path = Path("scripts") / ".." / "data" / "clean" / "cleaned_nyc_collisions.csv"
db_path  = Path("scripts") / ".." / "data" / "clean" / "data.db"

clean_csv_path = clean_csv_path.resolve()
db_path = db_path.resolve()

df = pd.read_csv(clean_csv_path)

connection = sqlite3.connect(db_path)
df.to_sql(
    name="collisions_clean",
    con = connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Imported to collisions_clean")