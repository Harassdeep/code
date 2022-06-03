import pandas as pd
import numpy
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv('music.csv')

input_t = music_data.drop(columns = ['genre'])
output_t = music_data['genre']

model = DecisionTreeClassifier()
model.fit(input_t.values, output_t)

for i in range(100):
    x = input('Enter Age: ')
    y = input('Enter gender: ')

    z = input('do you want to ask for another set? ')

    predictions = model.predict([[x,y]])
    print(predictions)

    if z == "no":
        break



#predictions = model.predict([[21,1], [24,0]])

#print(predictions)
