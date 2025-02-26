import pandas as pd
import numpy as np
student = 100

#создаем DataFrame(df) с рандомными числами
data = np.random.randint(1, 100, student)
df = pd.DataFrame(data, columns=['reading score'])
print(df)

#находим ср.значение через сумму и кол.вл учеников
average_score = df['reading score'].sum() // student
print(f'среднее {average_score}')


#df['reading score'] < average_score этой строкой мы создаем series в него входят все студенты в данных которых
#содерижтся True или False после мы сортируем наш изначальный df по новому series если true то значение проходит
#len выводит кол-во студентов которые прошли по True

results = len(df[df['reading score'] < average_score])
print(f'кол-во учеников с реултатом < среднего = {results}')


