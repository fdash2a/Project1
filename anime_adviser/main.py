def main():
    # anime_dict = {
    #     "classics": [],
    #     "sport": [],
    #     "sad": [],
    #     "spooky": [],
    #     "visuals": [],
    #     "romance": []
    # }

    while True:
        print("\nこんにちは! What do you want to do?")
        print("1. Add your anime to the list")
        print("2. Show the current anime list")
        print("3. Get a random anime to watch from the list")
        print("4. Quit")

        choice = input("Select an action (1, 2, 3, 4): ")

        if choice == "1":
            add_anime()
        elif choice == "2":
            display_anime()
        elif choice == "3":
            get_random_anime()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Sorry, I don't follow you. Please try again.")
