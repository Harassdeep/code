import pandas as pd
from sklearn.tree import DecisionTreeClassifier

t = pd.read_csv('music.csv')

t_input = t.drop(columns = ['genre'])
t_output = t['genre']

model = DecisionTreeClassifier()
model.fit(t_input.values, t_output)

matrix = []

R = int(input('Enter no. of entries: '))
C = 2

for j in range(R):
    a = []
    b = input("Enter age: ")
    a.append(b)
    c = input("Enter gender: ")
    if c == "male":
        a.append(1)
    else:
        a.append(0)
    matrix.append(a)

predictions=model.predict(matrix)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print(predictions[i])
    print()
