import requests
from bs4 import BeautifulSoup

def get_flipkart_price(search_query):
    query = search_query.replace(" ", "+")
    url = f"https://www.flipkart.com/search?q= {query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Try to find product title and price
    product = soup.find("div", class_="_4rR01T")  # for laptops, phones etc.
    price = soup.find("div", class_="_30jeq3 _1_WHN1")

    if product and price:
        print(f"Product: {product.text.strip()}")
        print(f"Price: {price.text.strip()}")
    else:
        print("Product not found or page layout has changed.")

# Example usage
product_name = input("Enter product to search on Flipkart: ")
get_flipkart_price(product_name)