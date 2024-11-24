def get_random_anime():
    while True:
        print("\nChoose what you want to experience:")
        show_items(anime_dict.keys())
        genre_choice = input("Pick the number of genre: ")
        genre_choice = integer_check(genre_choice, "Genre")
        if genre_choice is None:
            return
        if not (1 <= genre_choice <= len(anime_dict.keys())):
            print(f"Genre must be between 1 and {len(anime_dict.keys())}.")
            return
        genre_choice -= 1
        selected_genre = list(anime_dict.keys())[genre_choice]
        print("\nDo you want to watch a film or a series?")
        show_items(anime_dict[selected_genre].keys())
        type_choice = input("Select the number of preferable type: ")
        type_choice = integer_check(type_choice, "Type")
        if type_choice is None:
            return
        if not (1 <= type_choice <= len(anime_dict[selected_genre].keys())):
            print(f"Type must be between 1 and {len(anime_dict[selected_genre].keys())}.")
            return
        type_choice -= 1
        selected_type = list(anime_dict[selected_genre].keys())[type_choice]

        random_anime = _get_random_anime(selected_genre, selected_type)

        if random_anime:
            print(
                f"\nHere you go: {random_anime['title']}\nThe duration of watching: {random_anime['duration']}"
                f" minutes\nThe number of series: {random_anime['number']}")
        else:
            print("You've already seen all the animes from this list.")

        another = input("\nDo you want something else? (yes/no): ").strip().lower()
        if another != 'yes':
            return
