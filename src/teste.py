""" nome = set()

nome = {"1", "2", "3", "4", "5", "5", "5", "4", "4", "3", "2", "2", "2"}

print(nome)
print(type(nome))


 """
from collections import Counter


lista = [
    "maria",
    "hamburguer",
    "terça-feira" "joao",
    "hamburguer",
    "terça-feira" "maria",
    "pizza",
    "terça-feira" "maria",
    "coxinha",
    "segunda-feira" "arnaldo",
    "misto-quente",
    "terça-feira" "jose",
    "hamburguer",
    "sabado" "maria",
    "hamburguer",
    "terça-feira" "maria",
    "hamburguer",
    "terça-feira" "joao",
    "hamburguer",
    "terça-feira",
]


list = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 8, 8, 8, 8, 1, 1]
cnt = Counter([item[2] for item in lista])
print(cnt)
print(cnt.most_common())
print(cnt.most_common(4))
print(cnt.most_common(2))
print(cnt.most_common(3)[1][0])

print(cnt.most_common(3)[1][1])


# saída  [(8, 5), (1, 3), (2, 2), (3, 2), (4, 1), (6, 1), (7, 1)]