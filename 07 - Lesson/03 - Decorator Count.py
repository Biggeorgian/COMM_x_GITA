def counter(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(f"გამოძახება {count}")
        func()
    return wrapper

@counter
def say():
    print("Hi")

say()
say()
say()