from bs4 import BeautifulSoup
import requests

# with open("website.html") as html:
#     file = html.read()

# html = BeautifulSoup(file, "html.parser")
# print(html.title)
# all_a = html.find_all(name="a",)
# print(all_a)
# single_a = html.find(name="a", id="ferhat")
# print(single_a.getText())
# single_b = html.find(name="a", class_="adi")
# print(single_b.getText())
# With Selector... You are writing selector just as in css
# result = html.select(".ulist li")
# print(result)

# with open("sample1.xml") as xmlFile:
#     xml = xmlFile.read()
#
# xml = BeautifulSoup(xml, "lxml-xml")
# print(xml)

# website = requests.get("https://news.ycombinator.com/news")
# website_html = website.text
# scraped_website = BeautifulSoup(website_html, "html.parser")
#
# texts = []
# links = []
#
# for item in scraped_website.select(".titleline > a "):
#     texts.append(item.getText())
#     links.append(item.get("href"))
#
# scores = [int((score.getText()).split()[0]) for score in scraped_website.find_all("span", class_="score")]
# max_item = max(scores)
# max_item_index = scores.index(max_item)
#
# print(texts[max_item_index])
# print(links[max_item_index])


# Final project

movie_website = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
html_movie_website = movie_website.text
scraped_movie_website = BeautifulSoup(html_movie_website, "html.parser")
movies_list = [movie.getText() for movie in scraped_movie_website.find_all("h3")]

for movie in movies_list[::-1]:
    with open("movie.txt", "a") as file:
        file.write(f"{movie}\n")

for n in range(len(movies_list) - 1, -1, -1):
    print(movies_list[n])
