import subprocess
from datetime import datetime, timedelta


def generate_commits(commit_grid, year, repo_path, dummy_file):
    """
    Génère des commits pour remplir le graphe GitHub en fonction d'une grille de commits.
    :param commit_grid: Grille 7x49 de nombres de commits
    :param year: Année cible pour la contribution
    :param repo_path: Chemin vers le fichier txt a modifier dans un dépôt Git local
    :param dummy_file: Nom du fichier texte à modifier afin de créer les commits
    """
    start_date = datetime(year, 1, 1)
    while start_date.weekday() != 6:  # 6 = Dimanche
        start_date += timedelta(days=1)

    launch_commit(commit_grid, start_date, repo_path, dummy_file)


def launch_commit(commit_grid, start_date, repo_path, dummy_file):
    for week in range(49):
        for day in range(7):
            num_commits = commit_grid[day][week]
            commit_date = start_date + timedelta(weeks=week, days=day)

            for _ in range(num_commits):
                with open(f"{repo_path}/{dummy_file}", "a") as file:
                    file.write(f"Commit for {commit_date}\n")

                # Crée le commit avec la date correspondante
                subprocess.run(["git", "-C", repo_path, "add", dummy_file])
                subprocess.run([
                    "git", "-C", repo_path, "commit", "-m", "Automated commit",
                    "--date", commit_date.strftime("%Y-%m-%dT")
                ])

    # TODO add a security here :)

    subprocess.run(["git", "-C", repo_path, "push", "origin", "main"])
