# Requests Project

Este projeto foi desenvolvido para a obtenção de dados sobre as linguagens de programação utilizadas por grandes empresas, como Amazon, Spotify, Netflix e Apple. O objetivo do projeto é criar um pipeline ETL, que consiste nas etapas de extração, transformação e carga
## 📂 Estrutura do Projeto

```
requests-project/
├── scripts/                # Scripts Python
├── main.py                 # Arquivo principal para execução
└── 📄 requirements.txt     # Bibliotecas necessárias
```

## 🛠️ Configuração do Ambiente

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

### 2️⃣ Criar um ambiente virtual (WSL/Linux)
```bash
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

## 📝 Notas
Para usar a API do GitHub, você precisa de um token de acesso pessoal. Adicione o token ao código ou defina uma variável de ambiente:
```bash
export GITHUB_TOKEN='seu_token_aqui'  # Linux/Mac
set GITHUB_TOKEN=seu_token_aqui       # Windows
```
