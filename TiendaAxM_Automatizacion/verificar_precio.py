import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

def enviar_correo(precio_actual, precio_anterior):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    correo_emisor = 'tupuedes029@gmail.com'
    contraseña_app = 'ockhektdzgghypvr'  # Contraseña de aplicación generada

    if precio_actual < precio_anterior:
        mensaje = 'El precio del producto ha bajado de ${} a ${}. ¡Es hora de comprarlo!'.format(precio_anterior, precio_actual)
        asunto = '¡Alerta de precio de la Pagina TiendaAxM!'
    elif precio_actual > precio_anterior:
        mensaje = 'El precio del producto ha subido de ${} a ${}. ¡Espera a una posible oferta!'.format(precio_anterior, precio_actual)
        asunto = 'Alerta de aumento de precio'
    else:
        mensaje = 'El precio del producto sigue siendo ${}. No hay cambios.'.format(precio_actual)
        asunto = 'Actualización de precio'
    
    msg = MIMEText(mensaje)
    msg['Subject'] = asunto
    msg['From'] = correo_emisor
    msg['To'] = 'andresfeliperamirezespinal@gmail.com'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(correo_emisor, contraseña_app)
        server.sendmail(correo_emisor, [msg['To']], msg.as_string())
        print('¡Correo electrónico enviado correctamente!')
    except Exception as e:
        print('Error al enviar el correo electrónico:', e)
    finally:
        server.quit()

def obtener_precio_actual():
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5000')

    wait = WebDriverWait(driver, 10)
    elemento_precio = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.card-text:nth-child(2)')))
    time.sleep(5)

    precio_actual = float(elemento_precio.text.replace('Precio: $', '').replace(',', ''))
    
    driver.quit()

    return precio_actual

def cargar_precio_anterior():
    try:
        with open('precio_anterior.json', 'r') as file:
            data = json.load(file)
            return data.get('precio_anterior', 0)
    except FileNotFoundError:
        return 0

def guardar_precio_actual(precio_actual):
    with open('precio_anterior.json', 'w') as file:
        json.dump({'precio_anterior': precio_actual}, file)

def main():
    precio_actual = obtener_precio_actual()
    precio_anterior = cargar_precio_anterior()

    if precio_actual != precio_anterior:
        enviar_correo(precio_actual, precio_anterior)
        guardar_precio_actual(precio_actual)
    else:
        print('El precio del producto no ha cambiado. No se enviará ninguna alerta.')

if __name__ == "__main__":
    main()
