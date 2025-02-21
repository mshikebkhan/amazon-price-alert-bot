import requests
from bs4 import BeautifulSoup
from email_sender import send_email

def check_price(amazon_url, buy_price, user_email, user_password, recipient_email):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
        }
        response = requests.get(amazon_url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        price = soup.find(class_="a-price-whole").get_text().rstrip(".")

        if int(price.replace(",", "")) <= int(buy_price):
            send_email(user_email, user_password, recipient_email, amazon_url, price)

    except Exception as e:
        print(f"Error fetching price: {e}")
