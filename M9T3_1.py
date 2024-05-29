class StartPosError(Exception):
    pass

class EvenNumbers:

    def __init__(self, start=0, end=1):
        if start >= end:
            message = 'Значение атрибута start должно быть всегда меньше значения атрибута end.'
            raise StartPosError(message)
        else:
            self.start = start
        self.end = end
        self.pos = None

    def __iter__(self):
        # Сбрасываю счетчик перед циклом
        self.pos = self.start - 2 if not self.start % 2 else self.start - 1
        return self

    def __next__(self):
        # Метод возвращает значения по требованию перебора
        self.pos += 2
        if self.pos >= self.end:
            raise StopIteration
        return self.pos


# Проверка
en = EvenNumbers(10, 25)
for i in en:
    print(i)

en_1 = EvenNumbers(100, 25)
for i in en_1:
    print(i)