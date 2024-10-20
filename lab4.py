import data
# Write your functions for each part in the space below.
class ListProcessor:
    def __init__(self, nested_list: list[list[int]]):
        self.nested_list = nested_list

    def first_element(self) -> list[int]:
        filtered_lists = [lst for lst in self.nested_list if lst] # Filter out empty lists first
        first_elements = [lst[0] for lst in filtered_lists]    # Extract the first element from each of the remaining lists
        return first_elements

# Part 2
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def x_coordinates(points: list['Point']) -> list[float]:
        return [point.x for point in points]  # Return a list containing the x-coordinate of each point in the input list

# Part 3
class Quad:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

def are_in_positive_quadrant(points: list[Point]) -> list[Point]:
    return [point for point in points if point.x > 0 and point.y > 0]  # Return points where both x and y coordinates are positive (in the first quadrant)

# Part 4
import math # Brings sqrt function
class Dist:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

def distance(point1: Point, point2: Point) -> float:
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) # Euclidean distance is sqrt((x2 - x1)^2 + (y2 - y1)^2)

# Part 5
#ive just realized i dont need to make a new class for each function b/c its all using pt 2's, is this bad?
#should i force a new class each time?
def manhattan_distance(point1: Point, point2: Point) -> float:
    return abs(point1.x - point2.x) + abs(point1.y - point2.y) #manhatten dist is |x1 - x2| + |y1 - y2|

# Part 6
def distance_all(points: list[Point]) -> list[float]:
    origin = Point(0,0)
    return [manhattan_distance(origin, point) for point in points] # gets distances from (0, 0) to each point

