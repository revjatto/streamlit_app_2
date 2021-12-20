class Box:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    #using encapsulation tom hide/protect my data
    def set_width(self, value):
        self.__width = value

    def get_width(self):
        return self.__width

    def set_height(self, value):
        self.__height = value

    def get_height(self):
        return self.__height

    def area(self):
        return self.__height * self.__width


ups = Box(3.7, 11)
ups.set_width(20)
print(f"UPS box area is: {ups.area()}")

fedx = Box(3.9, 9)
fedx.set_width(12)
print(f"Fedx box area is: {fedx.area()}")
