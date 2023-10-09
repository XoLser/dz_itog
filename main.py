#В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
#Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)

def lst_robot(data):
    mac = []
    for i in data['whoAmI']:
        if i == 'robot':
            mac.append(1)
        else:
            mac.append(0)
    return mac

def lst_human(data):
    mac = []
    for i in data['whoAmI']:
        if i == 'human':
            mac.append(1)
        else:
            mac.append(0)
    return mac

data_1 = {'human': lst_human(data), 'robot': lst_robot(data)}
df = pd.DataFrame(data_1)
print(df)
