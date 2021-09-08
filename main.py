from selenium import webdriver
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(URL)

soup = BeautifulSoup(driver.page_source, "html.parser")
#print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

