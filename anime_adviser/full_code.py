import random

# Словарь с аниме по жанрам и типам, включая время просмотра в минутах
anime_dict = {
    "classics": {
        "film": [
            {"title": "Grave of the Fireflies", "duration": 89, "number": 1},
            {"title": "Spirited Away", "duration": 119, "number": 1},
            {"title": "Your Name", "duration": 106, "number": 1},
            {"title": "Howl's Moving Castle", "duration": 119, "number": 1},
            {"title": "Kiki's Delivery Service", "duration": 103, "number": 1},
            {"title": "My Neighbor Totoro", "duration": 86, "number": 1},
            {"title": "Suzume", "duration": 122, "number": 1},
        ],
        "series": [
            {"title": "Naruto", "duration": 24, "number": 720},
            {"title": "Dragon Ball Z", "duration": 26, "number": 141},
            {"title": "My Hero Academy", "duration": 24, "number": 120},
            {"title": "Hunter x Hunter", "duration": 25, "number": 148},
            {"title": "Demon Slayer", "duration": 23, "number": 48},
            {"title": "Evangelion", "duration": 25, "number": 26},
            {"title": "One Piece", "duration": 24, "number": 1116},
            {"title": "Mob Psycho 100", "duration": 25, "number": 38},
            {"title": "Bleach", "duration": 24, "number": 392},
            {"title": "Vinland Saga", "duration": 25, "number": 48},
        ],
    },

    "sport": {
        "film": [
            {"title": "Haikyuu!! The Movie: Aakeru no Kyuujitsu", "duration": 60, "number": 1},
            {"title": "Kuroko's Basketball: Last Game", "duration": 90, "number": 1},
            {"title": "Ping Pong the Animation: The Movie", "duration": 120, "number": 1},
        ],
        "series": [
            {"title": "Haikyuu!!", "duration": 24, "number": 85},
            {"title": "Kuroko no Basket", "duration": 24, "number": 75},
            {"title": "Free!", "duration": 25, "number": 12},
            {"title": "Yuri!!! on Ice", "duration": 25, "number": 12},
            {"title": "Ace of Diamond", "duration": 25, "number": 183},
            {"title": "Re-Main", "duration": 23, "number": 12},
            {"title": "Weakling Pedal", "duration": 24, "number": 113},
            {"title": "The Prince of Tennis", "duration": 22, "number": 178},
            {"title": "Blue Lock", "duration": 24, "number": 24},
            {"title": "Love All Play", "duration": 23, "number": 16},
            {"title": "SK∞", "duration": 24, "number": 12},
        ],
    },

    "sad": {
        "film": [
            {"title": "Grave of the Fireflies", "duration": 89, "number": 1},
            {"title": "I Want to Eat Your Pancreas", "duration": 108, "number": 1},
            {"title": "The Wind Rises", "duration": 126, "number": 1},
            {"title": "A Silent Voice", "duration": 130, "number": 1},
            {"title": "Ride Your Wave", "duration": 95, "number": 1},
            {"title": "Your Name", "duration": 106, "number": 1},
            {"title": "Words Bubble Up Like Soda Pop", "duration": 90, "number": 1},
            {"title": "Her Blue Sky", "duration": 108, "number": 1},
        ],
        "series": [
            {"title": "Your Lie in April", "duration": 25, "number": 22},
            {"title": "Violet Evergarden", "duration": 24, "number": 13},
            {"title": "Orange", "duration": 24, "number": 13},
            {"title": "Rainbow: Nisha Rokubou no Shichinin", "duration": 23, "number": 26},
            {"title": "To Your Eternity", "duration": 25, "number": 40},
            {"title": "Death Parade", "duration": 24, "number": 12},
            {"title": "Bokurano", "duration": 25, "number": 24},
        ],
    },

    "spooky": {
        "film": [
            {"title": "Vampire Hunter D: Bloodlust", "duration": 103, "number": 1},
            {"title": "Vampire Hunter D: Bloodlust", "duration": 90, "number": 1},
            {"title": "Perfect Blue", "duration": 81, "number": 1},
            {"title": "Gyo", "duration": 70, "number": 1},
            {"title": "Kakurenbo", "duration": 25, "number": 1},
        ],
        "series": [
            {"title": "Death Note", "duration": 24, "number": 37},
            {"title": "Hellsing", "duration": 24, "number": 13},
            {"title": "Soul Eater", "duration": 24, "number": 51},
            {"title": "Shiki", "duration": 25, "number": 22},
            {"title": "Highschool of the Dead", "duration": 23, "number": 12},
            {"title": "Berserk", "duration": 25, "number": 25},
            {"title": "Black Butler", "duration": 24, "number": 46},
            {"title": "Another", "duration": 25, "number": 12},
            {"title": "Jujutsu kaizen", "duration": 24, "number": 47},
            {"title": "Death Parade", "duration": 24, "number": 12},
        ],
    },

    "visuals": {
        "film": [
            {"title": "Spirited Away", "duration": 119, "number": 1},
            {"title": "Your Name", "duration": 106, "number": 1},
            {"title": "Howl's Moving Castle", "duration": 119, "number": 1},
            {"title": "Kiki's Delivery Service", "duration": 103, "number": 1},
            {"title": "Words Bubble Up Like Soda Pop", "duration": 90, "number": 1},
            {"title": "Beyond the Clouds, the Promised Place", "duration": 91, "number": 1},
            {"title": "Children Who Chase Lost Voices", "duration": 116, "number": 1},
        ],
        "series": [
            {"title": "Jujutsu kaizen", "duration": 24, "number": 47},
            {"title": "Fire Force", "duration": 25, "number": 48},
            {"title": "Violet Evergarden", "duration": 24, "number": 13},
            {"title": "Death Parade", "duration": 24, "number": 12},
            {"title": "Sword Art Online", "duration": 24, "number": 25},
            {"title": "No Game, No Life", "duration": 24, "number": 12},
        ],
    },

    "romance": {
        "film": [
            {"title": "The Wind Rises", "duration": 126, "number": 1},
            {"title": "Weathering with You", "duration": 112, "number": 1},
            {"title": "Your Name", "duration": 106, "number": 1},
            {"title": "A Silent Voice", "duration": 130, "number": 1},
            {"title": "The Garden of Words", "duration": 46, "number": 1},
            {"title": "The Light of a Firefly Forest", "duration": 45, "number": 1},
            {"title": "I Want to Eat Your Pancreas", "duration": 108, "number": 1},
            {"title": "Ride Your Wave", "duration": 95, "number": 1},
        ],
        "series": [
            {"title": "Toradora!", "duration": 25, "number": 25},
            {"title": "Your Lie in April", "duration": 25, "number": 22},
            {"title": "Spice and Wolf", "duration": 24, "number": 24},
            {"title": "My Love Story!!", "duration": 24, "number": 24},
            {"title": "Snow White with the Red Hair", "duration": 23, "number": 24},
            {"title": "Blue Spring Ride", "duration": 25, "number": 12},
            {"title": "Horimiya ", "duration": 24, "number": 13},
            {"title": "Wotakoi: Love Is Hard for Otaku", "duration": 24, "number": 12},
        ],
    },
}

