import requests
from bs4 import BeautifulSoup

def get_amazon_price(product_name):
    url = "https://www.amazon.com/s?k={}".format(product_name.replace(" ", "+"))
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find("span", {"class": "a-price-whole"})
    if result:
        return float(result.get_text().replace(",", "."))
    return None

def get_flipkart_price(product_name):
    url = "https://www.flipkart.com/search?q={}".format(product_name.replace(" ", "+"))
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find("div", {"class": "_30jeq3 _1_WHN1"})
    if result:
        return float(result.get_text().replace("₹", "").replace(",", ""))
    return None

def get_ebay_price(product_name):
    url = "https://www.ebay.com/sch/i.html?_nkw={}".format(product_name.replace(" ", "+"))
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find("span", {"class": "s-item__price"})
    if result:
        return float(result.get_text().replace("$", "").replace(",", ""))
    return None

def get_lowest_price(product_name, websites):
    prices = []
    if websites[0]:
        price = get_amazon_price(product_name)
        if price:
            prices.append(price)
    if websites[1]:
        price = get_flipkart_price(product_name)
        if price:
            prices.append(price)
    if websites[2]:
        price = get_ebay_price(product_name)
        if price:
            prices.append(price)
    if len(prices) > 0:
        return min(prices)
    else:
        return None
