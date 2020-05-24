import requests
from bs4 import BeautifulSoup


# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')

movie_list = dict()
for movie in movies:
    rank_tag = movie.select_one('td.ac > img')
    title_tag = movie.select_one('td.title > div > a')
    point_tag = movie.select_one('td.point')

    if rank_tag is not None:
        movie_list[title_tag.text] = {'rank': rank_tag['alt'],
                                      'point': point_tag.text}

for movie in movie_list:
    print(movie_list[movie]['rank'], movie, movie_list[movie]['point'])
