import mysql.connector
import requests
from bs4 import BeautifulSoup
baseUrl = "https://movie.douban.com/top250?start=%d&filter="
def get_movies(start):
    url = baseUrl % start
    lists = []
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    items = soup.find("ol", "grid_view").find_all("li",limit=20)
    for i in items:
        movie = {}
        movie["rank"] = i.find("em").text
        movie["link"] = i.find("div","pic").find("a").get("href")
        #movie["poster"] = i.find("div","pic").find("a").find('img').get("src")
        movie["name"] = i.find("span", "title").text
        #movie["score"] = i.find("span", "rating_num").text
        #movie["quote"] = i.find("span", "inq").text if(i.find("span", "inq")) else ""
        nexturl=movie["link"]
        print(nexturl)
        nexthtml=requests.get(nexturl)
        nextsoup = BeautifulSoup(nexthtml.content, "html.parser")
        movie["body"]=nextsoup.find("div","related-info").find("span","all hidden").text if(nextsoup.find("div","related-info").find("span","all hidden")) else nextsoup.find("div","related-info").find("span",attrs={"property":"v:summary"}).text
        #print(movie["body"])
        #movie["body"]=""
        lists.append(movie)
    return lists

if __name__ == "__main__":
    db = mysql.connector.connect(host="localhost",user="root",password="root",db="test",charset="utf8mb4")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS movies")
    createTab = """CREATE TABLE movies(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        body text CHARACTER SET utf8 COLLATE utf8_general_ci ,
        rank VARCHAR(4) NOT NULL,
        link VARCHAR(50) NOT NULL
    )"""
    cursor.execute(createTab)
    start = 0
    #while (start < 250):
    lists = get_movies(start)
    for i in lists:
        sql = "INSERT INTO `movies`(`name`,`body`,`rank`,`link`) VALUES(%s,%s,%s,%s)"
        try:
            cursor.execute(sql, (i["name"],i["body"], i["rank"], i["link"]))
            db.commit()
            print(i["name"]+" is success")
        except:
            db.rollback()
        #start += 25
    db.close()