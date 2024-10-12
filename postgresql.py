"""Module for PostgreSQL database operations using psycopg2."""

from typing import Any
import psycopg2
import sys

sys.path.append(".")
from config import (
    POSTGRES_DBNAME,
    POSTGRES_HOSTNAME,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USERNAME,
)


class PostgreSQLModel:
    """Represents a database model with a connection."""

    conn: Any

    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname="
            + POSTGRES_DBNAME
            + " user="
            + POSTGRES_USERNAME
            + " password="
            + POSTGRES_PASSWORD
            + " host="
            + POSTGRES_HOSTNAME,
            port=POSTGRES_PORT,
        )

        if self.conn is None:
            print("Error connecting to the PostgreSQL database")
        else:
            print("PostgreSQL connection established!")

    def fetch(self, query: str, args: object | None = None):
        """Execute the given query and fetch all results."""
        m_cursor = self.conn.cursor()
        m_cursor.execute(query, args)
        results = m_cursor.fetchall()
        self.conn.close()
        return results
