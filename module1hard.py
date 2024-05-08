#Входные данные:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Решение: 
students = sorted(list(students))
gpa = {}
gpa[students[0]] = sum(grades[0])/len(grades[0])
gpa[students[1]] = sum(grades[1])/len(grades[1]) 
gpa[students[2]] = sum(grades[2])/len(grades[2])
gpa[students[3]] = sum(grades[3])/len(grades[3])
gpa[students[4]] = sum(grades[4])/len(grades[4])
print ('Средние баллы учеников:')
print (gpa)

#В этой задаче рациональнее было бы использовать циклы, но эта тема еще не была изучена на уроках