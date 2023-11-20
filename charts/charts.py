import matplotlib.pyplot as plt
def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [100, 200, 300]

    '''fig, ax = plt.subplots()
    ax.pie(values, labels= labels)
    plt.show()'''

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Grafico de Pastel')
    # plt.show()

    # Guardar la figura en un archivo en lugar de mostrarla
    plt.savefig('grafico_pastel.png')
    plt.close()
