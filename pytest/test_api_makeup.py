import pytest
import requests

# BASE URL da API de Makeup
BASE_URL = "https://makeup-api.herokuapp.com/api/v1/products"

def test_get_products_by_brand_and_category():
    # Testar a busca de produtos por marca e categoria combinados
    brand = "maybelline"
    category = "lipstick"
    response = requests.get(BASE_URL + f".json?brand={brand}&product_type={category}")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, f"Nenhum produto encontrado para a marca {brand} e categoria {category}"
    for product in data:
        assert product["brand"] == brand, f"Marca incorreta no produto: {product['brand']}"
        assert category in product["product_type"], f"Categoria incorreta no produto: {product['product_type']}"
    print(f"Produtos encontrados para a marca {brand} e categoria {category}: {len(data)}")


def test_no_products_found():
    # Testar uma busca sem resultados
    brand = "nonexistent_brand"
    response = requests.get(BASE_URL + f".json?brand={brand}")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) == 0, f"Produtos inesperados encontrados para a marca {brand}"
    print(f"Nenhum produto encontrado para a marca {brand} (conforme esperado).")


def test_response_structure():
    # Testar a estrutura de resposta de um produto
    response = requests.get(BASE_URL + ".json")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    # Verificar que pelo menos um produto possui os campos esperados
    assert len(data) > 0, "Nenhum produto encontrado"
    expected_fields = ["id", "brand", "name", "price", "product_type"]
    for field in expected_fields:
        assert field in data[0], f"Campo ausente na resposta: {field}"
    print(f"Estrutura da resposta verificada com sucesso. Campos presentes: {expected_fields}")


def test_missing_fields_in_product():
    # Testar se algum campo importante está ausente nos produtos retornados
    response = requests.get(BASE_URL + ".json")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum produto encontrado"
    
    # Verificar se os produtos possuem campos obrigatórios
    mandatory_fields = ["id", "brand", "name", "price", "product_type"]
    for product in data:
        missing_fields = [field for field in mandatory_fields if field not in product]
        assert not missing_fields, f"Produto com campos ausentes: {missing_fields}"
    print("Todos os produtos possuem os campos obrigatórios.")

