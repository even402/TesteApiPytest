Teste de API com Pytest 🧪
Este repositório contém uma atividade acadêmica desenvolvida para a disciplina de testes, ministrada pelo professor Érico Borgonove, no 4º semestre, com o objetivo de explorar técnicas de automação de testes para APIs utilizando o framework Pytest.

📖 Descrição
O projeto apresenta exemplos práticos de como realizar testes automatizados em APIs RESTful utilizando o Pytest.
São abordados conceitos como:

Validação de status HTTP.
Teste de resposta do payload (corpo da resposta).
Testes parametrizados para múltiplos cenários.
Integração com APIs públicas e privadas.
🚀 Começando
Siga estas instruções para obter uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e testes.

📋 Pré-requisitos
Antes de executar os testes, certifique-se de que o ambiente atende aos seguintes requisitos:

Python 3.x: Linguagem de programação para desenvolvimento e execução dos testes.
pip: Gerenciador de pacotes do Python.
Pytest: Framework para escrita e execução dos testes.
Acesso às APIs necessárias, incluindo suas respectivas chaves de acesso, se aplicável.

🔧 Instalação
Clone o repositório:


git clone https://github.com/even402/TesteApiPytest.git

Instale as dependências:
pip install -r requirements.txt

📂 Estrutura do Projeto
O projeto está organizado da seguinte maneira:

TesteApiPytest/  
├── pytest/  
│   ├── test_api_game_of_thrones.py       # Testes para a API da série game of thrones
│   ├── test_api_makeup.py                # Testes para uma api de maquiagem
│   └── test_api_ricky_and_morty.py       # Testes para a api do ricky and morty 
│   └── test_api_stars_wars.py            # Testes para a api do stars wars 
├── selenium/  
│   ├── test_google.py         # Teste automatizado de busca no google 
├── .gitignore                 # Arquivo para ignorar arquivos desnecessários no Git  
├── requirements.txt           # Lista de dependências do projeto  
└── README.md                  # Documentação do projeto  


🔍 Detalhes dos Testes
📑 Testes Funcionais
Estes testes validam:

Códigos de status HTTP: Garantem que as respostas das APIs retornem os códigos esperados, como 200, 404 ou 500.
Conteúdo da resposta: Verifica se o corpo da resposta contém os dados esperados.
Validação de parâmetros: Testa endpoints com diferentes combinações de parâmetros.
⚙️ Testes de Integração
Simulam interações entre diferentes APIs ou serviços para garantir que os dados fluam corretamente entre eles.

✒️ Autores
Rosana Even - Desenvolvimento e Implementação - GitHub.

🎁 Agradecimentos 
Agradecimentos aaos meus colegas de sala que me inspiraram a buscar conhecimentos na área. 😊
⌨️ com ❤️ por Rosana Even.
