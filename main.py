import config
import logger
import database
import bot_respuestas

def ejecutar_sistema():
    print(f"=== SISTEMA {config.NOMBRE_PROYECTO} v{config.VERSION} ===")
    logger.registrar_evento("Iniciando flujo principal del embudo.")
    
    # Aseguramos que la base de datos esté inicializada
    database.inicializar_bd()
    
    # Simulación de un nuevo prospecto interactuando
    nombre_prospecto = "David"
    telefono_prospecto = "+593000000000"
    mensaje_prospecto = "Hola, me interesa el curso, ¿cuánto cuesta?"
    
    print(f"\n📩 Mensaje recibido de {nombre_prospecto}: '{mensaje_prospecto}'")
    
    # 1. Guardamos al prospecto en la base de datos
    database.guardar_prospecto(nombre_prospecto, telefono_prospecto)
    
    # 2. Generamos la respuesta con el enlace de Hotmart
    respuesta = bot_respuestas.responder_mensaje(mensaje_prospecto)
    
    print("\n🤖 Respuesta del Bot:")
    print(respuesta)
    print("\n===========================================")

if __name__ == "__main__":
    ejecutar_sistema()
    import time

# Mantener el proceso vivo en el servidor
if __name__ == "__main__":
    print("🚀 Servidor Mente Creadora activo y escuchando 24/7...")
    while True:
        time.sleep(3600)  # Espera activa para mantener el bot encendido
