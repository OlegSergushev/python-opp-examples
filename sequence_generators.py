from abc import ABC, abstractmethod


class Progression(ABC):
    def __init__(self, start, step):
        self._current = start
        self._step = step

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass


class ArithmeticProgression(Progression):
    def __next__(self):
        answer = self._current
        self._current += self._step
        return answer


class GeometricProgression(Progression):
    def __next__(self):
        answer = self._current
        self._current *= self._step
        return answer


# ======================
# Example usage
# ======================
if __name__ == "__main__":
    progression = ArithmeticProgression(100, -10)
    count = 0

    for item in progression:
        if count == 20:
            break
        count += 1
        print(item, end=' ')

    print()
    
    progression = GeometricProgression(100, 10)
    count = 0

    for item in progression:
        if count == 20:
            break
        count += 1
        print(item, end=' ')
