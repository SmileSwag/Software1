from fileinput import filename
import random
import json
import os

SAVE_FILE = "save_game.json"
player = None
grid = None
difficulty_mode = ""

class Item:
    def __init__(self, item_type: str, points: int, position: list):
        self.item_type = item_type
        self.points = points
        self.position = position

    def to_dict(self):
        return {
            "item_type": self.item_type,
            "points": self.points,
            "position": self.position
        }

    def from_dict(cls, data):
        return cls(
            data["item_type"],
            data["points"],
            data["position"]
        )


class Room:
    def __init__(self, row: int, col: int, item: Item = None):
        self.row = row
        self.col = col
        #row 0, col 0 = A1
        self.name = f"{chr(65 + col)}{row + 1}"
        self.item = item


class Player:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.moves_left = 100
        self.gold_count = 0
        self.mine_count = 0
        self.position = [0, 0]

    def get_score(self) -> int:
        return (self.gold_count * 3) - self.mine_count

    def move(self, direction: str, grid_size: int) -> bool:
        r = self.position[0]
        c = self.position[1]

        if direction == "w" and r > 0:
            r -= 1
        elif direction == "s" and r < grid_size - 1:
            r += 1
        elif direction == "a" and c > 0:
            c -= 1
        elif direction == "d" and c < grid_size - 1:
            c += 1
        else:
            return False

        self.position = [r, c]
        self.moves_left -= 1
        return True


class Grid:
    def __init__(self, size: int = 5):
        self.size = size
        self.items = []

        self.rooms = [
            [
                Room(r, c)
                for c in range(size)
            ]
            for r in range(size)
        ]

    def get_room_by_pos(self, pos: list) -> Room:
        return self.rooms[pos[0]][pos[1]]

    def get_random_empty_pos(self, occupied_positions: list) -> list:
        while True:
            pos = [
                random.randint(0, self.size - 1),
                random.randint(0, self.size - 1)
            ]

            if pos not in occupied_positions:
                return pos

    def setup_items(self, num_mines: int, player_pos: list):
        self.items = []

        # Clear old items from rooms
        for row in self.rooms:
            for room in row:
                room.item = None

        occupied = [player_pos]

        # Add gold
        gold_pos = self.get_random_empty_pos(occupied)
        gold_item = Item("Gold", 3, gold_pos)
        self.items.append(gold_item)
        self.get_room_by_pos(gold_pos).item = gold_item
        occupied.append(gold_pos)

        # Add mines
        for _ in range(num_mines):
            mine_pos = self.get_random_empty_pos(occupied)

            mine_item = Item("Mine", -1, mine_pos)
            self.items.append(mine_item)
            self.get_room_by_pos(mine_pos).item = mine_item
            occupied.append(mine_pos)

    def display(self, player_pos: list):
        cols = "   ".join(
            [
                chr(65 + c)
                for c in range(self.size)
            ]
        )

        print(f"\n    {cols}")

        for r in range(self.size):
            row_str = f"{r + 1}  "

            for c in range(self.size):

                if [r, c] == player_pos:
                    row_str += "[P] "

                else:
                    row_str += "[.] "

            print(row_str)

    def is_mine_nearby(self, player_pos: list) -> bool:

        for item in self.items:

            if item.item_type == "Mine":

                row_diff = abs(player_pos[0] - item.position[0])

                col_diff = abs(player_pos[1] - item.position[1])

                if row_diff <= 1 and col_diff <= 1:
                    return True

        return False

    def get_gold_position(self) -> list:

        for item in self.items:

            if item.item_type == "Gold":
                return item.position

        return [0, 0]

    def relocate_item(self, item: Item, player_pos: list):

        # Remove item from old room
        self.get_room_by_pos(item.position).item = None
        occupied = [player_pos]

        for other_item in self.items:
            if other_item != item:
                occupied.append(other_item.position)

        # Generate new position
        item.position = self.get_random_empty_pos(occupied)

        # Add item to new room
        self.get_room_by_pos(item.position).item = item


def calculate_distance(pos1: list, pos2: list) -> int:
    return (
        abs(pos1[0] - pos2[0])
        +
        abs(pos1[1] - pos2[1])
    )


