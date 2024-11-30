# import time
from time import perf_counter
import inquirer

import algoritms

class Bench():

    def gui(self):
        # Опции меню выбора
        options = ['fib_recursive', 'fib_loop', 'fib_array']
        questions = [inquirer.List('algorytm', message="Каким алгоритмом считать число фибоначи?", choices=options, ), ]
        answers = inquirer.prompt(questions)

        # Ответ на выбор пункта меню
        if answers["algorytm"] == "fib_recursive":
            print('Введите число:')
            self.rec()
        elif answers["algorytm"] == "fib_loop":
            print('Введите число:')
            self.loop()
        elif answers["algorytm"] == "fib_array":
            print('Введите число:')
            self.arr()
    
    def rec(self):
        n = int(input())

        time_start = perf_counter()
        print(f"Значение: {algoritms.fib_recursive(n)}")
        time_end = perf_counter()

        duration = time_end - time_start
        print(f"Посчитано за {duration}")

    def loop(self):
        n = int(input())

        time_start = perf_counter()
        print(f"Значение: {algoritms.fib_loop(n)}")
        time_end = perf_counter()

        duration = time_end - time_start
        print(f"Посчитано за {duration}")

    def arr(self):
        n = int(input())

        time_start = perf_counter()
        print(f"Значения: {algoritms.fib_array(n)}")
        time_end = perf_counter()

        duration = time_end - time_start
        print(f"Посчитано за {duration}")

if __name__ == "__main__":
    App = Bench()
    App.gui()