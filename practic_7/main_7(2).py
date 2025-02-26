import pandas as pd
import random

def Rand_Completed(kol): #рандомно выставляет есть или нет
    a = []
    for i in range(kol):
        if random.randint(0,1) == 1:
            a.append('Completed')
        else:
            a.append('Uncompleted')
    return a


def Cryptographer(mean): # переставляет местами
    mean_len = len(mean)
    return mean[mean_len // 2 :] + mean[: mean_len // 2]

student = 10

#создаем df
data = {
    'test preparation course': Rand_Completed(student)
}
df = pd.DataFrame(data)
print(df)

#создаем новый столбец значение через apply (применять функцию ко всем элементам столбца) передаем лямбду и в ней вызываем шифровальщик
df['crypted'] = df['test preparation course'].apply(lambda x:Cryptographer(x))
print(df)
