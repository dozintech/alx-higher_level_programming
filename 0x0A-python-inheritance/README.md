# Inheritance

This project contains some tasks for learning about inheritance in **Python**.

## Tasks To Complete

+ [x] 0\. Lookup <br/>_**[0-lookup.py](0-lookup.py)**_ contains a function that returns the list of available attributes and methods of an object.
+ [x] 1\. My list <br/>_**[1-my_list.py](1-my_list.py)**_ contains a class `MyList` that inherits from `list`.
  + Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort).
+ [x] 2\. Exact same object <br/>_**[2-is_same_class.py](2-is_same_class.py)**_ contains a function that returns `True` if the object is *exactly* an instance of the specified class; otherwise `False`.
+ [x] 3\. Same class or inherit from <br/>_**[3-is_kind_of_class.py](3-is_kind_of_class.py)**_ contains a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.
+ [x] 4\. Only sub class of <br/>_**[4-inherits_from.py](4-inherits_from.py)**_ contains a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.
+ [x] 5\. Geometry module <br/>_**[5-base_geometry.py](5-base_geometry.py)**_ contains an empty class `BaseGeometry`.
+ [x] 6\. Improve Geometry <br/>_**[6-base_geometry.py](6-base_geometry.py)**_ contains a class `BaseGeometry` (based on [5-base_geometry.py](5-base_geometry.py)).
  + Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`.
+ [x] 7\. Integer validator <br/>_**[7-base_geometry.py](7-base_geometry.py)**_ contains a class BaseGeometry (based on [6-base_geometry.py](6-base_geometry.py)).
  + Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`.
  + Public instance method: `def integer_validator(self, name, value):` that validates `value`.
+ [x] 8\. Rectangle <br/>_**[8-rectangle.py](8-rectangle.py)**_ contains a class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](7-base_geometry.py)).
  + Instantiation with `width` and `height`: `def __init__(self, width, height):`.
+ [x] 9\. Full rectangle <br/>_**[9-rectangle.py](9-rectangle.py)**_ contains a class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](7-base_geometry.py)). (task based on [8-rectangle.py](8-rectangle.py)).
  + Instantiation with `width` and `height`: `def __init__(self, width, height):`.
  + the `area()` method must be implemented.
  + `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`.
+ [x] 10\. Square #1 <br/>_**[10-square.py](10-square.py)**_ contains a class `Square` that inherits from `Rectangle` ([9-rectangle.py](9-rectangle.py)).
  + Instantiation with `size`: `def __init__(self, size):`.
  + the `area()` method must be implemented.
+ [x] 11\. Square #2 <br/>_**[11-square.py](11-square.py)**_ contains a class `Square` that inherits from `Rectangle` ([9-rectangle.py](9-rectangle.py)).
  + Instantiation with `size`: `def __init__(self, size):`.
  + the `area()` method must be implemented.
  + `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`.
+ [x] 12\. My integer <br/>_**[100-my_int.py](100-my_int.py)**_ contains a class `MyInt` that inherits from `int` and switches the `==` and `!=` operators.
+ [x] 13\. Can I? <br/>_**[101-add_attribute.py](101-add_attribute.py)**_ contains a function that adds a new attribute to an object if it’s possible.
