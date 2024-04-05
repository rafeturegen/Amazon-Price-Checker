import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"

headers = {
    "User-Agent":  USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
}
response = requests.get(AMAZON_URL, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

price_dot = soup.find(name="span", class_="a-price-whole").getText()
print(price_dot)
price_list = price_dot.split(".")
price = price_list[0]
print(price_dot)

product_name = soup.find(name="span", id="productTitle").getText()

my_email = "rafetcode@gmail.com"
password = "secret"
message = f"{product_name.strip()} is now {price}$".encode('ascii', 'ignore').decode()

if float(price) <= 120:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="rafetcode@yahoo.com",
                            msg=f"Subject:Amazon Price Alert\n\n{message}\n{AMAZON_URL}"
                            )



