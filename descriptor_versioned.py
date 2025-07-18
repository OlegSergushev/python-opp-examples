class Versioned:
    def __init__(self):
        self._history = {}

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if obj not in self._history:
            raise AttributeError('Атрибут не найден')
        version = self._history[obj][0]
        values = self._history[obj][1]
        return values[version]

    def __set__(self, obj, value):
        values = self._history.setdefault(obj, [-1, []])[1]
        values.append(value)

    def get_version(self, obj, n):
        values = self._history[obj][1]
        return values[n - 1]

    def set_version(self, obj, n):
        self._history[obj][0] = n - 1


# ======================
# Example usage
# ======================
class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)

Student.age.set_version(student, 1)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

Student.age.set_version(student, 2)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))
