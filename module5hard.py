"""
Задание "Свой YouTube":
Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.

Подробное ТЗ:

Каждый объект класса User должен обладать следующими атрибутами и методами:
Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
 Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
Метод log_out для сброса текущего пользователя на None.
Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
Для метода watch_video так же учитывайте следующие особенности:
Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
После воспроизведения нужно выводить: "Конец видео"
"""
# Решение:
from time import sleep


class UrTube:
    def __init__(self):
        """
        Сервис видеохостинга
        """
        self.users = list()
        self.videos = list()
        self.current_user = None

    def log_in(self, login, password):
        """
        Метод пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного
        :param login: имя пользователя
        :param password: пароль
        """
        for user in self.users:
            if login == user.name and hash(password) == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        """
        Метод добавляет пользователя в список,
        если пользователя не существует (с таким же nickname).
        :param nickname: имя пользователя
        :param password: пароль
        :param age: возраст
        """
        for user in self.users:
            if nickname == user.name:
                print(f'Пользователь {nickname} уже существует')
                return
        self.current_user = User(nickname, hash(password), age)
        self.users.append(self.current_user)

    def log_out(self):
        """
        Метод сброса текущего пользователя на None
        """
        self.current_user = None

    def add(self, *videos):
        """
        Метод добавляет видео на сервис
        :param videos: неограниченное кол-во объектов класса Video
        """
        for video in videos:
            for video_ur in self.videos:
                if video.title == video_ur.title:
                    break
            else:
                self.videos.append(video)

    def get_videos(self, word: str) -> list:
        """
        Метод поиска видео на сервисе
        :param word: поисковое слово
        :return: список названий всех видео
        """
        word = word.lower()
        result = list()
        for video in self.videos:
            if word in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title: str):
        """
        Метод воспроизводит видео и ведёт отчёт в консоль на какой секунде ведётся просмотр
        :param title: заголовок
        """
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео"')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for time in range(video.duration):
                    sleep(1)
                    video.time_now = time + 1
                    print(video.time_now, end=' ')
                print('Конец видео')
                video.time_now = 0


class Video:

    def __init__(self, title: str, duration: int, adult_mode=False):
        """
        Видео сервиса
        :param title: заголовок
        :param duration: продолжительность, секунды
        :param adult_mode: ограничение по возрасту, bool
        """
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class User:

    def __init__(self, name: str, password: int, age: int):
        """
        Пользователь сервиса
        :param name: имя пользователя
        :param password: пароль в хэшированном виде
        :param age: возраст
        """
        self.name = name
        self.password = password
        self.age = age

    def __str__(self):
        return self.name


# Проверка:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')