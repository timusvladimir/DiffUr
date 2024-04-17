import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

variableA = 3
variableB = 4
variableC = 2
variableD = 1

sum1 = variableA + variableD
sum2 = variableA*variableD - variableB*variableC
const1 = 1
const2 = 2

disk = sum1 * sum1 - 4 * sum2
x_list = []
y_list = []

if disk >= 0:
        gamma1 = (sum1 - math.sqrt(disk)) / 2
        gamma2 = (sum1 + math.sqrt(disk)) / 2

        xi1 = (gamma1 - variableA) / variableB
        xi2 = (gamma2 - variableA) / variableB
        print (gamma1, gamma2, xi1, xi2)

        h = 0.001
        tBegin = 0
        tEnd = 1 + h

        for t in np.arange(tBegin, tEnd, h):

            x = (const1*math.exp(gamma1*t)+const2*math.exp(gamma2*t))
            y = (const1*xi1*math.exp(gamma1*t)+const2*xi2*math.exp(gamma2*t))

            x_list.append(x)
            y_list.append(y)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_title('Графики зависимостей:', fontsize=16)
        ax.set_xlabel('x', fontsize=14)
        ax.set_ylabel('y', fontsize=14)
        ax.grid(which='major', linewidth=1.2)
        ax.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)

        ax.plot(x_list, label='')
        ax.plot(y_list, label='')

       # ax.legend()

        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())
        ax.tick_params(which='major', length=10, width=2)
        ax.tick_params(which='minor', length=5, width=1)
        plt.show()

        print(x_list)
        print(y_list)
