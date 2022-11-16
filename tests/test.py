import unittest
from src.first import result_get, new, incomes

class TestAnswer(unittest.TestCase):

    def test_answer(self):
        word = 'iamritik'
        result = result_get(word)
        ans = {'i': 3, 'a': 1, 'm': 1, 'r': 1, 't': 1, 'k': 1}

        self.assertEqual(result, ans)

    def test_new(self):
        result = new(incomes)
        ans = {'Books': 3970.0, 'Tutorials': 1940.0, 'Courses': 7680.0}
        self.assertEqual(result, ans)

if __name__ == "__main__":
    unittest.main()