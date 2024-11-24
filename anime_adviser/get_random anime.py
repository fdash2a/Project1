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
