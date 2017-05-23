from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        from random import randint
        num1 = randint(0, 9)
        num2 = randint(0, 9)
        num3 = randint(0, 9)

        result = solution([num1,num2,num3])

        self.assertEqual(result, num1+num2+num3)