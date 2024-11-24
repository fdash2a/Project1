def get_random_anime():
    global used_titles
    while True:
        print("\nChoose what you want to experience:")
        genre_choice = choose_item(anime_dict.keys(), "genre")
        if genre_choice is None:
            return
        selected_genre = list(anime_dict.keys())[genre_choice]
        print("\nDo you want to watch a film or a series?")
        type_choice = choose_item(anime_dict[selected_genre].keys(), "type")
        if type_choice is None:
            return
        selected_type = list(anime_dict[selected_genre].keys())[type_choice]

        random_anime = None
        if selected_genre in anime_dict and selected_type in anime_dict[selected_genre]:
            anime_list = anime_dict[selected_genre][selected_type]
            available_anime = [anime for anime in anime_list if anime["title"] not in used_titles]
            if available_anime:
                selected_anime = random.choice(available_anime)
                used_titles.add(selected_anime["title"])
                random_anime = selected_anime
        if random_anime is not None:
            print(
                f"\nHere you go: {random_anime['title']}\n" + "\n".join(anime_info(random_anime)))
        else:
            print("You've already seen all the animes from this list.")

        another = input("\nDo you want something else? (yes/no): ").strip().lower()
        if another != 'yes':
            return
