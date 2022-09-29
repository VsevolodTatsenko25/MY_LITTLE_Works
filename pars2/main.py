import requests
from bs4 import BeautifulSoup

url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

headers = {
    "Accept": "*/*"
}
req = requests.get(url)