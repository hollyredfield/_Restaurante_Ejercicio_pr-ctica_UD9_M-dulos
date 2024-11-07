import sqlite3
import os
from typing import List
from src.models.menu_item import MenuItem
from src.models.order import Order

class DBManager:
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'restaurant.db')
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS menu (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                price REAL,
                category TEXT
            );
            
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                date TEXT,
                items TEXT,
                total REAL
            );
        ''')
        self.conn.commit()

    def add_menu_item(self, item: MenuItem):
        self.cursor.execute('''
            INSERT INTO menu (name, price, category) VALUES (?, ?, ?)
        ''', (item.name, item.price, item.category))
        self.conn.commit()

    def get_menu_item(self, name: str) -> MenuItem:
        self.cursor.execute('''
            SELECT name, price, category FROM menu WHERE name = ?
        ''', (name,))
        row = self.cursor.fetchone()
        if row:
            return MenuItem(*row)
        return None

    def add_order(self, order: Order):
        order_dict = order.to_dict()
        print(f"Adding order to database: {order_dict}")
        self.cursor.execute('''
            INSERT INTO orders (date, items, total) VALUES (?, ?, ?)
        ''', (order_dict["date"], ','.join(order_dict["items"]), order_dict["total"]))
        self.conn.commit()