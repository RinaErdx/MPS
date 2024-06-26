import numpy as np
from tabulate import tabulate
from DecisionHelper import DecisionHelper

if __name__ == '__main__':
    name= ['Sublime text','Jupiter Notebook','PyCharm','Visual Studio Code','Python IDLE']
    har=['Цена.','Функциональная пригодность','Временные характеристики','Удобство использования','Уровень производительности','Сопровождаемость','Эффективность']
    m = np.array([[5, 43.4, 68.9, 67, 94.3, 70, 62.3],
                  [2, 84.6, 73.4, 93, 75.7, 90, 85.8],
                  [5, 95.8, 78.7, 78, 83.9, 85, 70.4],
                  [2, 94.2, 89.5, 83, 91.4, 100, 96.7],
                  [1, 80.7, 79.6, 96, 93.9, 80, 83.4]])
    wei = [0.01, 0.2, 0.05, 0.25, 0.09, 0.15,0.25]

    dh = DecisionHelper(m, wei,name)
    print("+------Исходная таблица------+")
    print(tabulate(m, headers=har, tablefmt="grid", showindex=name, numalign="center"))
    print("+----------------------------+")
    dh.saw()
    dh.topsis()
    dh.electre()
