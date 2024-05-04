import pandas as pd

df = pd.read_csv('./yarleanspuntocoom.csv')

#1
conteo_cargos = df[df['Cargo'].isin(['Chef', 'Mesero'])].groupby('Sede')['Cargo'].value_counts().unstack()

sede_requerida = conteo_cargos[(conteo_cargos['Chef'] == 3) & (conteo_cargos['Mesero'] == 5)].index.tolist()

print('La sede que tiene 3 chefs y 5 meseros es:')
print(sede_requerida)

#2
salarios_por_sede = df.groupby('Sede')['Salario'].sum().reset_index(name='Total de salarios')

print("\nTotal de salarios por sede:")
print(salarios_por_sede)

#3
promedio_salarios = df['Salario'].mean()
print("\nEl promedio de salarios es:", promedio_salarios)

#4
suma_total_salarios = df['Salario'].sum()
print("La suma total de salarios es:", suma_total_salarios)



#Punto de 4
""" 
Se puede hacer una tabla que registre el numero de personas que han muerto, la edad, la fecha de muerte, la razón de muerte, genero
y demas info extendida, con la intención de visibilizar cual es la razón de muertes comun y edades para poder tomar medidas y recomendaciones
a las personas para evitar esto

"""