import requests
from bs4 import BeautifulSoup

def scrape_codechef_profile(username):
    url = f"https://www.codechef.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    
    profile = {
        "username": username,
        "name": soup.find("h1", {"class": "h2-style"}).get_text(strip=True) if soup.find("h1", {"class": "h2-style"}) else None,
        "rating": soup.find("div", {"class": "rating-number"}).get_text(strip=True) if soup.find("div", {"class": "rating-number"}) else None,
        "stars": soup.find("span", {"class": "rating"}).get_text(strip=True) if soup.find("span", {"class": "rating"}) else None,
        "country": soup.find("span", {"class": "user-country-name"}).get_text(strip=True) if soup.find("span", {"class": "user-country-name"}) else None,
        "global_rank": soup.find("div", {"class": "rating-ranks"}).find("a").get_text(strip=True) if soup.find("div", {"class": "rating-ranks"}) else None,
    }

    return profile

username = "kl_cseh_30053"  # Replace with actual CodeChef username
profile_data = scrape_codechef_profile(username)

if profile_data:
    print("+------------------+")
    print("| CodeChef Profile |")
    print("+------------------+")
    for key, value in profile_data.items():
        print(f"{key}: {value}")
