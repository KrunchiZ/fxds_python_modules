import requests
from bs4 import BeautifulSoup

url = "https://weather.com/my/city/kuala-lumpur/today"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://example.com/",
}


def main():
    html_content: str = None
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html_content = response.text
        else:
            print(f"Request failed with status code: {response.status_code}")
            return
    except Exception as e:
        print(f"Error: {e}")
        return

    soup = BeautifulSoup(html_content, "html.parser")
    data = soup.find("span", attrs={"class": "leading-[88px]"})
    print(f"Data found: {data}\n")
    data = data.find("span", attrs={"data-testid": "TemperatureValue"})
    if data:
        print(f"The temperature is {data.text}")
    else:
        print(f"Could not find temperature information.")


if __name__ == "__main__":
    main()