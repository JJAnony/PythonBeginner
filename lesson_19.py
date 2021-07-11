import requests


def request_address(zipcode):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(zipcode))
    return response.json()


def request_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    return response.json()


if __name__ == '__main__':
    address = request_address('01001000')
    print(address)

    pokemon = request_pokemon('pikachu')
    print(pokemon['sprites']['front_shiny'])
