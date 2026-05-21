import sqlite3
from config.settings import settings
import os

class SqliteDB:
    def __init__(self):
        os.makedirs(os.path.dirname(settings.DB_PATH), exist_ok=True)
        self.conn = sqlite3.connect(settings.DB_PATH, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._init_table()

    def _init_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS document(
            file_id TEXT PRIMARY KEY,
            title TEXT,
            file_type TEXT,
            file_path TEXT,
            tags TEXT
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS chunk_relation(
            child_id TEXT PRIMARY KEY,
            parent_id TEXT,
            file_id TEXT,
            child_content TEXT
        )
        ''')
        self.conn.commit()

    def insert(self, sql: str, data: tuple):
        self.cursor.execute(sql, data)
        self.conn.commit()

    def query(self, sql: str):
        return self.cursor.execute(sql).fetchall()