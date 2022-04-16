# DICCIONARIOS
personas = {'Brian': 26, 'Maria': 22, 'Martin': 66, 'Patricia': 55}
print(personas) # {'Brian': 26, 'Maria': 22, 'Martin': 66, 'Patricia': 55}
print(personas['Brian']) # 26 asi accedo al value desde una key
print(personas['Maria']) # 22 asi accedo al value desde una key
personas['Jose'] = 42  # para agregar un nuevo par key-value, se agrega ala final
print(personas) # {'Brian': 26, 'Maria': 22, 'Martin': 66, 'Patricia': 55, 'Jose': 42}
personas['Brian'] = 23
print(personas['Brian'])  # 23, asi modifico un value