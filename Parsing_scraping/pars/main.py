
from bs4 import BeautifulSoup

with open(r"blank/index.html", encoding='utf-8') as file:
    src = file.read()
#print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title
#print(title)
#print(title.text)
#print(title.string)

#.find(...)    .find_all(....)


#page_h1 = soup.find("h1")  Вывод только одну строку
#print(page_h1)

# page_all_h1 = soup.find_all("h1")  #Выводит все строки h1 в список
# print(page_all_h1)
#
# for item in page_all_h1:
#     print(item.text)


# user_name = soup.find("div", class_= "user__name")
# print(user_name.text.strip())

# user_name = soup.find("div", class_= "user__name").find("span").text   #.text выводит только текст в теге, если без , то вывод full строки
# print(user_name)  5:59!