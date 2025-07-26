import requests
from bs4 import BeautifulSoup

url = "https://www.timeanddate.com/weather/india/bhubaneswar"

try:
    res = requests.get(url)
    res.raise_for_status()  
except requests.exceptions.RequestException as e:
    print("Error fetching the URL:", e)
    exit()

soup = BeautifulSoup(res.text, "html.parser")


title = soup.title.string
print("Page Title:", title)


weather_info = soup.find('div', class_='h2')
if weather_info:
    print("Current Temperature:", weather_info.text.strip())
else:
    print("Temperature info not found.")


links = soup.find_all('a')
print("\n--- All Non-empty Links ---")
with open('links.txt', 'w', encoding='utf-8') as f:
    for link in links:
        href = link.get('href')
        text = link.text.strip()
        if href and text:
            print(text, "-", href)
            f.write(f"{text} - {href}\n")