def setup_new_game():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "intro.txt")
    if os.path.exists(file_path):
        with open(file_path,"r",encoding="utf-8") as f:
            print(f.read())

    else:
        print(f"[intro.txt missing]")

    global player
    global grid
    global difficulty_mode

    if player is None:
        print("No player found.")
        return

    print("\n=== Difficulty ===")
    print("1. Easy")
    print("2. Hard")
    print("3. Impossible")

    while True:

        choice = input(
            "Choose difficulty (1-3): "
        ).strip()

        if choice == "1":
            difficulty_mode = "Easy"
            num_mines = 1
            break

        elif choice == "2":
            difficulty_mode = "Hard"
            num_mines = 3
            break

        elif choice == "3":
            difficulty_mode = "Impossible"
            num_mines = 5
            break

        else:
            print("Invalid choice.")

    grid_size = 5

    grid = Grid(grid_size)

    player.moves_left = 50
    player.gold_count = 0
    player.mine_count = 0

    player.position = [
        random.randint(0, grid_size - 1),
        random.randint(0, grid_size - 1)
    ]

    grid.setup_items(num_mines,player.position)

    starting_room = grid.get_room_by_pos(player.position)

    print("\nGame created!")
    print(f"Difficulty: {difficulty_mode}")
    print(f"Mines: {num_mines}")
    print(f"Starting room: {starting_room.name}")


def save_game():
    if player == None or grid == None:
        print("No active game to save.")
        return

    save_data = {
        "name": player.name,
        "age": player.age,
        "moves_left": player.moves_left,
        "gold_count": player.gold_count,
        "mine_count": player.mine_count,
        "player_pos": player.position,
        "grid_size": grid.size,

        "items": [
            item.to_dict()
            for item in grid.items
        ],

        "difficulty_mode": difficulty_mode
    }

    try:

        with open(SAVE_FILE,"w",encoding="utf-8") as f:
            json.dump(save_data,f,indent=4)
        print("\nGame saved successfully!")

    except Exception as e:
        print(f"\nError saving game: {e}")


def load_game() -> bool:
    global player
    global grid
    global difficulty_mode

    if not os.path.exists(SAVE_FILE):
        print("\nNo save file found.")
        return False

    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, SAVE_FILE)
        with open(file_path,"r",encoding="utf-8") as f:

            data = json.load(f)

        player = Player(name=data["name"],age=data["age"])

        player.moves_left = data["moves_left"]
        player.gold_count = data["gold_count"]
        player.mine_count = data["mine_count"]
        player.position = data["player_pos"]

        grid = Grid(size=data["grid_size"])

        grid.items = [
            Item.from_dict(item_dict)
            for item_dict in data["items"]
        ]

        # Reconnect items to rooms
        for item in grid.items:

            grid.get_room_by_pos(item.position).item = item

        difficulty_mode = data["difficulty_mode"]

        print(f"\nSave loaded! \nWelcome back, {player.name}!")
        return True

    except Exception as e:

        print(f"\nFailed to load save file: {e}")
        return False


def play_grid_game():
    global player
    global grid

    if player is None:
        print("No player found.")
        return

    # Only make a new grid when one does not exist
    if grid is None or not grid.items:
        setup_new_game()

    prev_distance = calculate_distance(player.position,grid.get_gold_position())

    while player.moves_left > 0 and not player.get_score() < 0:

        grid.display(player.position)
        current_room = grid.get_room_by_pos(player.position)

        print(f"\nLocation: Room "
            f"{current_room.name}")

        # Mine detector
        if grid.is_mine_nearby(player.position):

            print("METAL DETECTOR: BEEP! BEEP! Mine detected nearby!")

        else:

            print("METAL DETECTOR: Quiet...")

        # Gold radar
        gold_pos = grid.get_gold_position()

        current_distance = calculate_distance(player.position,gold_pos)

        if current_distance < prev_distance:
            print("GOLD RADAR: WARMER! (Getting closer)")
        elif current_distance > prev_distance:
            print("GOLD RADAR: COLDER! (Moving away)")
        else:
            print("GOLD RADAR: Neutral")

        prev_distance = current_distance

        # HUD
        print(f"\nMoves Left: {player.moves_left}/50")
        print(f"Gold: {player.gold_count}")
        print(f"Mines Hit: {player.mine_count}")
        print(f"Score: {player.get_score()}")

        cmd = input("\nEnter move (W/A/S/D) or [M] for Menu: ").strip().lower()

        if cmd == "m":
            break

        if not player.move(cmd,grid.size):
            print("Invalid move or wall collision! Try again.")
            continue

        # Check new room
        new_room = grid.get_room_by_pos(player.position)

        if new_room.item is not None:
            item = new_room.item
            if item.item_type == "Mine":
                player.mine_count += 1
                print(f"\nBOOM! You stepped on a landmine in Room {new_room.name}! \n -1 point")

                grid.relocate_item(item,player.position)

            elif item.item_type == "Gold":
                player.gold_count += 1
                print(f"\nGOLD FOUND in Room {new_room.name}! \n +3 points")

                grid.relocate_item(item,player.position)
                prev_distance = (
                    calculate_distance(
                        player.position,
                        grid.get_gold_position()
                    )
                )

    if player.moves_left == 0 or player.get_score() < 0:
        print("\nGAME OVER!")
        print(f"Final Score: {player.get_score()}")
        grid = None