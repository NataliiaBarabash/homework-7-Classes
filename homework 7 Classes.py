import json


class JsonParser:

    def __init__(self, json_line):
        self.json_line = json_line
        pass

    def __enter__(self):
        return json.loads(self.json_line)

    def __exit__(self, var1, var2, var3):
        pass


with JsonParser('"hello world"') as res:
    assert res == "hello world"

with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
    assert res == {"hello": "world", "key": [1, 2, 3]}


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def contains(self, point):
        if point.x >= self.point1.x and point.y >= self.point1.y:
            return True
        else:
            return False


start_point = Point(1, 0)
end_point = Point(7, 3)

rect = Rectangle(start_point, end_point)
assert rect.contains(start_point)
assert not rect.contains(Point(-1, 3))
