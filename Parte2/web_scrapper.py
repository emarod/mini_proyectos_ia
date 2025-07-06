import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB
import os

db = TinyDB("products.json")

def scrape_books():
    db.truncate()  # Borra datos previos
    url = "http://books.toscrape.com/catalogue/page-1.html"

    while url:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        for article in soup.select("article.product_pod"):
            title = article.h3.a["title"]
            price = float(article.select_one(".price_color").text[2:])
            rating_str = article.p.get("class")[1]
            rating = ["Zero", "One", "Two", "Three", "Four", "Five"].index(rating_str)
            category = "Books"

            db.insert({
                "title": title,
                "price": price,
                "category": category,
                "rating": rating
            })

        next_btn = soup.select_one("li.next > a")
        if next_btn:
            next_page = next_btn["href"]
            url = "http://books.toscrape.com/catalogue/" + next_page
        else:
            url = None
