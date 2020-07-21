import datetime
from datetime import timedelta
from json import JSONEncoder

import pandas as pd
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

column_names = [
    'From Date id (UTC)', 'till', 'day', 'temperature', 'quality', 'Time:', 'Unnamed: 5'
]
column_names_used = [
    'From Date Tid (UTC)', 'till', 'day'
]


def make_numeric_values(arr, title):
    new_arr = []
    for date in arr[title]:
        new_date = make_date(date)
        new_arr.append(new_date)
    arr[title] = new_arr


def fix_array(arr):
    for name in column_names_used:
        make_numeric_values(arr, name)


def make_date(date):
    new_date = date.split(' ')
    new_date = new_date[0]
    new_date = new_date.split('-')
    new_number = ''
    first = True
    for number in new_date:
        if first:
            first = False
        else:
            new_number = new_number + number
    return new_number


def convert_date_to_string(plus_days):
    date = datetime.datetime.today() + timedelta(days=plus_days)
    date = date.strftime("%Y-%m-%d %H:%M:%S")
    date = date.split(' ')
    date = date[0]
    date = date.split('-')
    date = date[1] + date[2]
    return date


# THIS IS WHERE THE MODEL GETS TRAINED
# if you want to use this in your own project this is the method you want to study

def train():
    data1 = pd.read_csv("p4.csv", sep=';', skiprows=3607, names=column_names)
    data2 = pd.read_csv("p3.csv", sep=';', skiprows=15, names=column_names)
    print(data1)

    data1 = data2.append(data1)
    data1 = data1.drop('Time:', axis=1)
    X = data1.drop(["temperature"], axis=1)
    X = X.drop(['quality'], axis=1)
    X = X.drop(['Unnamed: 5'], axis=1)
    fix_array(X)
    y = data1['temperature']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=3)
    tree_model = DecisionTreeRegressor()
    tree_model.fit(X_train, y_train)
    joblib.dump(tree_model, 'weather_predictor.pkl')
    print("-" * 48)
    print("\nDone training\n")
    print("-" * 48)


def predict_weather1(year, month, day, number_of_days):
    train()
    tree_model = joblib.load('weather_predictor.pkl')
    dtarr = []
    for x in range(number_of_days):
        day = day + x
        day1 = str(month) + str(day)
        date = [
            [day1,
             (str(int(day1) + 1)),
             day1]
        ]
        print(date)
        dtarr.append(date)

    predicted = []
    for x in range(number_of_days):
        print("--------------------------------")
        print(dtarr[x])
        temp = tree_model.predict(dtarr[x])
        print("\nThe temperature is estimated to be: " + str(temp) + "\n")
        strTemp = str(temp)
        strTemp = strTemp.replace('[','')
        strTemp = strTemp.replace(']','')
        retVal = ReturnValue(x, strTemp)        
        predicted.append(retVal)
    print(predicted)
    return predicted


class ReturnValue():
    temperature = ""
    day = ""

    def __init__(self, day, temp):
        # Instance Variable
        self.temperature = temp
        self.day = day


class RetValEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
