maze = [
    ["S", ".", "#", ".", "."],
    ["#", ".", "#", ".", "#"],
    [".", ".", ".", ".", "."],
    ["#", "#", "#", ".", "#"],
    [".", ".", ".", ".", "E"]
]

class Maze:
    def __init__(self, layout):
        self.layout = layout
        self.height = len(self.layout)
        self.width = len(self.layout[0])
        self.visited = {(0, 0)}

    def get_move_status(self, x, y):
        if not (0 <= y < self.height and 0 <= x < self.width):
            return "Boundary"

        tile = self.layout[y][x]
        if tile == '#': return "mine"
        elif tile == 'E': return "win"
        else: return "move"

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, maze):
        next_x, next_y = self.x, self.y
        if   direction == 'w': next_y -= 1
        elif direction == 's': next_y += 1
        elif direction == 'a': next_x -= 1
        elif direction == 'd': next_x += 1

        status = maze.get_move_status(next_x, next_y)
        if status in ["move", "win"]:
            self.x, self.y = next_x, next_y
        return status

def display_maze(maze, player):
    for y in range(maze.height):
        row_to_print = []
        for x in range(maze.width):
            if (x, y) in maze.visited:
                row_to_print.append(maze.layout[y][x])
            else:
                row_to_print.append("░")
        if y == player.y:
            row_to_print[player.x] = "☺"
        print(" ".join(row_to_print))

def game():
    labyrinth = Maze(maze)
    theseus = Player(0, 0)

    print("თქვენ აღმოჩნდით დანაღმულ ლაბირინთში! იპოვეთ გამოსასვლელი (E).")

    while True:
        display_maze(labyrinth, theseus)
        direction = input("მიმართულება (w/a/s/d) | გასვლა (exit): ").lower()

        if direction == 'exit':
            print("ნახვამდის!")
            break

        if direction in ["w", "a", "s", "d"]:
            move_status = theseus.move(direction, labyrinth)

            if move_status in ["move", "win"]:
                labyrinth.visited.add((theseus.x, theseus.y))

            if move_status == "boundary":
                print("⛔️ თქვენ ლაბირინთის კიდეს ეჯახებით.")

            elif move_status == "mine":
                print("\n💥 თქვენ დანაღმულ კედელს დაეჯახეთ! "
                      "დავიწყოთ თავიდან.")
                game()

            elif move_status == "win":
                display_maze(labyrinth, theseus)
                print("\n🎉 გილოცავთ, თქვენ იპოვეთ გამოსასვლელი!")
                break
        else:
            print("⚠️ არასწორი ბრძანება.")
game()