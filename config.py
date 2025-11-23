"""
Конфигурация тестов API Авито
"""

BASE_URL = "https://qa-internship.avito.com"

ENDPOINTS = {
    "create_item": "/api/1/item",
    "get_item": "/api/1/item/{id}",
    "get_seller_items": "/api/1/{sellerId}/item", 
    "get_statistics": "/api/1/statistic/{id}"
}

import random

def generate_seller_id():
    return random.randint(111111, 999999)

def generate_item_data(seller_id=None):
    if seller_id is None:
        seller_id = generate_seller_id()
    
    return {
        "sellerID": seller_id,
        "name": f"Test Item {random.randint(1000, 9999)}",
        "price": random.randint(100, 10000),
        "statistics": {
            "likes": random.randint(0, 100),
            "viewCount": random.randint(0, 1000),
            "contacts": random.randint(0, 50)
        }
    }

DEFAULT_HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}