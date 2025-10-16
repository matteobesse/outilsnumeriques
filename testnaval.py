import random

GRID_SIZE = 5
NUM_SHIPS = 3

def create_grid():
    return [["~"] * GRID_SIZE for _ in range(GRID_SIZE)]

def print_grid(grid, hide_ships=True):
    print("  " + " ".join(str(i) for i in range(GRID_SIZE)))
    for idx, row in enumerate(grid):
        display_row = []
        for cell in row:
            if hide_ships and cell == "S":
                display_row.append("~")
            else:
                display_row.append(cell)
        print(f"{idx} " + " ".join(display_row))

def place_ships(grid):
    ships = 0
    while ships < NUM_SHIPS:
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        if grid[x][y] == "~":
            grid[x][y] = "S"
            ships += 1

def get_move():
    while True:
        try:
            coords = input("Entrez les coordonnées (x y): ").split()
            if len(coords) != 2:
                raise ValueError
            x, y = map(int, coords)
            if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                return x, y
        except ValueError:
            pass
        print("Coordonnées invalides. Réessayez.")

def main():
    grid = create_grid()
    place_ships(grid)
    attempts = 0
    hits = 0

    print("Bienvenue à la bataille navale !")
    while hits < NUM_SHIPS:
        print_grid(grid)
        x, y = get_move()
        if grid[x][y] == "S":
            print("Touché !")
            grid[x][y] = "X"
            hits += 1
        elif grid[x][y] == "~":
            print("Manqué.")
            grid[x][y] = "O"
        else:
            print("Déjà essayé.")
        attempts += 1

    print("Félicitations, vous avez coulé tous les navires en", attempts, "coups !")
    print("Voici la grille finale :")
    print_grid(grid, hide_ships=False)

if __name__ == "__main__":
    main()