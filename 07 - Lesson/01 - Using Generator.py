word = "CODE"

def wordbyword(word):
    for char in word:
        yield char

printer = wordbyword(word)

for _ in range(len(word)):
    print(next(printer))
