from playwright.sync_api import sync_playwright
import json
import csv


URL = "https://books.toscrape.com/"


with sync_playwright() as p:

   
    # PHASE 1
    # Browser + Page
   

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(URL)

    print("Page opened:", page.title())


    # Screenshot
    page.screenshot(
        path="books_page.png",
        full_page=True
    )


    # PHASE 2
    # Locator
  

    products = page.locator(
        "article.product_pod"
    )

    print("Products:", products.count())



    # PHASE 3
    # Multiple product scraping


    all_books = []


    for i in range(products.count()):

        product = products.nth(i)

        # Title
        title = product.locator(
            "h3 a"
        ).get_attribute("title")


        # Price
        price = product.locator(
            ".price_color"
        ).text_content()


        # Product link
        link = product.locator(
            "h3 a"
        ).get_attribute("href")


        # Image
        image = product.locator(
            "img"
        ).get_attribute("src")


        book = {
            "title": title,
            "price": price.strip(),
            "link": link,
            "image": image
        }

        all_books.append(book)


  
    # Output
    

    for book in all_books:

        print("\n----------------")

        print("Title:", book["title"])
        print("Price:", book["price"])
        print("Link:", book["link"])
        print("Image:", book["image"])


    # =====================================
    # Pagination
    # =====================================

    next_button = page.locator(
        "li.next a"
    )


    if next_button.count() > 0:

        print("\nNext page available!")

        next_button.click()

        # Dynamic page load
        page.locator(
            "article.product_pod"
        ).first.wait_for()

        print(
            "Next page:",
            page.url
        )


    # =====================================
    # PHASE 4
    # Multiple page/tab concept
    # =====================================

    new_page = browser.new_page()

    new_page.goto(
        "https://books.toscrape.com/catalogue/category/books_1/index.html"
    )

    print(
        "Second page title:",
        new_page.title()
    )


    # =====================================
    # Save JSON
   

    with open(
        "books.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            all_books,
            file,
            ensure_ascii=False,
            indent=4
        )


    # =====================================
    # Save CSV
    # =====================================

    with open(
        "books.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "title",
            "price",
            "link",
            "image"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(all_books)


    print("\nScraping completed!")

    print("Saved:")
    print("books.json")
    print("books.csv")


    # Close/////////////////////////////////////////////////////

    browser.close()