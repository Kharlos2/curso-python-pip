import pandas as pd

df = pd.read_csv('./ventas.csv')

print(df.head(5))

num_filas = df.shape[0]
num_columnas = df.shape[1]

print(f"El DataFrame tiene {num_filas} filas y {num_columnas} columnas.")

valores_nulos_por_columna = df.isnull().sum()

print("Cantidad de valores nulos por columna: ", df.isnull().sum())

print("La suma total de ventas", df['ventas'].sum())

df['fecha'] = pd.to_datetime(df['fecha'])

# Crear una nueva columna 'mes' que contenga el mes de cada fecha
df['mes'] = df['fecha'].dt.month

# Calcular el promedio de ventas por mes
promedio_ventas_por_mes = df.groupby('mes')['ventas'].mean()

print("Promedio de ventas por mes:")
print(promedio_ventas_por_mes)


producto_mas_vendido = df.groupby('producto')['ventas'].sum().idxmax()
cantidad_total_vendida = df.groupby('producto')['ventas'].sum().max()

print(f"El producto más vendido es '{producto_mas_vendido}' con una cantidad total vendida de {cantidad_total_vendida} unidades.")


df_electronica = df[df['categoria'] == 'Electronica']

print(df_electronica)

df_electronica.to_csv('Ventas_electronica.csv', index=False)
