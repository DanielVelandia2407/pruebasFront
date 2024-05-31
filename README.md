# pruebasFront
Playwright Automation Script
Este script automatiza la navegación por varias páginas del sitio web Fourpark utilizando Playwright, tomando capturas de pantalla en diferentes estados y páginas del sitio.

Requisitos
Antes de ejecutar el script, asegúrate de tener instalados los siguientes componentes:

Python 3.7 o superior
Playwright
Instalación
Instala Playwright:

bash
Copiar código
pip install playwright
Instala los navegadores necesarios para Playwright:

bash
Copiar código
playwright install
Uso
Guarda el script en un archivo, por ejemplo fourpark_automation.py, y ejecútalo con Python:

bash
Copiar código
python fourpark_automation.py
Descripción del Script
El script realiza las siguientes acciones:

Inicio del navegador: Inicia un navegador Chromium en modo no headless (visible).
Navegación y capturas de pantalla:
Accede a la página de inicio de sesión y toma una captura de pantalla.
Completa el formulario de inicio de sesión con credenciales.
Marca la casilla de verificación si está presente y hace clic en "Iniciar sesión".
Espera a que la página cargue completamente.
Navega a varias páginas del sitio y toma capturas de pantalla en cada una de ellas.
Las capturas de pantalla se guardan en la carpeta especificada en cada línea de page.screenshot().

Estructura del Código
python
Copiar código
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Navegación a la página de login
    page.goto("https://fourpark.vercel.app/login")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/login.png")
    page.fill('input[name="username"]', 'WhoopyEv')
    page.fill('input[name="password"]', 'Patrones1234')
    checkbox = page.query_selector('input[type="checkbox"]')
    if checkbox:
        checkbox.check()
    page.click('button:text("Iniciar sesión")')
    page.wait_for_load_state('networkidle')
    
    # Navegación y capturas de pantalla en varias páginas
    pages_to_capture = [
        "inicio-nologueado",
        "reserves/7",
        "maps",
        "actualizartc",
        "vreservas",
        "register",
        "forgot-password",
        "send-verify",
        "adminParkings",
        "admin/stats",
        "admin/parkings",
        "admin/users",
        "admin/admins",
        "admin/logs"
    ]

    for page_path in pages_to_capture:
        page.goto(f"https://fourpark.vercel.app/{page_path}")
        page.screenshot(path=f"C:/Users/HABI/Documents/Proyectos/Evidencias/{page_path.replace('/', '-')}.png")
    
    browser.close()
Notas
Asegúrate de tener las credenciales correctas para el inicio de sesión (WhoopyEv y Patrones1234 en el ejemplo).
Modifica las rutas de las capturas de pantalla según sea necesario.
El navegador se inicia en modo no headless para que puedas ver las acciones en tiempo real. Cambia headless=False a headless=True si prefieres que el navegador no sea visible.
