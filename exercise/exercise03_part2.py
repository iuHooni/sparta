from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta 

# 영화제목 '매트릭스'의 평점을 가져오기
matrix = list(db.movies.find({'title': '매트릭스'}))
matrix_point = matrix[0]['point']
print(matrix_point)

# '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
same_point = list(db.movies.find({'point': matrix_point}))
for movie in same_point:
    print(movie['title'])

# '매트릭스'의 평점과 같은 평점의 영화 제목들의 평점을 0으로 만들기
db.movies.update_many({'point': matrix_point}, {'$set':{'point': 0}})