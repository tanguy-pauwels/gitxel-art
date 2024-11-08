COLORS = {
    0: "#161B22",  # Noir (0 commit)
    1: "#0D4429",  # Vert 1 (1 commit)
    2: "#016D32",  # Vert 2 (2 commits)
    4: "#27A641",  # Vert 3 (4 commits)
    8: "#3AD353",  # Vert 4 (8 commits)
}
import matplotlib.pyplot as plt


def generate_graph(data):
    """
    Affiche une grille de contribution GitHub en fonction des niveaux de commits.
    :param data: Liste de listes représentant les niveaux de commits (0, 1, 2, 4, ou 8) pour chaque case.
    """
    rows, cols = len(data), len(data[0])

    fig, ax = plt.subplots(figsize=(15, 3))
    ax.set_aspect('equal')

    for row in range(rows):
        for col in range(cols):
            level = data[row][col]
            color = COLORS.get(level, "#ebedf0")
            rect = plt.Rectangle((col, rows - row - 1), 1, 1, color=color)
            ax.add_patch(rect)

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.axis('off')
    plt.show()
