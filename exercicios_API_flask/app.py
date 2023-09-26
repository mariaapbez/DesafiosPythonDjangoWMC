from flask import Flask, render_template
import urllib.request, json, re
 
app = Flask(__name__)

@app.route("/")
def get_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict_character = json.loads(data)
    
    return render_template("characters.html", characters=dict_character["results"]) # "characters.html" é o código html criado com o template a ser utilizado para os dados coletados, com todos os personagens da série contidos na lista "results" que está na url descrita.

#Exercício 5: --------------------------------------------------------------------------------

#Na página de perfil do personagem, adicione as seguintes informações: espécie, gênero, origem e localização. As informações de origem, localização e episódios em que o personagem aparece devem conter um link para a página de perfil da localização.-->

@app.route("/profile/<id>")
def get_profile_page(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict_profile = json.loads(data)

    url_2 = "https://rickandmortyapi.com/api/episode/?page="
    response_2 = urllib.request.urlopen(url_2)
    data_2 = response_2.read()
    dict_profile_2 = json.loads(data_2)

    character_episodes_infos = []
    
    for episode in dict_profile["episode"]: #list
        episode_url = episode
        id_episode = re.findall("\d+", episode_url)
        id_episode_num = int("".join(id_episode))
      
        for item in dict_profile_2["results"]:
            if id_episode_num == item["id"]: #list
                character_episode = {
                    "id": id_episode_num,
                    "name": item["name"]
                    }

                character_episode_copy = character_episode.copy()
                character_episodes_infos.append(character_episode_copy)

    #return (f"{character_episode} - {id_episode_num} - {episode_url} - {url_2} - {character_episodes_infos}") ---->  verificar variáveis
              
    url_3 = "https://rickandmortyapi.com/api/location/?page="
    response_3 = urllib.request.urlopen(url_3)
    data_3 = response_3.read()
    dict_profile_3 = json.loads(data_3)

    character_location_id = []
        
    location_url = dict_profile["location"]["url"]
    id_location = re.findall("\d+", location_url)
    id_location_num = int("".join(id_location))
      
    for item in dict_profile_3["results"]:
        if id_location_num == item["id"]: #list
            character_location = {
                "id": id_location_num,
                }

            character_location_copy = character_location.copy()
            character_location_id.append(character_location_copy)

    #return (f"{character_location} - {id_location_num} - {location_url} - {url_3} - {character_location_id}") ---->  verificar variáveis

    url_4 = "https://rickandmortyapi.com/api/location/?page="
    response_4 = urllib.request.urlopen(url_4)
    data_4 = response_4.read()
    dict_profile_4 = json.loads(data_4)

    character_origin_id = []
    
    location_url = dict_profile["origin"]["url"]
    id_location = re.findall("\d+", location_url)
    id_location_num = ("".join(id_location))
      
    for item in dict_profile_4["results"]:  
        if id_location_num == item["id"]:  
                character_origin = {
                    "id": id_location_num,
                    }

                character_origin_copy = character_origin.copy()
                character_origin_id.append(character_origin_copy)
    
    #return (f"{character_origin} - {id_location_num} - {location_url} - {url_4} - {character_origin_id}") ---->  verificar variáveis

    return render_template("profile.html", profile=dict_profile, character_eps=character_episodes_infos, character_loc=character_location_id, character_ori=character_origin_id) # "profile.html" é o código html criado com o template a ser utilizado para os dados coletados, com informações de um personagem específico.


# Exercício 1: --------------------------------------------------------------------------------

# Criar uma nova rota para listar as localizações. A rota deverá ser acessível através do caminho /locations. A página deverá ser renderizada através do template locations.html. A página deverá conter uma tabela com as seguintes informações: nome, tipo e dimensão. A tabela deverá conter um link para a página de perfil da localização.

@app.route("/locations")
def get_locations_page():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict_locations = json.loads(data)

    return render_template("locations.html", locations=dict_locations["results"])


# Exercício 2: ----------------------------------------------------------------------------------

# Criar uma nova rota para listar os episódios. A rota deverá ser acessível através do caminho /episodes. A página deverá ser renderizada através do template episodes.html. A página deverá conter uma tabela com as seguintes informações: nome, data de lançamento e código. A tabela deverá conter um link para a página de perfil do episódio.

@app.route("/episodes")
def get_episodes_page():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict_episodes = json.loads(data)

    return render_template("episodes.html", episodes=dict_episodes["results"])


# Exercício 3: ----------------------------------------------------------------------------------

# Criar uma nova rota para exibir o perfil da localização. A rota deverá ser acessível através do caminho /location/<id>. A página deverá ser renderizada através do template location.html. A página deverá conter as seguintes informações: nome, tipo, dimensão e uma lista com os personagens que aparecem na localização. A lista deverá conter um link para a página de perfil do personagem.

@app.route("/location/<id>")
def get_location_page(id):
    global count_page, dict_location
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict_location = json.loads(data)

    count_page = 0
    page = f'{count_page}'

    url_2 = "https://rickandmortyapi.com/api/character/?page=" + page
    response_2 = urllib.request.urlopen(url_2)
    data_2 = response_2.read()
    dict_location_2 = json.loads(data_2)

    infos_residents_location = []
    
    for resident in dict_location["residents"]:
        character = resident
        id_resident = re.findall("\d+", character)
        id_resident_num = int("".join(id_resident))
      
        for item in dict_location_2["results"]:
            if id_resident_num == item["id"]:
                characters_location = {
                    "id": id_resident_num,
                    "name": item["name"],  
                    "image": item["image"]
                    }

                characters_location_copy = characters_location.copy()
                infos_residents_location.append(characters_location_copy)
              
                count_page = + 1
    
    #return (f"{character} {id_resident_num}  {characters_location} {url_2} {page} {infos_residents_location}") ---->  verificar variáveis

    return render_template("location.html", location=dict_location, residents=infos_residents_location)
    

# Exercício 4: ----------------------------------------------------------------------------------

# Criar uma nova rota para exibir o perfil do episódio. A rota deverá ser acessível através do caminho /episode/<id>. A página deverá ser renderizada através do template episode.html. A página deverá conter as seguintes informações: nome, data de lançamento, código e uma lista com os personagens que aparecem no episódio. A lista deverá conter um link para a página de perfil do personagem.

@app.route("/episode/<id>")
def get_episode_page(id):
    global count_page, dict_episode
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict_episode = json.loads(data)
    
    count_page = 0
    page = f'{count_page}'

    url_2 = "https://rickandmortyapi.com/api/character/?page=" + page
    response_2 = urllib.request.urlopen(url_2)
    data_2 = response_2.read()
    dict_episode_2 = json.loads(data_2)

    infos_characters_ep = []
    
    for character in dict_episode["characters"]:
        personagem = character
        id_character = re.findall("\d+", personagem)
        id_character_num = int("".join(id_character))
      
        for item in dict_episode_2["results"]:
            if id_character_num == item["id"]:
                characters_episode = {
                    "id": id_character_num,
                    "name": item["name"],  
                    "image": item["image"]
                    }

                characters_episode_copy = characters_episode.copy()
                infos_characters_ep.append(characters_episode_copy)
              
                count_page = + 1
    
    #return (f"{personagem} {id_character_num}  {characters_episode} {url_2} {page} {infos_characters_ep}") ---->  verificar variáveis

    return render_template("episode.html", episode=dict_episode, characters=infos_characters_ep)