def add_movie(watchlist):
    movie = {}

    title = input("Enter movie title: ")
    movie["title"] = title
    watchlist.append(movie)

    return watchlist

def remove_movie(watchlist):
    remove_movie = input("Which movie would you like to remove?")

    for movie in watchlist:
        if movie['title'] == remove_movie:
            print(f"Removing {movie['title']}...")
            del watchlist[movie]

def mark_watched():
    pass

def show_watchlist(watchlist):
    for movie in watchlist:
        for key, value in movie.items():
            print(f"{key}")
            print(f"{value}")

def main():
    watchlist = []

    while True:
        print(f"\n🎬 Our Watchlist")
        print(f"=================")

        print(f"1. Add a movie")
        print(f"2. Remove a movie")
        print(f"3. Mark as watched")
        print(f"4. Show watchlist")
        print(f"5. Quit")

        option = int(input("Select an option: "))

        if option == 1:
            watchlist = add_movie(watchlist)
        elif option == 2:
            remove_movie(watchlist)
        elif option == 3:
            mark_watched()
        elif option == 4:
            show_watchlist(watchlist)
        elif option == 5:
            break


main()