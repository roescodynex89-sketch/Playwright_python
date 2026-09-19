# Playwright Automation & Web Scraping Practice Lab

A comprehensive practice project covering core concepts of **Playwright (Python)** for browser automation and web scraping. This project demonstrates end-to-end testing and data extraction workflows using a local simulated environment (`sample.html`).

## 🚀 What I Have Learned

### Phase 1: Browser Basics
* **Installation & Setup:** Configured Playwright with python environment (`pip install playwright` & `playwright install`).
* **Browser Lifecycle:** Managed browser instantiation, launching targeted browser engines (Chromium), opening isolated contexts/pages, and handling clean resource teardowns.
* **Page Content Retrieval:** Used `page.content()` to grab raw HTML page source for scraping or audit validation.
* **Visual Snapshots:** Captured accurate UI states using `page.screenshot()`.

### Phase 2: Web Elements & Interactions
* **Locators Engine:** Mastered Playwright's `locator()` system and standard locator APIs.
* **Semantic Targetting:** Utilized human-centric structural locators like `get_by_role()` and text matches via `get_by_text()`.
* **Traditional Selectors:** Implemented classic locator methodologies including strict **CSS Selectors** and reliable **XPath** expressions.
* **Simulated Actions:** Drove human-like web interactions using `.fill()` (data inputs), `.click()` (mouse interactions), and `.press()` (dispatching structural keyboard events like `Enter`).
* **Content Extraction:** Extracted runtime DOM metrics using `.text_content()` and specified structural details via `.get_attribute()`.

### Phase 3: Web Scraping Strategies
* **Multi-Element Evaluation:** Utilized `.all()` to grab dynamic element arrays and process collections sequentially inside a loop.
* **Asynchronous Elements:** Handled dynamic content injections via API/JS effortlessly through explicit waiting utilities (`page.wait_for_selector()`).
* **Data Parsing:** Combined text extractions and attribute parsing into structural dictionary matrices (e.g., extracting title, price, and target hyperlinks together).

### Phase 4: Advanced Browser Automation
* **Authentication Flows:** Simulated stateful user validation routines inside custom application logins.
* **State Management:** Intercepted operational browser states (`page.context.cookies()`) and saved operational tokens to a persistent `storage_state` JSON file for session persistence.
* **Networking Controls:** Injecting mock custom identities into systemic browser headers (e.g., custom `User-Agent` strings).
* **IO Lifecycle Interception:** Handled file downloads cleanly through functional promise-like wrapper patterns via `page.expect_download()`.

---

## 🏃 How to Run the Laboratory

1. Clone or download this project workspace.
2. Install required dependencies:
   ```bash
   pip install playwright
   playwright install
   ```
3. Run the automated automation sequence:
   ```bash
   python sample.py
   ```