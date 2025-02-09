import requests
import pandas as pd
import os
from math import ceil

class DataRepos:
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com/'
        self.access_token = os.getenv("GITHUB_TOKEN")  # Obtém o token da variável de ambiente

        if not self.access_token:
            raise ValueError("Erro: Token do GitHub não encontrado! Defina a variável de ambiente GITHUB_TOKEN.")

        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def repos_lists(self):
        repos_list = []
        response = requests.get(f'https://api.github.com/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30)

        for page_num in range(1, num_pages + 1):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        return repos_list

    def repos_names(self, repos_list):
        repo_names = []
        for page in repos_list:
            for repo in page:
                try: 
                    repo_names.append(repo.get('name', ''))
                except:
                    pass
        return repo_names

    def languages_names(self, repos_list):
        repo_languages = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo.get('language', ''))
                except:
                    pass
        return repo_languages

    def create_df_languages(self):
        repos = self.repos_lists()
        names = self.repos_names(repos)
        languages = self.languages_names(repos)

        datas = pd.DataFrame({
            'repository_name': names,
            'language': languages
        })

        return datas