from random import randint


class Team:

    def __init__(self, name):
        self.name = name
        self.num = randint(4,6)
        self.score = 0
        self.time = 0

    def solve_tasks(self):
        # Сложная формула коллективного разума, которую наспех придумал и объяснять не буду =Р
        self.score = int(randint(30,40) / (1 - 1/self.num))
        self.time = randint (40, 60) * self.score


team1 = Team('Мастера кода')
team2 = Team('Волшебники данных')

# Использование `%`
print('В команде %s участников: %d !' % (team1.name, team1.num))
print('В команде %s участников: %d !' % (team2.name, team2.num))
print('Итого сегодня в командах участников : %d и %d !' % (team1.num, team2.num))
print()

team1.solve_tasks()
team2.solve_tasks()

# Использование `format()`:
print('Команда {} решила задач: {} !'.format(team1.name, team1.score))
print('{} решили задачи за {} с !'.format(team1.name, team1.time))
print('Команда {} решила задач: {} !'.format(team2.name, team2.score))
print('{} решили задачи за {} с !'.format(team2.name, team2.time))
print()

# Использование f-строк:
print(f'Команды решили {team1.score} и {team2.score} задач.')

if team1.score > team2.score or team1.score == team2.score and team1.time > team2.time:
    challenge_result = f'Победа команды {team1.name}!'
elif team1.score < team2.score or team1.score == team2.score and team1.time < team2.time:
    challenge_result = f'Победа команды {team2.name}!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: {challenge_result}')
print()

tasks_total = team1.score + team2.score
time_avg = (team1.time + team2.time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!')
