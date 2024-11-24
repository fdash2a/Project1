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
