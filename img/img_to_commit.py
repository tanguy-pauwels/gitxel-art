from PIL import Image


def grayscale_to_commits(value):
    """
    Convertit une valeur de gris (0–255) en nombre de commits selon des seuils définis.
    :param value: Niveau de gris (0–255)
    :return: Nombre de commits (0, 1, 2, 4, ou 8)
    """
    if value <= 51: #Proche du noir
        return 8  # Vert foncé (8 commits)
    elif value <= 102:
        return 4  # Vert moyen (4 commits)
    elif value <= 153:
        return 2  # Vert clair (2 commits)
    elif value <= 204:
        return 1  # Vert très clair (1 commit)
    else:
        return 0  # Noir (0 commit)


def image_to_commit_grid(image_path):
    """
    Convertit une image en niveaux de gris en une grille de nombres de commits.
    :param image_path: Chemin de l'image en niveaux de gris
    :return: Grille de commits sous forme de liste de listes
    """
    img = Image.open(image_path).convert("L")  # 'L' pour niveaux de gris
    width, height = img.size

    if width > 49 or height > 7:
        raise ValueError("Image must be less than 7x49 pixels.")

    commit_grid = []

    for y in range(height):
        row = []
        for x in range(width):
            gray_value = img.getpixel((x, y))
            commits = grayscale_to_commits(gray_value)
            row.append(commits)
        commit_grid.append(row)

    return commit_grid

