from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://fourpark.vercel.app/login")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/login.png")
    page.fill('input[name="username"]', 'WhoopyEv')
    page.fill('input[name="password"]', 'Patrones1234')
    checkbox = page.query_selector('input[type="checkbox"]')
    if checkbox:
        checkbox.check()
    page.click('button:text("Iniciar sesión")')
    page.wait_for_load_state('networkidle')
    page.goto("https://fourpark.vercel.app/inicio-nologueado")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/inicio-nologueado.png")
    page.goto("https://fourpark.vercel.app/reserves/7")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/inicio-reserves7.png")
    page.goto("https://fourpark.vercel.app/maps")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/maps.png")
    
    page.goto("https://fourpark.vercel.app/actualizartc")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/actualizartc.png")
    
    page.goto("https://fourpark.vercel.app/vreservas")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/vreservas.png")
    
    page.goto("https://fourpark.vercel.app/register")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/register.png")
    
    page.goto("https://fourpark.vercel.app/forgot-password")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/forgot-password.png")
    
    page.goto("https://fourpark.vercel.app/send-verify")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/send-verify.png")
    
    page.goto("https://fourpark.vercel.app/adminParkings")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/adminParkings.png")
    
    page.goto("https://fourpark.vercel.app/admin/stats")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/admin-stats.png")
    
    page.goto("https://fourpark.vercel.app/admin/parkings")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/admin-parkings.png")
    
    page.goto("https://fourpark.vercel.app/admin/users")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/admin-users.png")
    
    page.goto("https://fourpark.vercel.app/admin/admins")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/admin-admins.png")
    
    page.goto("https://fourpark.vercel.app/admin/logs")
    page.screenshot(path="C:/Users/HABI/Documents/Proyectos/Evidencias/admin-logs.png")
    browser.close()