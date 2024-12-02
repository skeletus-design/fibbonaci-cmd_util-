# import time
from time import perf_counter
import inquirer

import algoritms, huffman_encoder

class Bench():

    def start(self):
        options = ['Алгоритмы для чисел Фибоначчи', 'Кодировка алгоритмом Хаффмана', 'Декодирование алгоритмом Хаффмана']
        questions = [inquirer.List('select', message="Выберите категорию", choices=options, ), ]
        answers = inquirer.prompt(questions)

        if answers["select"] == "Алгоритмы для чисел Фибоначчи":
            self.gui()
        elif answers["select"] == "Кодировка алгоритмом Хаффмана":
            print("Введите строку для кодирования: ")
            s = input()
            huffman_encoder.huffman_encode(s)

            self.start()
        elif answers["select"] == "Декодирование алгоритмом Хаффмана":
            print("None ;3")
            print("")
            self.start()

    def gui(self):
        # Опции меню выбора
        options = ['fib_recursive', 'fib_loop', 'fib_array', 'fib_binet', 'fib_big_even_odd']
        questions = [inquirer.List('algorytm', message="Каким алгоритмом считать число фибоначчи?", choices=options, ), ]
        answers = inquirer.prompt(questions)

        self.select_method = None

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
        
        elif answers["algorytm"] == "fib_binet":
            print('Введите число:')
            self.bin()

        elif answers["algorytm"] == "fib_big_even_odd":
            print('Введите число:')
            self.fib_eo()
    
    def rec(self):
        n = int(input())

        time_start = perf_counter()
        print(f"Значение: {algoritms.fib_recursive(n)}")
        time_end = perf_counter()

        duration = time_end - time_start
        print(f"Посчитано за {duration}")

        self.gui()

    def loop(self):
        n = int(input())

        time_start = perf_counter()
        print(f"Значение: {algoritms.fib_loop(n)}")
        time_end = perf_counter()

        duration = time_end - time_start
        print(f"Посчитано за {duration}")

        self.gui()

    def arr(self):
        n = int(input())

        time_start = perf_counter()
        print(f"Значения: {algoritms.fib_array(n)}")
        time_end = perf_counter()

        duration = time_end - time_start
        print(f"Посчитано за {duration}")

        self.gui()

    def bin(self):
        n = int(input())

        time_start = perf_counter()
        print(f"Значения: {algoritms.fib_binet(n)}")
        time_end = perf_counter()

        duration = time_end - time_start
        print(f"Посчитано за: {duration}")

        self.gui()

    def fib_eo(self):
        n = int(input())

        time_start = perf_counter()
        print(f"Значение: {algoritms.fib_big_even_odd(n)}")
        time_end = perf_counter()

        duration = time_end - time_start
        print(f"Посчитано за: {duration}")

        if algoritms.fib_big_even_odd(n) % 2 == 0:
            print("even")
        else:
            print("odd")

        self.gui()

if __name__ == "__main__":
    App = Bench()
    App.start()
