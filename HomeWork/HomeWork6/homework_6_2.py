"""
Встанови пакет requests за допомогою pip.
Напиши скрипт, який завантажує сторінку з вказаного URL та зберігає її вміст у текстовий файл.
Додай обробку помилок на випадок, якщо сторінка недоступна.
"""
import requests
import json
import io

base_url = "https://pokeapi.co/api/v2/"

def get_pkmn_info(name) -> "json":
    """
    Function, that get pokemon info to txt file from url API
    :param name:
    :return:
    """
    url = f"{base_url}/pokemon/{name}"
    reseponse = requests.get(url)
    if reseponse.status_code == 200:
        pkmn_data = reseponse.json()
        save_response_data(str(pkmn_data))
        return pkmn_data
    else:
        print(f"Failed to retrieve data {reseponse.status_code}")

def save_response_data(response) -> None:
    try:
        file = open("json_response.txt", "w")
        file.write(str(response))
        file.close()
    except Exception as ex:
        print(f"URL data not saved!: {ex}")

pokemon_name = "typhlosion"
pkmn_info = get_pkmn_info(pokemon_name)

# if pkmn_info:
#     print(f"Name: {pkmn_info["name"].capitalize()}")
#     print(f"Id: {pkmn_info["id"]}")
#     print(f"Height: {pkmn_info["height"]}")
#     print(f"Weight: {pkmn_info["weight"]}")
