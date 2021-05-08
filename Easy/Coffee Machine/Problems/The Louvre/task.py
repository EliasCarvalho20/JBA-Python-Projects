class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def to_string(self):
        return f'\"{self.title}\" by {self.artist} ({self.year}) hangs in the {self.museum}.'


new_paint = Painting(input(), input(), int(input()))
print(new_paint.to_string())
