import sys
import os
import game


def read_file(filename: str):

    if os.path.exists(filename):

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as f:

            print(f.read())

    else:

        print(
            f"[{filename} missing]"
        )


def command_menu():

    while True:

        print("\n--- Command Menu ---")
        print("1. Sing")
        print("2. Cook")
        print("3. Dance")
        print("4. Return to Main Menu")

        command = input(
            "What do you want me to do? "
            "(1-4): "
        ).strip()

        if command == "1":

            print(
                "Ok, I will sing for you: "
                "La la la 🎵"
            )

        elif command == "2":

            print(
                "Ok, I will cook for you: "
                "szzsszzszszsssss..... "
                "Here comes your favorite meal!"
            )

        elif command == "3":

            print(
                "Ok, I will dance for you: "
                "dancing..."
            )

        elif command == "4":

            break

        else:

            print("Invalid option. Please choose 1-4.")


def main_menu():


    while True:

        print("\n=== Main Menu ===")
        print("1. Play Gold Rush Grid")
        print("2. View Instructions")
        print("3. Command Menu")
        print("4. Save Game")
        print("5. Exit Game")

        command = input(
            "Choose an option (1-5): "
        ).strip()

        if command == "1":

            game.play_grid_game()

        elif command == "2":

            read_file(
                "instructions.txt"
            )

        elif command == "3":

            command_menu()

        elif command == "4":

            game.save_game()

        elif command == "5":

            save_choice = input(
                "Do you want to save "
                "before exiting? (y/n): "
            ).strip().lower()

            if save_choice == "y":

                game.save_game()
                break

            elif save_choice == "n":

                print(f"Damn.. alright bud... Bye {game.player.name}!")
                break

            else:

                print("Invalid option. Choose (y/n)")

            

        else:

            print("Invalid option. Please choose 1-5.")


def main():

    # Existing save
    if os.path.exists(
        game.SAVE_FILE
    ):

        choice = input(
            "Found a saved game! "
            "Do you want to continue? "
            "(y/n): "
        ).strip().lower()

        if choice == "y":

            if game.load_game():

                main_menu()

                return

    # New player
    while True:

        name = input(
            "Enter your name: "
        ).strip()

        if name != "":
            break

        print(
            "Name cannot be empty."
        )

    # Age
    while True:

        try:

            age = int(
                input(
                    "Enter your age: "
                )
            )

            if age <= 0:

                print(
                    "Age must be greater than 0."
                )

                continue

            break

        except ValueError:

            print(
                "Please enter a valid integer."
            )

    # Age restriction
    if age < 12:

        print(
            "\nPlayers under 12 years old are not allowed to play."
        )

        print(
            "Exiting game... Goodbye!"
        )

        sys.exit()

    # Create player
    game.player = game.Player(
        name=name,
        age=age
    )

    print(
        f"\nWelcome {name}!"
    )

    main_menu()


if __name__ == "__main__":
    main()