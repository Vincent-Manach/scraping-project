import requests
from bs4 import BeautifulSoup

movieName=input("Entrez le nom du film recherché : ")

file= open("main.html", "w", encoding="utf-8")
file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link href="style.css" rel="stylesheet">
    <title>Python Parsing - Movies</title>
</head>
<body>''')

for counter in range(0, 1):

    page = requests.get(f'https://www.allocine.fr/rechercher/movie/?q={movieName}')

    soupdata = BeautifulSoup(page.content, "html.parser")

    results = soupdata.find_all("li", class_="mdl")

    file.write(f'''
    <header>
        <h1>Résultats pour "{movieName}"</h1>
    </header>
    ''')

    for result in results:
        index = results.index(result)
        title = result.find("h2", class_="meta-title")
        description = result.find("div", class_="content-txt")
        if description == None:
            description = "Synopsis non disponible"
        release = result.find("span", class_="date")
        if release == None:
            release = "Date de sortie inconnue"
        notes = result.find_all("span", class_="stareval-note")
        pressNote = notes[0].text
        publicNote = notes[1].text
        img = result.find("img", class_="thumbnail-img")
        imgRef = img.get("data-src")
        
        file.write(f'''<div class="card">
    <div class="card-img">
        <img src="{imgRef}" alt="affiche du film" width="310">
    </div>
    <div class="card-body">
        <h3 class="card-title">{title.text}</h3><br>
        <p class="release"><strong>Date de sortie : </strong>{release}</p><br>
        <p><em>{description}</em></p><br>
        <div class="notes">
            <div class="press-note">
                <h5>Note de la presse</h5>
                <p>Note de la presse : {pressNote}/5</p>
            </div>
            <div class="public-note">
                <h5>Note de la presse</h5>
                <p>Note du public : {publicNote}/5</p>
            </div>
        </div>        
    </div>
    </div>''')

file.write('''
</body>
</html>''')