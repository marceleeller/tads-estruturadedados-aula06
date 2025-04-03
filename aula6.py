class Pilha:
    def __init__(self):
        self.itens = []
    
    def push(self, item):
        self.itens.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        return None
    
    def is_empty(self):
        return len(self.itens) == 0

def inverter_string(string):
    pilha = Pilha()
    for char in string:
        pilha.push(char)
    
    string_invertida = ""
    while not pilha.is_empty():
        string_invertida += pilha.pop()
    
    return string_invertida

testes = [
    "Python",
    "12345",
    "!@# $%&*",
    "A casa é azul",
    "Stack" 
]

for teste in testes:
    print(f"Original: {teste} -> Invertida: {inverter_string(teste)}")