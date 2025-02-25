import pandas as pd

#параметр задающий по скольким первым (максимальным) игрокам мы считаем
player = 5

#считываем файл(важно чтобы файл лежал в том же каталоге что и исполнительный файл)
df = pd.read_csv('football11.csv')

#выделяем columns только те что нужны(для удобства)
df = df.loc[:, ['Name', 'Wage', 'Penalties', 'HeadingAccuracy']]

#берем зп первых 5 игроков с максимальным числом пенальти
wage_penalties = df.nlargest(player, ['Penalties']).sum()['Wage']

#берем зп первых 5 игроков имеющих максимальную точность удара головой
wage_headingaccuracy = df.nlargest(player, ['HeadingAccuracy']).sum()['Wage']

#вычесляем ср.зарплату
wage_penalties = wage_penalties / player
wage_headingaccuracy = wage_headingaccuracy / player

#выводим в какое кол-во раз округляя до 3-х знаков
print(f'В {wage_penalties / wage_headingaccuracy:.3f} раз средняя зарплата игроков '
      f'забивающих максимальночисло пенальти выше средней зарплаты игроков, '
      f'имеющих максимальную точность удара головой')

