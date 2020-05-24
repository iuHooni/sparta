import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Initializing dbspart in Mongodb
client = MongoClient(host='localhost', port=27017)
db = client.dbsparta

# Crawling movie.naver.com
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    rank_tag = movie.select_one('td.ac > img')
    title_tag = movie.select_one('td.title > div > a')
    point_tag = movie.select_one('td.point')

    if rank_tag is not None:
        # Saving movie_list data to DB
        movieinfo = {
            'title': title_tag.text,
            'rank': rank_tag['alt'],
            'point': point_tag.text
        }
        db.movies.insert_one(movieinfo)