# Esse pequeno código tem o objetivo de simular um sistema de consulta a Pokedex Nacional
# trazendo informações relevantes para todos os pokemons disponiveis
import requests
import webbrowser
import time
from requests import api


def pokedex():
    print("###### Bem vindo ao Sistema da  Pokedex Nacional ######")
    p = input("Digite o nome ou ID do Pokemon ")
    api_url = "https://pokeapi.co/api/v2/pokemon/{}".format(p)
    r = requests.get(api_url)
    if r.status_code != 200:
        print("Pokemon não encontrado!")
    else:
        pokemon = r.json()
        print("Processando...")
        time.sleep(2)
        print("Pokemon encontrado:")
        print("ID: %d" % (pokemon['id']))
        print("Nome: %s" % (pokemon['name'].capitalize()))
        print("Tipo: %s" % (pokemon['types'][0]['type']['name']))
        print("Moves: %s, %s, %s, %s" % (pokemon['moves'][0]['move']['name'],
                                         pokemon['moves'][1]['move']['name'],
                                         pokemon['moves'][2]['move']['name'],
                                         pokemon['moves'][3]['move']['name'],))
        print("Menu de opções: ")
        print("1. Ver mais informações online")
        print("2. Procurar outro pokemon")
        print("3. Sair")
        m = int(input())
        if m == 1:
            url_db = "https://pokemondb.net/pokedex/{}".format(pokemon['name'])
            webbrowser.open(url_db, autoraise=True)
            pokedex()
        elif m == 2:
            pokedex()
        elif m == 3:
            exit()
        else:
            print("Opção Invalida ")
            pokedex()


pokedex()
