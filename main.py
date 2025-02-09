from scripts.manipulate_repos import ManipulateRepos

if __name__ == "__main__":
    new_repo = ManipulateRepos('vitor-akira')

    name_repo = 'language_repository_companies'
    new_repo.create_repo(name_repo)

    new_repo.add_archives(name_repo, 'languages_amzn.csv', 'datas/languages_amzn.csv')
    new_repo.add_archives(name_repo, 'languages_netflix.csv', 'datas/languages_netflix.csv')
    new_repo.add_archives(name_repo, 'languages_spotify.csv', 'datas/languages_spotify.csv')
    new_repo.add_archives(name_repo, 'languages_apple.csv', 'datas/languages_apple.csv')
