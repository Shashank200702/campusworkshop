"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaad12k728r8869s47g-a.oregon-postgres.render.com",
        database="todo_401w",
        user="root",
        password="9mhNyMCBKEvyK1jUch30E3IpddxDLE57")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
