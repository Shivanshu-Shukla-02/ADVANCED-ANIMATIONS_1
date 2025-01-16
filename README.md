# ADVANCED-ANIMATIONS_1

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: SHIVANSHU SHUKLA

**INTERN ID**:CT08NFT

**DOMAIN**: CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION**: January 15th, 2025 to February 15th, 2025

**MENTOR NAME**: Neela Santhosh Kumar

# ENTER DESCRIPTION OF TASK PERFORMED NOT LESS THAN 500 WORDS


Objective
The primary aim is to develop a comprehensive tool to identify common web application vulnerabilities, specifically SQL Injection and Cross-Site Scripting (XSS). These vulnerabilities are prevalent and can lead to severe security breaches if not detected and mitigated.

Key Features and Capabilities
Web Crawling:

Purpose: To traverse through the web application's pages and gather URLs for analysis.

Implementation: Use the requests library to make HTTP requests and BeautifulSoup to parse HTML content. The tool will start from a base URL and follow internal links to ensure extensive coverage of the web application.

SQL Injection Detection:

Purpose: Identify potential SQL Injection points where attackers could execute arbitrary SQL commands.

Implementation: Send various SQL payloads to different parts of the web application, such as query parameters and form inputs. Analyze the responses for database error messages or unexpected behavior that indicates SQL code execution.

Cross-Site Scripting (XSS) Detection:

Purpose: Detect areas where an attacker could inject malicious scripts.

Implementation: Inject common XSS payloads into various inputs and observe the responses. Check if the payloads are executed or reflected in the HTML output, indicating a vulnerability.

Steps to Develop the Scanner
1. Setting Up the Environment
First, ensure the necessary libraries are installed. The requests library handles HTTP requests, and BeautifulSoup is used for parsing HTML content.

bash
pip install requests beautifulsoup4
2. Defining Vulnerability Checks
Implement functions to check for SQL Injection and XSS vulnerabilities. These functions will send crafted payloads to the target web application and analyze the responses.

SQL Injection Check:

python
import re

def check_sql_injection(url):
    sql_payloads = ["'", '"', " OR 1=1", "' OR '1'='1", " OR 'a'='a", " UNION SELECT"]
    for payload in sql_payloads:
        full_url = url + payload
        response = requests.get(full_url)
        if "error" in response.text or "syntax" in response.text:
            return True
    return False
XSS Check:

python
def check_xss(url):
    xss_payloads = ['<script>alert(1)</script>', '<img src=x onerror=alert(1)>']
    for payload in xss_payloads:
        response = requests.get(url, params={"q": payload})
        if payload in response.text:
            return True
    return False
3. Crawling the Website
Develop a function to crawl the website starting from a base URL, collecting all internal links for analysis. This function will use requests to fetch pages and BeautifulSoup to extract links.

python
def crawl_website(base_url):
    visited_urls = set()
    urls_to_visit = [base_url]

    while urls_to_visit:
        current_url = urls_to_visit.pop(0)
        if current_url in visited_urls:
            continue

        try:
            response = requests.get(current_url)
            visited_urls.add(current_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('http'):
                    urls_to_visit.append(href)
                else:
                    urls_to_visit.append(base_url + href)
        except requests.RequestException as e:
            print(f"Failed to access {current_url}: {e}")

    return visited_urls
4. Scanning for Vulnerabilities
Combine the crawling and vulnerability checks to scan the entire website. This function will iterate through all collected URLs, performing SQL Injection and XSS checks.

python
def scan_for_vulnerabilities(base_url):
    urls = crawl_website(base_url)
    for url in urls:
        if check_sql_injection(url):
            print(f"SQL Injection vulnerability detected at: {url}")
        if check_xss(url):
            print(f"XSS vulnerability detected at: {url}")
5. Running the Scanner
Finally, run the scanner with your target website's base URL.

python
if __name__ == "__main__":
    base_url = "http://example.com"
    scan_for_vulnerabilities(base_url)
Conclusion
This Python-based scanner provides a foundational tool for identifying SQL Injection and XSS vulnerabilities in web applications. The scanner leverages the requests library for making HTTP requests and BeautifulSoup for parsing and analyzing HTML content. While this example focuses on basic payloads and checks, it's essential to expand and refine the payloads for more robust detection. Moreover, consider incorporating additional security checks and reporting mechanisms to enhance the scanner's capabilities.
