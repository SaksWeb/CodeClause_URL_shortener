import string
import random

url_mapping = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

def shorten_url(long_url):
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return short_url

def expand_url(short_url):
    return url_mapping.get(short_url, None)

# Example usage
long_url = input("Enter the url: ")
short_url = shorten_url(long_url)
print(f"Short URL: {short_url}")
print(f"Expanded URL: {expand_url(short_url)}")
