def auto_repr(args, kwargs):
    def wrapper(cls):
        def __repr__(self):
            cls_args = [repr(self.__dict__[k]) for k in args]
            cls_kwargs = [f'{k}={self.__dict__[k]!r}' for k in kwargs]
            return f'{type(self).__name__}({", ".join(cls_args + cls_kwargs)})'

        cls.__repr__ = __repr__
        return cls

    return wrapper


# ======================
# Example usage
# ======================
@auto_repr(args=['x', 'y'], kwargs=['color'])
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

point = Point(1, 2, color='green')
print(point)

point.x = 10
point.y = 20
print(point)
