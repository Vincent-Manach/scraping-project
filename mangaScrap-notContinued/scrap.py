import requests
from bs4 import BeautifulSoup

host="https://www.anime-planet.com/"

mangaName=input("Entrez le nom du manga recherché : ")

file= open("main.html", "w", encoding="utf-8")
file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Python Parsing</title>
</head>
<body>''')
for counter in range(10, 110, 10):

    page = requests.get(f'https://www.anime-planet.com/manga/all?name={mangaName}')

    soupdata = BeautifulSoup(page.content, "html.parser")
    # manga = BeautifulSoup(detailsInfo.title, "html.parser")

    results = soupdata.find_all("a", class_="tooltip")

    for result in results:
        img = result.find("img")
        # imgRef = img.find("src") 

        if('title' in result.attrs):
            title = result.find("h3", class_="cardName")
            detailsInfo = result.attrs
            vol = result.find("li", class_="iconVol")

        if ('data-class' in result.attrs):
            index = results.index(result)
            del results[index]

        # nmbrVol = soupdata.find('a')['title']
        # for ('title' in 'a'.attrs):
        #     detailsInfo = find("li", class_="iconVol")
        # if ('title' in 'a'.attrs):
        #     print('hello')
        # print(soupdata.find('title' in 'a'))
        file.write(f'''<div class="card">
    <div class="card-header">
    </div>
    <div class="card-body">
      
        <h5 class="card-title">{title}</h5>
        <img src="{img}">
        <ul>
            <li>{detailsInfo}</li>       
            <li>{vol}</li>        
        </ul>
    </div>
    </div>''')

file.write('''
</body>
</html>''')