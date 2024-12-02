import pytest
import requests

# Base URL da API
BASE_URL = "https://www.anapioficeandfire.com/api"

@pytest.mark.parametrize("house_id, expected_name", [
    (1, "House Algood"),
    (2, "House Allyrion of Godsgrace"),
    (3, "House Amber")
])
def test_get_specific_house_parametrized(house_id, expected_name):
    # Testa a recuperação de casas específicas com diferentes IDs
    endpoint = f"/houses/{house_id}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["name"] == expected_name, f"Esperado: {expected_name}, Retornado: {data['name']}"
    print(f"Casa retornada ({house_id}): {data['name']}")

def test_get_books_with_pagination():
    # Testa a recuperação de livros com paginação
    endpoint = "/books"
    params = {"page": 1, "pageSize": 2}  # Limitar a quantidade de livros retornados
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) == 2, "Número incorreto de livros retornados"
    print(f"Livros retornados na página 1: {len(data)}")

def test_search_house_by_region():
    # Testa a busca de casas por região
    endpoint = "/houses"
    params = {"region": "The North"}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhuma casa encontrada na região"
    print(f"Casas encontradas na região 'The North': {len(data)}")

def test_get_characters_with_alias():
    # Testa a busca de personagens por alias
    endpoint = "/characters"
    params = {"alias": "The Daughter of the Dusk"}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum personagem encontrado com este alias"
    assert data[0]["aliases"][0] == "The Daughter of the Dusk", f"Alias incorreto: {data[0]['aliases'][0]}"
    print(f"Personagem encontrado com alias 'The Daughter of the Dusk': {data[0]['name']}")

def test_get_invalid_character():
    # Testa a tentativa de recuperar um personagem com um ID inválido
    invalid_character_id = 9999  # ID inexistente
    endpoint = f"/characters/{invalid_character_id}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 404, "Esperado status 404 para ID inexistente"
    print("Requisição de personagem inválido retornou 404 conforme esperado.")

def test_get_house_sworn_members():
    # Testa a recuperação dos membros de uma casa específica
    house_id = 1  # ID da primeira casa
    endpoint = f"/houses/{house_id}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    sworn_members = data.get("swornMembers", [])
    assert isinstance(sworn_members, list), "Lista de membros não retornada"
    print(f"Membros jurados da Casa {data['name']}: {len(sworn_members)}")
