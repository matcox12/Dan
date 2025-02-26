import pandas as pd
import numpy as np
student = 100
#создаем DataFrame с рандомными числами
data = np.random.randint(1, 100, student)
df = pd.DataFrame(data, columns=['reading score'])
print(df)

#находим ср.значение через сумму и кол.вл учеников
average_score = df['reading score'].sum() // student
print(f'среднее {average_score}')

#создаем новый df через булевую инексацию(то есть в качестве индекса(строки)
#передается true or false если true то строка записывается в новый df) через len находим кол-во учеников
results = len(df[df['reading score'] < average_score])
print(results)