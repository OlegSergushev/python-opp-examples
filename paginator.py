from itertools import islice


class Pagination:
    @staticmethod
    def _chunked(data, n, length):
        data = iter(data)
        for _ in range(length):
            yield islice(data, n)

    def __init__(self, data, pag):
        self.current_page = 1
        length = len(data) // pag
        self.total_pages = length + 1 * (length != 1)
        chunks = self._chunked(data, pag, self.total_pages)
        self._data = [list(next(chunks)) for _ in range(self.total_pages)]

    def get_visible_items(self):
        return self._data[self.current_page - 1]

    def prev_page(self):
        self.current_page = max(1, self.current_page - 1)
        return self

    def next_page(self):
        self.current_page = min(self.total_pages, self.current_page + 1)
        return self

    def go_to_page(self, n):
        self.current_page = max(1, min(self.total_pages, n))

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = self.total_pages


#TEST
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
pagination.next_page()
print(pagination.get_visible_items())

pagination.last_page()
print(pagination.get_visible_items())

pagination.first_page()
print(pagination.get_visible_items())
