import unittest
import requests

def fetch_todos() -> list:
    url = "https://jsonplaceholder.typicode.com/todos"
    response_data = requests.get(url)
    response_data.raise_for_status()
    return response_data.json()

def get_todo_title(todo_item: dict) -> str:
    if "title" in todo_item:
        return todo_item["title"]
    else:
        raise ValueError("მიღებულ ობიექტში 'title' ველი არ მოიძებნა.")

def get_todo_description(todo_item: dict) -> str:
    if "description" in todo_item:
        return todo_item["description"]
    else:
        raise ValueError("მიღებულ ობიექტში 'description' ველი არ მოიძებნა.")

class TestResponse(unittest.TestCase):
    all_todos = None
    first_todo = None

    @classmethod
    def setUpClass(cls):
        cls.all_todos = fetch_todos()
        if cls.all_todos:
            cls.first_todo = cls.all_todos[0]

    def test_response_title(self):
        # შეცდომაზე გავა ვინაიდან Title არსებობს
        if self.first_todo:
            self.assertIn("title", self.first_todo,
                          "ველი 'title' არ უნდა არსებობდეს, მაგრამ მოიძებნა.")

    def test_response_description(self):
        # შეცდომაზე გავა ვინაიდან Description არ არსებობს
        if self.first_todo:
            self.assertNotIn("description", self.first_todo,
                             "ველი 'description' უნდა არსებობდეს, მაგრამ არ მოიძებნა.")

# ვნახე რომ ამაზე იყო რეკომენდაცია, მაგრამ ბოლომდე ვერ მივხვდი რატომ?
if __name__ == '__main__':
    unittest.main()