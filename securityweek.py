import requests
import cloudscraper

# RSS feed URL
rss_url = "https://www.securityweek.com/feed/"

# Set headers to emulate a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.securityweek.com/",
}

# Attempt to fetch using requests
response = requests.get(rss_url, headers=headers)

if response.status_code == 200:
    print("RSS feed fetched successfully with requests.")
    with open("redpacketsecurity_feed.xml", "w", encoding="utf-8") as file:
        file.write(response.text)
else:
    print(f"Requests failed with status code {response.status_code}. Trying cloudscraper...")

    # Fallback to cloudscraper
    scraper = cloudscraper.create_scraper()
    response = scraper.get(rss_url)

    if response.status_code == 200:
        print("RSS feed fetched successfully with cloudscraper.")
        with open("securityweek_feed.xml", "w", encoding="utf-8") as file:
            file.write(response.text)
    else:
        print(f"Cloudscraper failed with status code {response.status_code}.")
