import pandas as pd

df = pd.read_csv('./people.csv', sep=";")

print(df)

df = df.dropna(subset=['Salario Mensual'])
print(df)
df = df.dropna(subset=['Apellido'])
print(df)
""" df = df.drop_duplicates(['Departamento'])
print(df)
 """
#Indexar

mayores = df[df['Edad']>40]
print(mayores)

mayores = df[df['Edad']<40]
print(mayores[['Nombre','Salario Mensual']])

df['Salario Anual'] = df['Salario Mensual'] * 12
print(df)

ventas = df[df['Departamento']=='Ventas']
print(ventas)