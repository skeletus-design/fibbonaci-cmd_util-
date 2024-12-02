import heapq
from collections import Counter

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
    # Построение дерева Хаффмана
    root = build_huffman_tree(s)

    # Генерация кодов
    huffman_code = build_codes(root)

    # Закодированная строка
    encoded_string = ''.join(huffman_code[char] for char in s)

    # Вывод результатов
    print("Количество уникальных символов:", len(huffman_code),";","Размер закодированной строки:", len(encoded_string))
    for char, code in sorted(huffman_code.items()):
        print(f"'{char}': {code}")
    print(encoded_string)

