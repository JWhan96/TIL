import requests
from bs4 import BeautifulSoup

def crawling_basic():
    # 가져올 웹 페이지 url
    url = 'http://quotes.toscrape.com/tag/love/'

    response = requests.get(url)

    # 우리가 얻고자 하는 HTML내용이 여기에 담긴다
    html_text = response.text

    #HTML을 파싱이 가능한 정리된 형태로 변환
    soup = BeautifulSoup(html_text, 'html.parser')

    #예쁘게 출력
    # print(soup.prettify())

    # 1. 태그로 검색하기
    # 1.1 가장 첫 번째 태그에 해당하는 요소
    # 크롤링 할 때는 항상 페이지 분석 -> 검색
    title = soup.find('a')
    print(f'제목: {title}') # html태그까지
    print(f'제목: {title.text}') # text만(나중에 자바스크립트 배우면서 배움)

    # 1.2 해당 태그 모든 요소
    a_tags = soup.find_all('a') # 리스트 형태
    for a_tag in a_tags:
        print(f'a 태그들 = {a_tag}')

    # 2. CSS 선택자로 검색하기
    # 2.1 첫번째로 CSS선택자와 일치하는 요소
    word = soup.select_one('.text')
    print(f'첫번째 글 = {word.text}')

    # 2.2 CSS선택자와 일치하는 모든 욧
    words = soup.select('.text') #왜 .text???
    for w in words:
        print(f'글: {w.text}')
    

crawling_basic()