"""Configuration parser module."""

import configparser

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
MYSQL_HOSTNAME = parser.get("mysql_config", "hostname")
MYSQL_PORT = parser.get("mysql_config", "port")
MYSQL_USERNAME = parser.get("mysql_config", "username")
MYSQL_DBNAME = parser.get("mysql_config", "database")
MYSQL_PASSWORD = parser.get("mysql_config", "password")

# PostgreSQL configuration
POSTGRES_HOSTNAME = parser.get("postgres_config", "hostname")
POSTGRES_PORT = parser.get("postgres_config", "port")
POSTGRES_USERNAME = parser.get("postgres_config", "username")
POSTGRES_DBNAME = parser.get("postgres_config", "database")
POSTGRES_PASSWORD = parser.get("postgres_config", "password")


MONGO_HOSTNAME = parser.get("mongo_config", "hostname")
MONGO_USERNAME = parser.get("mongo_config", "username")
MONGO_PASSWORD = parser.get("mongo_config", "password")
MONGO_DBNAME = parser.get("mongo_config", "database")
MONGO_COLLECTION = parser.get("mongo_config", "collection")
