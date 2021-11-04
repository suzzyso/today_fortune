import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('mongodb://test:test@localhost', 27017)
#client = MongoClient('13.125.44.145', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.animal                      # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
from requests import Response

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data_mouse = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%A5%90%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_cow = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%86%8C%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_tiger = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%98%B8%EB%9E%91%EC%9D%B4%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_rabbit = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%86%A0%EB%81%BC%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_dragon = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%9A%A9%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_snake = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%B1%80%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_horse = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%A7%90%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_sheep = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%96%91%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_monkey = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%9B%90%EC%88%AD%EC%9D%B4%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_chicken = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%8B%AD%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_dog = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EA%B0%9C%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)
data_pig = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%8F%BC%EC%A7%80%EB%9D%A0%20%EC%9A%B4%EC%84%B8',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup_mouse = BeautifulSoup(data_mouse.text, 'html.parser')
soup_cow = BeautifulSoup(data_cow.text, 'html.parser')
soup_tiger = BeautifulSoup(data_tiger.text, 'html.parser')
soup_rabbit = BeautifulSoup(data_rabbit.text, 'html.parser')
soup_dragon = BeautifulSoup(data_dragon.text, 'html.parser')
soup_snake = BeautifulSoup(data_snake.text, 'html.parser')
soup_horse = BeautifulSoup(data_horse.text, 'html.parser')
soup_sheep = BeautifulSoup(data_sheep.text, 'html.parser')
soup_monkey = BeautifulSoup(data_monkey.text, 'html.parser')
soup_chicken = BeautifulSoup(data_chicken.text, 'html.parser')
soup_dog = BeautifulSoup(data_dog.text, 'html.parser')
soup_pig = BeautifulSoup(data_pig.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
fortune_mouse = soup_mouse.select('#yearFortune > div')
fortune_cow = soup_cow.select('#yearFortune > div')
fortune_tiger = soup_tiger.select('#yearFortune > div')
fortune_rabbit = soup_rabbit.select('#yearFortune > div')
fortune_dragon = soup_dragon.select('#yearFortune > div')
fortune_snake = soup_snake.select('#yearFortune > div')
fortune_horse = soup_horse.select('#yearFortune > div')
fortune_sheep = soup_sheep.select('#yearFortune > div')
fortune_monkey = soup_monkey.select('#yearFortune > div')
fortune_chicken = soup_chicken.select('#yearFortune > div')
fortune_dog = soup_dog.select('#yearFortune > div')
fortune_pig = soup_pig.select('#yearFortune > div')

db.fortune.drop()

for fortune in fortune_mouse:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' +today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_cow:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_tiger:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_rabbit:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_dragon:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_snake:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_horse:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_sheep:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_monkey:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_chicken:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_dog:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_pig:
    name = fortune.select_one('#yearFortune > div > div.detail > h6 > ul > li').text
    today_text = fortune.select_one('#yearFortune > div > div.detail > p').text
    first_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(1)').text
    first_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(2)').text
    second_year = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dt:nth-child(3)').text
    second_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(4)').text
    third_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(5)').text
    third_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(6)').text
    fourth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(7)').text
    fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(8)').text
    fifth_year = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dt:nth-child(9)').text
    fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(5) > dd:nth-child(10)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(4)').text
    t_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(2)').text
    t_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(4)').text
    t_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(6)').text
    t_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(8)').text
    t_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(6) > dd:nth-child(10)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(5)').text
    w_first_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(2)').text
    w_second_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(4)').text
    w_third_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(6)').text
    w_fourth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(8)').text
    w_fifth_text = fortune.select_one('#yearFortune > div > dl:nth-child(7) > dd:nth-child(10)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail > p:nth-child(6)').text

    if name is not None:
        #띠별 운세
        print(name)
        print('오늘의 운세 : ' + today_text)
        print(first_year + ' : ' + first_text)
        print(second_year + ' : ' + second_text)
        print(third_year + ' : ' + third_text)
        print(fourth_year + ' : ' + fourth_text)
        print(fifth_year + ' : ' + fifth_text)
        print('내일의 운세 : ' + tomorrow_text)
        print(first_year + ' : ' + t_first_text)
        print(second_year + ' : ' + t_second_text)
        print(third_year + ' : ' + t_third_text)
        print(fourth_year + ' : ' + t_fourth_text)
        print(fifth_year + ' : ' + t_fifth_text)
        print('이주의 운세 : ' + week_text)
        print(first_year + ' : ' + w_first_text)
        print(second_year + ' : ' + w_second_text)
        print(third_year + ' : ' + w_third_text)
        print(fourth_year + ' : ' + w_fourth_text)
        print(fifth_year + ' : ' + w_fifth_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'name': name,
            'today_text': today_text,
            'first_year': first_year,
            'first_text': first_text,
            'second_year': second_year,
            'second_text': second_text,
            'third_year': third_year,
            'third_text': third_text,
            'fourth_year': fourth_year,
            'fourth_text': fourth_text,
            'fifth_year': fifth_year,
            'fifth_text': fifth_text,
            'tomorrow_text': tomorrow_text,
            't_first_text': t_first_text,
            't_second_text': t_second_text,
            't_third_text': t_third_text,
            't_fourth_text': t_fourth_text,
            't_fifth_text': t_fifth_text,
            'week_text': week_text,
            'w_first_text': w_first_text,
            'w_second_text': w_second_text,
            'w_third_text': w_third_text,
            'w_fourth_text': w_fourth_text,
            'w_fifth_text': w_fifth_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)


