# database.py
import sqlite3
from datetime import datetime

DB_NAME = "lenguajes.db"

def inicializar_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lenguajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                fecha TEXT NOT NULL
            )
        """)
        conn.commit()

def guardar_lenguajes(lenguajes):
    fecha_actual = datetime.now().isoformat()
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        for nombre, cantidad in lenguajes:
            cursor.execute("""
                INSERT INTO lenguajes (nombre, cantidad, fecha)
                VALUES (?, ?, ?)
            """, (nombre, cantidad, fecha_actual))
        conn.commit()

def obtener_historico():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT nombre, cantidad, fecha
            FROM lenguajes
            ORDER BY fecha DESC
        """)
        return cursor.fetchall()
