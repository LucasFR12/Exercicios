lista = ["python", 'c++', "ruby", "kotlin"]

for x in lista:
    print(x)

print("=" * 50)

npcs = [
    {"name": "Monstro 1", "level": 1},
    {"name": "Monstro 2", "level": 2},
    {"name": "Monstro 3", "level": 3},
    {"name": "Monstro 4", "level": 4},
    {"name": "Monstro 5", "level": 5},
]

for x in npcs:
    print(f'Nome: {x['name']} // Level: {x['level']}')

print("=" * 50)

lista_npcs = []

def criar_monstro(nome, level):
    novo_npc = {
        "nome" : nome,
        "level": level,
        }
    return novo_npc
    
lista_npcs.append(criar_monstro("Monstro", 10))
lista_npcs.append(criar_monstro("Monstro 5", 13))
lista_npcs.append(criar_monstro("Monstro 10", 15))

for x in lista_npcs:
    print(f'Nome: {x['nome']} // Level: {x['level']}')