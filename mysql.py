"""Module for MySQL database operations using PyMySQL."""

import sys
import pymysql
from pymysql import Connection

sys.path.append(".")
from config import (
    MYSQL_DBNAME,
    MYSQL_HOSTNAME,
    MYSQL_PASSWORD,
    MYSQL_PORT,
    MYSQL_USERNAME,
)


class MySQLModel:
    """Represents a database model with a connection."""

    conn: Connection

    def __init__(self):
        self.conn = pymysql.connect(
            host=MYSQL_HOSTNAME,
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD,
            db=MYSQL_DBNAME,
            port=int(MYSQL_PORT),
        )

        if self.conn is None:
            print("Error connecting to the MySQL database")
        else:
            print("MySQL connection established!")

    def fetch(self, query: str, args: object | None = None):
        """Execute the given query and fetch all results."""
        m_cursor = self.conn.cursor()
        m_cursor.execute(query, args)
        results = m_cursor.fetchall()
        self.conn.close()
        return results
