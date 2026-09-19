import os
from playwright.sync_api import sync_playwright

def run_practice_lab():
    # sample.html path 
    html_path = os.path.abspath("sample.html")
    
    with sync_playwright() as p:
        # ==========================================
        # PHASE 1 & 4: Browser Launch & Context Setup
        # ==========================================
        print("🚀 Launching Browser...")
        browser = p.chromium.launch(headless=False, slow_mo=500) # slow_mo 
        
        # Custom Headers ও User-Agent 
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) PlaywrightTester/1.0",
            extra_http_headers={"X-Practice-Mode": "true"}
        )
        page = context.new_page()
        
        # Local HTML open
        page.goto(f"file://{html_path}")
        print(f"📖 Page Opened. Title: {page.title()}")

 
        # PHASE 2 & 4: Elements Handling & Login
    
        print("\n🔐 Performing Login...")
        # Locators and Form Fill (Phase 2 & 4)
        page.locator("#username").fill("admin")
        page.locator("#password").fill("secret123")
        page.locator("#login-btn").click()
        
        # Cookie Check (Phase 4)
        cookies = context.cookies()
        print(f"🍪 Active Cookies after Login: {cookies}")
        
        # Storage State (Session) Save করা (Phase 4)
        context.storage_state(path="auth_state.json")
        print("💾 Session state saved to 'auth_state.json'")

     
        # PHASE 3: Dynamic Content & Waiting
      
        print("\n⏳ Triggering Dynamic Content...")
        page.get_by_role("button", name="Load Dynamic Products").click()
        
        # Auto-waiting / Manual waiting for dynamic elements 
        print("Waiting for dynamic product cards to appear...")
        page.wait_for_selector(".product-card", state="visible")

        # Screenshot  
        page.screenshot(path="dashboard_loaded.png")
        print("📸 Screenshot saved as 'dashboard_loaded.png'")

       
        # PHASE 3: Scraping Multiple Elements
    
        print("\n🕷️ Scraping Data...")
        # HTML/Content 
        full_html = page.content()
        
        # Multiple Product Scraping (Phase 3)
        product_cards = page.locator(".product-card").all()
        print(f"Found {len(product_cards)} products.")
        
        for idx, card in enumerate(product_cards, 1):
            # Text & Attributes Extraction (Phase 2 & 3)
            title = card.locator(".product-title").text_content()
            price = card.locator(".price").text_content()
            link = card.locator(".details-link").get_attribute("href")
            
            print(f"📦 Product {idx}: {title} | Price: {price} | URL: {link}")

      
        # PHASE 4: File Download
       
        print("\n📥 Testing File Download...")
        with page.expect_download() as download_info:
            page.locator("#download-link").click()
        
        download = download_info.value
        download.save_as("downloaded_report.pdf")
        print("📄 File successfully downloaded and saved as 'downloaded_report.pdf'")

   
        # PHASE 1: Page & Browser Close
    
        print("\n🧹 Cleaning up and closing browser...")
        page.close()
        context.close()
        browser.close()
        print("✅ Practice Lab Completed Successfully!")

if __name__ == "__main__":
    run_practice_lab()