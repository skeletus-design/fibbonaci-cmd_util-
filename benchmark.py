# import time
from time import perf_counter
import inquirer

import algoritms

class Bench():

    def gui(self):
        # Опции меню выбора
        options = ['requrcive', 'cicle', 'coming soon']
        questions = [inquirer.List('algorytm', message="Каким алгоритмом считать число фибоначи?", choices=options, ), ]
        answers = inquirer.prompt(questions)

        # Ответ на выбор пункта меню
        if answers["algorytm"] == "requrcive":
            print('Введите число:')
            self.rec()
        elif answers["algorytm"] == "cicle":
            print('Введите число')
            self.cic()
    
    def rec(self):
        n = int(input())

        time_start = perf_counter()
        print(f"Значение: {algoritms.recr(n)}")
        time_end = perf_counter()

        duration = time_end - time_start
        print(f"Посчитано за {duration}")

    def cic(self):
        n = int(input())

        time_start = perf_counter()
        print(f"Значение: {algoritms.cicle(n)}")
        time_end = perf_counter()

        duration = time_end - time_start
        print(f"Посчитано за {duration}")

if __name__ == "__main__":
    App = Bench()
    App.gui()