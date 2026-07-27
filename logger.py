import os
if not os.path.exists("logs"):
    os.makedirs("logs")
from datetime import datetime

def registrar_evento(mensaje):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{fecha_hora}] {mensaje}\n"
    
    # Guarda el registro en la carpeta logs
    ruta_log = os.path.join("logs", "historial.txt")
    with open(ruta_log, "a", encoding="utf-8") as archivo:
        archivo.write(linea)
    
    print(f"📌 Registrado: {mensaje}")

# Prueba del registrador
registrar_evento("El sistema Mente Creadora se inicio correctamente.")
