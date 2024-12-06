import heapq
from collections import Counter
import inquirer


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(s):
    frequency = Counter(s)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def build_codes(node, code="", huffman_code=None):
    if huffman_code is None:
        huffman_code = {}
    if node is not None:
        if node.char is not None:
            huffman_code[node.char] = code
        build_codes(node.left, code + "0", huffman_code)
        build_codes(node.right, code + "1", huffman_code)
    return huffman_code

def huffman_encode(s):
    root = build_huffman_tree(s)
    huffman_code = build_codes(root)
    encoded_string = ''.join(huffman_code[char] for char in s)
    return huffman_code, encoded_string

def huffman_decode(encoded_string, huffman_code):
    reverse_code = {code: char for char, code in huffman_code.items()}
    decoded_string = ""
    buffer = ""
    for bit in encoded_string:
        buffer += bit
        if buffer in reverse_code:
            decoded_string += reverse_code[buffer]
            buffer = ""
    return decoded_string

def main():
    # print("Выберите режим:")
    # print("1: Кодировать строку")
    # print("2: Декодировать строку")
    # choice = input("Введите ваш выбор (1 или 2): ").strip()

    options = ['Кодировка алгоритмом Хаффмана', 'Декодировка алгоритмом Хаффмана']
    questions = [inquirer.List('select', message="Выберите опцию", choices=options, ), ]
    answers = inquirer.prompt(questions)

    if answers['select'] == "Кодировка алгоритмом Хаффмана":
        string = input("Введите строку для кодирования: ").strip()
        huffman_code, encoded_string = huffman_encode(string)
        print(len(huffman_code), len(encoded_string))
        for char, code in sorted(huffman_code.items()):
            print(f"'{char}': {code}")
        print(encoded_string)
    elif answers['select'] == "Декодировка алгоритмом Хаффмана":
        encoded_string = input("Введите закодированную строку: ").strip()
        print("Введите коды символов в формате 'символ: код' (пустая строка для завершения):")
        huffman_code = {}
        while True:
            line = input().strip()
            if not line:
                break
            char, code = line.split(": ")
            huffman_code[char.strip("'")] = code
        decoded_string = huffman_decode(encoded_string, huffman_code)
        print(f"Декодированная строка: {decoded_string}")
    else:
        print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
