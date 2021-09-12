import numpy as np

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

from tkinter import Button, Label, Tk, mainloop, filedialog



main = Tk()
main.title("Spectra")
main.geometry("800x600")
main.resizable(1, 1)

def run():

    # my_btn = Button(main, text="Open Spectra", command=pre_calculate()).pack()
    # global pan
    # global qdots
    # global complex
    # global solvent
    # pan = _open()
    # qdots = _open()
    # complex = _open()
    # solvent = _open()
    # pan = substract_line(pan, solvent)
    # qdots = substract_line(qdots, solvent)
    # complex = substract_line(complex, solvent)
    calculate_button = Button(
                    main, text='calculate', command=calculate(pan, qdots, complex)
                              ).pack()
    # xyz = calculate(pan, qdots, complex)
    # with open('result.txt', 'w') as file:
    #     file.write(xyz)
    my_label = Label(main, text='')
    my_label.config(text=f)
    main.mainloop()






def pass_lines(spectra):
    """ Пропуск первых строчек файла"""
    spectra.readline()
    spectra.readline()
    spectra = spectra.readlines()
    return spectra

def spectra_value_to_float(spectra):
    """ Функция работает с исходными данными
    (убирает переносы строк и объединяет числа, разделенные табуляцией)
    и возвращает список из дробных чисел"""
    spectra_2 = []
    for line in spectra:
        line = line.rstrip("\n")
        line = line.split(sep='\t')
        spectra_2.append(line)
    spectra_3 = []
    for value in spectra_2:
        spectra_4 = []
        for number in value:
            number = float(number)
            spectra_4.append(number)
        spectra_3.append(spectra_4)
    return spectra_3


def spectra_to_plot(spectra):


    y = []
    for i, value in enumerate(spectra):

        for m, number in enumerate(value):
            # if m == 0:
            #
            #     x.append(number)
            if m == 1:

                y.append(number)
    return y

def pre_calculate():
    pan = _open()
    qdots = _open()
    complex = _open()
    solvent = _open()
    pan = substract_line(pan, solvent)
    qdots = substract_line(qdots, solvent)
    complex = substract_line(complex, solvent)

    plot_spectra_pan = spectra_to_plot(pan)
    plot_spectra_qdots = spectra_to_plot(qdots)
    plot_spectra_complex = spectra_to_plot(complex)


    fig = Figure(figsize=(5, 5),
                dpi=100)
    plot_pan = fig.add_subplot(111)
    x = np.arange(200.0, 801.0)
    plot_qdots = fig.add_subplot(211)
    plot_complex = fig.add_subplot(311)
    plot_pan.scatter(x, plot_spectra_pan)
    plot_qdots.scatter(x, plot_spectra_qdots)
    plot_complex.scatter(x, plot_spectra_complex)
    canvas = FigureCanvasTkAgg(fig, master=main)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, main)
    toolbar.update()
    canvas.get_tk_widget().pack()





def _open():
    def open_file():
        """Открывает файл и проделывает с ним необходимые операции, возвращает
        массив"""
        a = (
        filedialog.askopenfilenames(initialdir="None",title="select a file",
        filetypes=[("all files", "*.*")])
        )
        return list(a)
    a = open_file()
    a = "".join(a)
    with open(a, 'r') as file:
        file = pass_lines(file)
        file = spectra_value_to_float(file)
    return file


def substract_line(spectra_1, spectra_2):
    """Производит вычитание целого числа из элемента массива
    ((нужно для учета физического явления, если не вдаваться в подробности))"""

    p = spectra_2[600][1]

    for i, entry in enumerate(spectra_1):
        entry[1] -= p

    return spectra_1


def calculate(spectra_1, spectra_2, spectra_3):

    """Работа только со вторым столбцом  исходного массива, составление
    и решение линейного уравнения"""
    def value_in_spectra(spectra):
        values = []
        for value in spectra:
            for index, number in enumerate(value):
                if index == 1:
                    number = number
            values.append(number)
        return values
    a = value_in_spectra(spectra_1)
    b = value_in_spectra(spectra_2)
    c = value_in_spectra(spectra_3)

    for i_a, value_a in enumerate(a):
        m = a[250]
        p = a[350]
    for i_b, value_b in enumerate(b):
        k = b[250]
        n = b[350]
    for i_c, value_c in enumerate(c):
                # values_spectra = []
                # while i_a, i_b, i_c in range (0, len(c)):
                # else:
                #     break
        u = c[250]
        w = c[350]
    M = np.array([[m, n], [p, k]]) # Матрица (левая часть системы)
    v = np.array([u, w]) # Вектор (правая часть системы)
    global f
    f = np.linalg.solve(M, v)
            # values_spectra.append(f)

    print(f)
    return f


run()
