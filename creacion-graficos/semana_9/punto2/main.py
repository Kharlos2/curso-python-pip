import pandas as pd

df = pd.read_csv('temperaturas.csv')

print(df.head())

print(df.columns)

#1
medias_temperaturas = df.mean()
print("Medias de temperaturas:")
print(medias_temperaturas)

#2
desviacion_temperaturas = df.std()
print("Desviaciones estándar de temperaturas:")
print(desviacion_temperaturas)

#3
filtro_temperatura_1 = df[df['Temperatura 1'] > 24]
print("Filtrado por Temperatura 1 mayor que 24 grados:")
print(filtro_temperatura_1)

#4
correlacion_temperaturas = df.corr()
print("Correlación entre temperaturas:")
print(correlacion_temperaturas)

#5
df['Media_temperaturas'] = df.mean(axis=1)
print("DataFrame con nueva columna de media de temperaturas:")
print(df)

#6
df_ordenado = df.sort_values(by='Temperatura 2', ascending=False)
print("DataFrame ordenado por Temperatura 2 de forma descendente:")
print(df_ordenado)

#7
df_ordenado.to_csv('temperaturas_ordenadas.csv', index=False)
print("DataFrame ordenado guardado en 'temperaturas_ordenadas.csv'.")

#8 temp maxima
temperatura_maxima_Temperatura1 = df['Temperatura 1'].max()
temperatura_maxima_Temperatura2 = df['Temperatura 2'].max()
temperatura_maxima_Temperatura3 = df['Temperatura 3'].max()

print(f"Temperatura máxima en Temperatura 1: {temperatura_maxima_Temperatura1} grados")
print(f"Temperatura máxima en Temperatura 2: {temperatura_maxima_Temperatura2} grados")
print(f"Temperatura máxima en Temperatura 3: {temperatura_maxima_Temperatura3} grados")

#9 Calcular la moda de cada columna de temperaturas
moda_Temperatura1 = df['Temperatura 1'].mode()
moda_Temperatura2 = df['Temperatura 2'].mode()
moda_Temperatura3 = df['Temperatura 3'].mode()

print(f"Moda en Temperatura 1: {moda_Temperatura1[0]} grados")
print(f"Moda en Temperatura 2: {moda_Temperatura2[0]} grados")
print(f"Moda en Temperatura 3: {moda_Temperatura3[0]} grados")

#10 
suma_acumulada = df.cumsum()

print("Suma acumulada por columna:")
print(suma_acumulada)