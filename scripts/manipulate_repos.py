import requests
import base64
import os

class ManipulateRepos:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com/'
        self.access_token = os.getenv("GITHUB_TOKEN")  # Obtém o token da variável de ambiente

        if not self.access_token:
            raise ValueError("Erro: Token do GitHub não encontrado! Defina a variável de ambiente GITHUB_TOKEN.")

        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def create_repo(self, name_repo):
        data = {
            "name": name_repo,
            "description": "data from repositories of some companies",
            "private": False
        }

        response = requests.post(f"{self.api_base_url}/user/repos", 
                                 json=data, headers=self.headers)

        print(f'status_code criação do repositório: {response.status_code}')

    def add_archives(self, name_repo, name_archive, path_archive):
        with open(path_archive, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content).decode("utf-8")

        url = f"{self.api_base_url}/repos/{self.username}/{name_repo}/contents/{name_archive}"
        data = {
            "message": "Add a new archive",
            "content": encoded_content
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')