used_titles = set()  # Множество для хранения уже выпавших ранее названий


def _get_random_anime(genre, anime_type):
    global used_titles
    if genre in anime_dict and anime_type in anime_dict[genre]:
        anime_list = anime_dict[genre][anime_type]
        available_anime = [anime for anime in anime_list if anime["title"] not in used_titles]
        if available_anime:
            selected_anime = random.choice(available_anime)
            used_titles.add(selected_anime["title"])
            return selected_anime
    return


def show_items(sequence):
    for idx, element in enumerate(sequence, 1):
        print(f"{idx}. {element}")

# проверка, что ввели натуральное число
def integer_check(string_number, name):
    try:
        number = int(string_number)
        if number <= 0:
            raise ValueError
    except ValueError:
        print(f"{name} must be positive integer number.")
        return
    return number


def add_anime():
    global anime_dict
    print("\nAvailable categories:")
    show_items(anime_dict.keys())
    category_index = input("Choose the category: ")
    category_index = integer_check(category_index, "Category")
    if category_index is None:
        return
    if not (1 <= category_index <= len(anime_dict.keys())):
        print(f"Category must be between 1 and {len(anime_dict.keys())}.")
        return
    category_index -= 1
    category = list(anime_dict.keys())[category_index]
    title = input("Type the anime's name: ")
    duration = input("Type the duration of one seria (in minutes): ")
    duration = integer_check(duration, "Duration")
    if duration is None:
        return
    episodes = input("Type the number of series: ")
    episodes = integer_check(episodes, "Number of series")
    if episodes is None:
        return
    # Проверка на дубликаты
    for anime_type in anime_dict[category]:
        for anime in anime_dict[category][anime_type]:
            if anime["title"] == title:
                print(f"The anime '{title}' already exists in category '{category}'.")
                return

    # Добавляем новую запись в соответствующую категорию
    anime_dict[category]["film" if episodes == 1 else "series"].append({"title": title,
                                                                        "duration": duration,
                                                                        "number": episodes})
    print(f"The anime '{title}' has been successfully added to category '{category}'!")


def print_nested_list(anime_dict):
    for i, sublist in enumerate(anime_dict):
        print(f"{i + 1}:")
        for item in sublist:
            print(f"- {item}")
            print()


def display_anime():
    my_list = [
        ["Элемент 1", "Элемент 2", "Элемент 3"],
        ["Элемент 4", "Элемент 5"],
        ["Элемент 6", "Элемент 7", "Элемент 8", "Элемент 9"]
    ]
    print_nested_list(my_list)


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


if __name__ == "__main__":
    main()
