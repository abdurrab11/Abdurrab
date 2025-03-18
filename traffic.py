import requests
from collections import Counter
import time

# Function to analyze web server logs
def analyze_traffic(log_file):
    ips = []
    with open(log_file, "r") as file:
        for line in file:
            ips.append(line.split()[0])  # Assuming IP is the first element

    ip_count = Counter(ips)
    print("Top 10 IPs by traffic:")
    for ip, count in ip_count.most_common(10):
        print(f"{ip}: {count} visits")

# Function to monitor website uptime
def monitor_website(url, interval=300):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{url} is up!")
            else:
                print(f"{url} returned status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        time.sleep(interval)

# Function to check SEO metrics
def check_seo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Check title
    title = soup.title.string if soup.title else "No title found"
    print(f"Title: {title}")
    
    # Check meta description
    meta_description = soup.find("meta", attrs={"name": "description"})
    if meta_description:
        print(f"Meta Description: {meta_description['content']}")
    else:
        print("No meta description found")
    
    # Check headings
    headings = soup.find_all(["h1", "h2", "h3"])
    print("Headings:")
    for heading in headings:
        print(f"{heading.name}: {heading.text.strip()}")

# Main function
def main():
    log_file = "access.log"  # Replace with your server log file
    website_url = "https://example.com"  # Replace with your website URL

    print("Analyzing traffic...")
    analyze_traffic(log_file)

    print("\nMonitoring website uptime...")
    monitor_website(website_url)

    print("\nChecking SEO metrics...")
    check_seo(website_url)

if __name__ == "__main__":
    main()