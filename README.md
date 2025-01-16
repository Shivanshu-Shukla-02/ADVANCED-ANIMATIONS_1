# ADVANCED-ANIMATIONS_1

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: SHIVANSHU SHUKLA

**INTERN ID**:CT08NFT

**DOMAIN**: CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION**: January 15th, 2025 to February 15th, 2025

**MENTOR NAME**: Neela Santhosh Kumar

# ENTER DESCRIPTION OF TASK PERFORMED NOT LESS THAN 500 WORDS



Purpose:
The main objective is to create a comprehensive tool that can identify common vulnerabilities in web applications, particularly SQL injection and cross-site scripting (xss). These vulnerabilities are widespread and can result in significant security breaches if not identified and addressed.

Main Attributes and Functions Web scraping: The purpose of this task is to navigate through the web application's pages and collect URLs for further analysis.

Implementation: utilize the requests library to send http requests and beautifulsoup to extract html content. The tool will begin at a base URL and follow internal links to guarantee comprehensive coverage of the web application.

Detection of SQL Injection Attacks.

The purpose of this exercise is to identify potential vulnerabilities in the system where attackers could execute arbitrary SQL commands.

Implementation: send different types of SQL payloads to various sections of the web application, including query parameters and form inputs. Examine the feedback for database error messages or unusual actions that suggest the sql code is being executed.

SQL Injection Detection:

Purpose: Identify potential SQL Injection points where attackers could execute arbitrary SQL commands.

Implementation: Send various SQL payloads to different parts of the web application, such as query parameters and form inputs. Analyze the responses for database error messages or unexpected behavior that indicates SQL code execution.

Cross-site scripting (xss) detection: The purpose of this analysis was to identify potential vulnerabilities in the system that could be exploited by attackers to inject malicious scripts.

Implementation: inject common xss payloads into different inputs and observe the corresponding responses. Verify if the payloads are implemented or displayed in the HTML output, suggesting a potential vulnerability.

Steps to create the scanner.
1: Establishing the Conditions.
Before proceeding, make sure to install the required libraries. The requests library is responsible for handling http requests, while beautifulsoup is utilized for parsing html content.

Bash: Pip install requests beautifulsoup4.
2: Identifying Weaknesses
Implement measures to verify the absence of SQL injection and cross-site scripting vulnerabilities. These functions will deliver customized payloads to the target web application and evaluate the responses.
SQL Injection Check:

python
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
coclution:
This Python-based scanner serves as a fundamental tool for detecting vulnerabilities related to SQL injection and cross-site scripting (xss) in web applications. The scanner utilizes the requests library for making HTTP requests and beautifulsoup for parsing and analyzing HTML content. While this example focuses on simple payloads and checks, it's crucial to expand and refine the payloads for more comprehensive detection capabilities. Furthermore, take into account the implementation of additional security measures and reporting systems to further improve the scanner's functionality.
