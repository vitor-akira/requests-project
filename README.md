# Requests Project

Este projeto foi desenvolvido para a obtenção de dados sobre as linguagens de programação utilizadas por grandes empresas, como Amazon, Spotify, Netflix e Apple. O objetivo do projeto é criar um pipeline ETL, que consiste nas etapas de extração, transformação e carga
## 📂 Estrutura do Projeto

```
requests-project/
├── scripts/
│   ├── extracting_data.py  # Script para extração de dados dos repositórios
│   ├── manipulate_repos.py # Manipulação de repositórios (criação, upload de arquivos)
│   ├── repos_data.py       # 
├── main.py                 # Arquivo principal para execução
└── 📄 requirements.txt     # Bibliotecas necessárias
```

📌 Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o Python 3 instalado e configurar um ambiente virtual:

python3 -m venv venv
source venv/bin/activate  # Linux/Mac
o venv\Scripts\activate  # Windows
pip install -r requirements.txt

🔧 Como Usar

1️⃣ Configurar Credenciais da API do GitHub

Para usar a API do GitHub, você precisa de um token de acesso pessoal. Adicione o token ao código ou defina uma variável de ambiente:

export GITHUB_TOKEN='seu_token_aqui'  # Linux/Mac
set GITHUB_TOKEN=seu_token_aqui       # Windows

### 2️⃣ Criar um ambiente virtual (WSL/Linux)
```bash
sudo apt install python3.12-venv  # Caso o venv não esteja disponível
python3 -m venv venv
source venv/bin/activate  # Ativar o ambiente virtual
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Extrair Data
```bash
python3 -m scripts.extracting_data
```
