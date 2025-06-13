# SAMPLE GENERATED TESTS:

import sqlite3
import pytest

DB_PATH = "data/clean/data.db"

@pytest.fixture(scope="module")
def conn():
    conn = sqlite3.connect(DB_PATH)
    yield conn
    conn.close()

def test_table_exists(conn):
    """Ensure the collisions_clean table is present."""
    cur = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='collisions_clean';"
    )
    assert cur.fetchone() is not None, "Table 'collisions_clean' should exist."

def test_row_count_positive(conn):
    """Ensure there's at least one row in collisions_clean."""
    count = conn.execute("SELECT COUNT(*) FROM collisions_clean;").fetchone()[0]
    assert count > 0, "Table should contain at least one row."

def test_no_null_crash_datetime(conn):
    """Ensure crash_datetime has no NULL values."""
    nulls = conn.execute(
        "SELECT COUNT(*) FROM collisions_clean WHERE crash_datetime IS NULL;"
    ).fetchone()[0]
    assert nulls == 0, "crash_datetime should have no NULL values."
