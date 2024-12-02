import pytest
import requests

#Executar Teste: pytest
#Executar Testes e obter também Respostas de rotas: pytest -s py-simulator/test_api_rickyMorty.py


BASE_URL = "https://rickandmortyapi.com/api"

@pytest.mark.parametrize("gender, expected_min_results", [
    ("male", 1),         # Testar gênero masculino
    ("female", 1),       # Testar gênero feminino
    ("unknown", 1)       # Testar gênero desconhecido
])
def test_filter_characters_by_gender(gender, expected_min_results):
    response = requests.get(f"{BASE_URL}/character/?gender={gender}")
    assert response.status_code == 200, f"Erro ao buscar personagens do gênero {gender}"
    data = response.json()
    assert "results" in data and len(data["results"]) >= expected_min_results, f"Esperado ao menos {expected_min_results} resultados para gênero {gender}"
    print(f"Personagens do gênero {gender} encontrados: {len(data['results'])} (Status: {response.status_code})\n")


@pytest.mark.parametrize("location_name", [
    "Earth (C-137)",  # Nome completo
    "Earth"           # Nome parcial
])
def test_search_location_by_name(location_name):
    response = requests.get(f"{BASE_URL}/location/?name={location_name}")
    assert response.status_code == 200, f"Erro ao buscar localização com nome {location_name}"
    data = response.json()
    assert "results" in data and len(data["results"]) > 0, f"Nenhuma localização encontrada com nome {location_name}"
    for location in data["results"]:
        assert location_name in location["name"], f"Nome incorreto retornado: {location['name']}"
    print(f"Localizações encontradas para '{location_name}': {len(data['results'])} (Status: {response.status_code})\n")


def test_total_episodes_count():
    response = requests.get(f"{BASE_URL}/episode")
    assert response.status_code == 200, "Erro ao buscar lista de episódios"
    data = response.json()
    assert "info" in data and "count" in data["info"], "Campo 'count' não encontrado na resposta"
    print(f"Total de episódios disponíveis: {data['info']['count']} (Status: {response.status_code})\n")



def test_invalid_endpoint():
    invalid_endpoint = f"{BASE_URL}/invalid_endpoint"
    response = requests.get(invalid_endpoint)
    assert response.status_code == 404, f"Esperado status 404 para endpoint inválido, recebido: {response.status_code}"
    print(f"Teste de endpoint inválido '{invalid_endpoint}' bem-sucedido (Status: {response.status_code})\n")


def test_episode_name_by_id():
    # Teste para verificar o nome de um episódio específico
    episode_id = 1
    response = requests.get(f"{BASE_URL}/episode/{episode_id}")
    assert response.status_code == 200, f"Erro ao buscar episódio com ID {episode_id}"
    data = response.json()
    assert data["name"] == "Pilot", f"Esperado: Pilot, Recebido: {data['name']}"
    print(f"Episódio com ID {episode_id}: {data['name']} (Status: {response.status_code})\n")



