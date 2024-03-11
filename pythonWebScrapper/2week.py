# berlinstartupjobs.com 웹사이트용 스크래퍼를 만듭니다.
# 스크래퍼는 다음 URL을 스크랩할 수 있어야 합니다:
# https://berlinstartupjobs.com/engineering/
# https://berlinstartupjobs.com/skill-areas/python/
# https://berlinstartupjobs.com/skill-areas/typescript/
# https://berlinstartupjobs.com/skill-areas/javascript/
# 첫 번째 URL에는 페이지가 있으므로 pagination 을 처리해야 합니다.
# 나머지 URL은 특정 스킬에 대한 것입니다. URL의 구조에 스킬 이름이 있으므로 모든 스킬을 스크래핑할 수 있는 스크래퍼를 만드세요.
# 회사 이름, 직무 제목, 설명 및 직무 링크를 추출하세요.

import requests
from bs4 import BeautifulSoup

# 스킬별 직무 정보를 스크래핑하는 함수
def scrape_jobs_for_skill(skill):
    url = f"https://berlinstartupjobs.com/engineering/?s={skill}"
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    )

    soup = BeautifulSoup(response.content, 'html.parser')
    job_posts = soup.find_all('div', class_='product-listing-h2')

    for post in job_posts:
        title = post.find('a').get_text(strip=True)
        company = post.find('h5').get_text(strip=True)
        link = post.find('a')['href']
        description = post.find_next_sibling('div', class_='job-details').get_text(strip=True) if post.find_next_sibling('div', class_='job-details') else "No description"

        print(f"회사 이름: {company}")
        print(f"직무 제목: {title}")
        print(f"설명: {description}")
        print(f"직무 링크: {link}\n")
    print(f"--- {skill} 검색 완료 ---\n")

# 주어진 스킬 리스트를 사용하여 각 스킬별로 스크래핑 실행
skills = ["python", "typescript", "javascript", "rust"]

for skill in skills:
    print(f"{skill} 스킬에 대한 직무 정보를 스크래핑합니다...")
    scrape_jobs_for_skill(skill)

# pagination
buttons = soup.find("ul",class_="bsj-nav").find_all("span",class_="page-numbers")