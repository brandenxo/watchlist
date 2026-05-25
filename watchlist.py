def add_movie():
    pass

def remove_movie(watchlist):
    remove_movie = input("Which movie would you like to remove?")

    for movie in watchlist:
        if movie['title'] == remove_movie:
            print(f"Removing {movie['title']}...")
            del movie['title']
            del movie['watched']

def mark_watched():
    pass

def show_watchlist():
    pass


def main():
    movie = {}
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

        if option == 5:
            break


main()