import pandas as pd
import numpy
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv('music.csv')

t_input = music_data.drop(columns = ['genre'])
t_output = music_data['genre']

model = DecisionTreeClassifier()
model.fit(t_input.values, t_output)

#for i in range(100):
#    x = int(input('Enter Age: '))
#    y = int(input('Enter gender: '))
#
#    predictions = model.predict([[x,y]])
#    print(predictions)
#
#    z = input('do you want to ask for another set? ')
#
#    if z == "no":
#        break

R = int(input('No. of Entries you want: '))
C = 2

matrix = []


for j in range(R):
    a = []
    b = input('Enter age: ')
    a.append(b)
    d = input('Enter gender: ')
    a.append(d)
    matrix.append(a)

predictions = model.predict(matrix)
print(predictions)
