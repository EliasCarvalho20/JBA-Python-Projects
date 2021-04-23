def print_book_info(title, author=None, year=None):
    print(f'"{title}"', end="")
    if author or year:
        print(" was written", end="")
    if author:
        print(f" by {author}", end="")
    if year:
        print(f" in {year}")
