from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.__init_photos(pages)

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.MAX_PHOTOS_PAGE)
        return cls(pages)

    def __init_photos(self, pages: int):
        matrix = [[] for _ in range(pages)]
        return matrix

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.MAX_PHOTOS_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page" \
                       f" {index + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        result = []
        separator = "-" * 11
        for page in self.photos:
            result.append(separator)
            result.append(' '.join('[]' for _ in page))
        result.append(separator)

        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
