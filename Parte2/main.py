from fastapi import FastAPI, Query
from tinydb import TinyDB, Query as TinyQuery
from typing import Optional

app = FastAPI()
db = TinyDB("products.json")
Product = TinyQuery()

@app.get("/scrape")
def scrape():
    from web_scrapper import scrape_books
    scrape_books()
    return {"message": "Scraping completo"}

@app.get("/products")
def get_products(
    title: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
):
    results = db.all()

    if title:
        results = [p for p in results if title.lower() in p["title"].lower()]
    if category:
        results = [p for p in results if category.lower() in p["category"].lower()]
    if min_price:
        results = [p for p in results if p["price"] >= min_price]
    if max_price:
        results = [p for p in results if p["price"] <= max_price]
    if min_rating:
        results = [p for p in results if p["rating"] >= min_rating]

    return results
