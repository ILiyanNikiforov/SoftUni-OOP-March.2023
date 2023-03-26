class vowels:
    def __init__(self, text: str):
        self.text = text
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        list_of_vowels = ["a", "e", "i", "o", "u", "y"]

        while self.start < len(self.text):
            current = self.text[self.start]
            self.start += 1

            if current.lower() in list_of_vowels:
                return current
        raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
