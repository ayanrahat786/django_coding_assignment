class Rectangle:
    def __init__(self, length:int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield {"length": self.length}
        yield {"wisth": self.width}


rectangle = Rectangle(5,110)

for dimension in rectangle:
    print(dimension)