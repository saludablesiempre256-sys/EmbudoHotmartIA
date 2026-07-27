import sqlite3
import os
from datetime import datetime

def obtener_conexion():
    ruta_bd = os.path.join("database", "prospectos.db")
    
    # Crear carpeta si no existe
    directorio = os.path.dirname(ruta_bd)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio, exist_ok=True)
        
    return sqlite3.connect(ruta_bd)
    ruta_bd = os.path.join("data", "embudo.db")
    return sqlite3.connect(ruta_bd)

def inicializar_bd():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prospectos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            telefono TEXT,
            estado TEXT DEFAULT 'Interesado',
            fecha TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def guardar_prospecto(nombre, telefono):
    inicializar_bd()
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    cursor.execute('''
        INSERT INTO prospectos (nombre, telefono, fecha)
        VALUES (?, ?, ?)
    ''', (nombre, telefono, fecha_actual))
    
    conexion.commit()
    conexion.close()
    print(f"👤 Prospecto guardado: {nombre} ({telefono})")

def listar_prospectos():
    inicializar_bd()
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute('SELECT id, nombre, telefono, estado, fecha FROM prospectos')
    prospectos = cursor.fetchall()
    conexion.close()
    
    print("\n--- LISTA DE PROSPECTOS ---")
    for p in prospectos:
        print(f"ID: {p[0]} | Nombre: {p[1]} | Tel: {p[2]} | Estado: {p[3]} | Fecha: {p[4]}")

# PRUEBA DEL SISTEMA
guardar_prospecto("Cliente Ejemplo", "+593999999999")
listar_prospectos()
