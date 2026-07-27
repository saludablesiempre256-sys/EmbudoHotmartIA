import config
import logger

def responder_mensaje(mensaje_cliente):
    mensaje_lc = mensaje_cliente.lower()
    
    # Tomamos el enlace real desde config.py
    link_venta = config.LINK_HOTMART
    
    if "precio" in mensaje_lc or "cuanto" in mensaje_lc or "pago" in mensaje_lc:
        respuesta = f"Nuestros contenidos y recursos de Mente Creadora tienen un precio muy accesible. Revisa los detalles y ofertas directas aquí: 👇\n{link_venta}"
    elif "comprar" in mensaje_lc or "enlace" in mensaje_lc or "link" in mensaje_lc:
        respuesta = f"¡Es súper fácil! Puedes acceder inmediatamente a través de nuestro enlace oficial de Hotmart: 👇\n{link_venta}"
    elif "garantia" in mensaje_lc or "seguro" in mensaje_lc:
        respuesta = f"Sí, todos nuestros productos cuentan con garantía de satisfacción respaldada por Hotmart. Compra segura aquí: 👇\n{link_venta}"
    elif "contenido" in mensaje_lc or "curso" in mensaje_lc or "ebook" in mensaje_lc:
        respuesta = f"Ofrecemos guías y recursos digitales para potenciar tus proyectos. Descubre más detalles aquí: 👇\n{link_venta}"
    else:
        respuesta = f"¡Hola! Gracias por escribir a Mente Creadora. Conoce nuestros productos digitales en Hotmart: 👇\n{link_venta}"
    
    # Registramos la interacción
    logger.registrar_evento(f"Consulta: '{mensaje_cliente}' | Respuesta enviada.")
    return respuesta

# PRUEBA DEL CHATBOT
print("--- PRUEBA DEL CHATBOT CON LINK REAL ---")
pregunta = "Dame el link para comprar"
print(f"Cliente pregunta: {pregunta}\n")
print(f"Bot responde:\n{responder_mensaje(pregunta)}")