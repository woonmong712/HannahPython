import requests
from bs4 import BeautifulSoup

url = 'https://weworkremotely.com/remote-full-time-jobs'

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

all_jobs = []

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser",)

    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]  # 첫 번째와 마지막 항목을 제외
    for job in jobs:
        title = job.find("span", class_="title").text.strip()
        company = job.find_all("span", class_="company")[0].text.strip()
        position = job.find_all("span", class_="company")[1].text.strip()
        region = job.find_all("span", class_="company")[2].text.strip()
        url = job.find("div",class_="tooltip").find_next_sibling["href"]
        
        job_data = {
            "title": title,
            "company": company,
            "position": position,
            "region": region,
            "url":url
        }
        all_jobs.append(job_data)

buttons = soup.find("div",class_="pagination").find_all("span",class_="page")

print(buttons)
