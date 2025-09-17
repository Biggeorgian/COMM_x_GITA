from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int

    def info(self):
        return self.title

    def is_classic(self):
        if self.year < 1970:
            return "კლასიკა"
        else:
            return "თანამედროვე"

book1 = Book("დიუნი", "ფრენკ ჰერბერტი", 1965)
book2 = Book("დიუნის მესია", "ფრენკ ჰერბერტი", 1969)
book3 = Book("დიუნის შვილები", "ფრენკ ჰერბერტი", 1976)
book4 = Book("დიუნის ღმერთი-იმპერატორი", "ფრენკ ჰერბერტი", 1981)

print(f"{book1.info()} არის {book1.is_classic()}")
print(f"{book2.info()} არის {book2.is_classic()}")
print(f"{book3.info()} არის {book3.is_classic()}")
print(f"{book4.info()} არის {book4.is_classic()}")