from cgitb import reset

import data
import lab4
import unittest


# Write your test cases for each part below.
# Part 1
from lab4 import ListProcessor, are_in_positive_quadrant, manhattan_distance, distance_all


class TestListProcessor(unittest.TestCase):
    def test_first_element_1(self):
        input = [[1, 2], [3, 4]]
        processor = ListProcessor(input)
        result = processor.first_element()
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        input = [[1, 2, 3], [], [4, 5], [6], []]
        processor = ListProcessor(input)
        result = processor.first_element()
        expected = [1, 4, 6]
        self.assertEqual(expected, result)

    # Part 2
from lab4 import Point, x_coordinates # for some reason my tests wont work without this, is this normal? I had to look it up
class TestXCoord(unittest.TestCase):
    def test_x_coord(self):
        points = [Point(1, 2), Point(3, 4), Point(5, 6)]
        result = x_coordinates(points)
        expected = [1, 3, 5]
        self.assertEqual(result, expected)

    def test_x_coord_2(self):
        points = [Point(7, 9)]
        result = x_coordinates(points)
        expected = [7]
        self.assertEqual(result, expected)

    # Part 3
class TestPosQuad(unittest.TestCase):
    def test_first_quad(self):
        points = [Point(1, 2), Point(3, 4), Point(-1, 2), Point(5, -6)]
        result = are_in_positive_quadrant(points)
        expected = [points[0], points[1]] # Only (1, 2) and (3, 4) are in the first quadrant
        self.assertEqual(result, expected)

    def test_first_quad_2(self):
        points = [Point(-1, -2), Point(0,0), Point(-3, 4)]
        result = are_in_positive_quadrant(points)
        expected = [] # No points should be in the first quadrant
        self.assertEqual(result, expected)

    # Part 4
from lab4 import distance
class TestDist(unittest.TestCase):
    def test_distance(self):
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        result = distance(p1, p2)
        expected = 5.0
        self.assertEqual(result, expected)

    def test_distance_2(self):
        p1 = Point(3,5)
        p2 = Point(3,5)
        result = distance(p1, p2)
        expected = 0.0
        self.assertEqual(result, expected)

    # Part 5
class TestManDist(unittest.TestCase):
    def test_man_hat(self):
        p1 = Point(1, 2)
        p2 = Point(3,6)
        result = manhattan_distance(p1, p2)
        expected = 6.0
        self.assertEqual(result, expected)

    def test_man_hat_2(self):
        p1 = Point(7, 6)
        p2 = Point(2, 9)
        result = manhattan_distance(p1, p2)
        expected = 8.0
        self.assertEqual(result, expected)

    # Part 6
class TestAllDist(unittest.TestCase):
    def test_dist_all(self):
        points = [Point(4, 6), Point(1,1)]
        result = distance_all(points)
        expected = [10.0, 2.0]
        self.assertEqual(result, expected)

    def test_dist_all_2(self):
        points = [Point(9, 7)]
        result = distance_all(points)
        expected = [16]
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
