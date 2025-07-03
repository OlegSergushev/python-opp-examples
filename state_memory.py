from copy import deepcopy


class Selfie:
    def __init__(self):
        self.states = []

    def save_state(self):
        # Сохраняем текущее состояние всех атрибутов в виде словаря
        current_state = deepcopy(self.__dict__) 
        self.states.append(current_state)

    def recover_state(self, index):
        # Восстанавливаем состояние из списка
        if 0 <= index < len(self.states):
            state = self.states[index]
            new_selfie = Selfie()
            new_selfie.__dict__.update(state)  # Восстанавливаем состояние
            return new_selfie
        return self  # Если индекс вне диапазона, возвращаем текущий экземпляр

    def n_states(self):
        # Возвращаем количество сохраненных состояний
        return len(self.states)

# ======================
# Example usage
# ======================
if __name__ == "__main__":
  def sum_a_b(a, b):
    return a + b


  def sub_a_b(a, b):
      return a - b


  def mul_a_d(a, b):
      return a * b


  def truediv_a_b(a, b):
      return a / b


  obj = Selfie()
  obj.sum_a_b = sum_a_b
  print(obj.sum_a_b(1, 2))
  obj.save_state()

  obj.sub_a_b = sub_a_b
  print(obj.sub_a_b(1, 2))
  obj.save_state()

  obj.mul_a_d = mul_a_d
  print(obj.mul_a_d(1, 2))
  obj.save_state()

  obj.truediv_a_b = truediv_a_b
  print(obj.truediv_a_b(1, 2))
  obj.save_state()

  print(obj.n_states())
  obj = obj.recover_state(1)

  print(obj.n_states())
