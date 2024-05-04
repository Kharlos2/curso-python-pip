""" import matplotlib.pyplot as plt
import pandas as pd


def generate_chart():
    data = pd.read_csv('panes.csv')

    grouped_data = data.groupby('Pan mas vendido').sum()

    labels = grouped_data.index
    values = grouped_data['Cantidad vendida']

    plt.bar(labels, values)

    plt.title('Panes más vendidos en 50 panaderías de Medellín')
    plt.xlabel('Tipo de pan')
    plt.ylabel('Cantidad vendida')

    plt.savefig('panes_mas_vendidos.png')
    plt.close() """

import matplotlib.pyplot as plt
import pandas as pd

def generate_chart():
    data = pd.read_csv('panes.csv')

    # Renombrar la columna para eliminar espacios y mayúsculas
    data = data.rename(columns={'Pan Mas Vendido': 'Pan_mas_vendido'})

    grouped_data = data.groupby('Pan_mas_vendido').sum()

    labels = grouped_data.index
    values = grouped_data['Cantidad Vendida']  # Ajustar el nombre de la columna

    plt.bar(labels, values)

    plt.title('Panes más vendidos en 50 panaderías de Medellín')
    plt.xlabel('Tipo de pan')
    plt.ylabel('Cantidad vendida')

    plt.savefig('panes_mas_vendidos.png')
    plt.close()

# Esta parte sigue igual
def run():
    generate_chart()

if __name__ == '__main__':
    run()
