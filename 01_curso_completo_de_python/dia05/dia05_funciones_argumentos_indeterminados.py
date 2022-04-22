def sumar(*args):
  print(args)

def mostrar(*args):
  for i in args:
    print(i)

sumar(10,20,30,40,50,60,70)  # (10, 20, 30, 40, 50, 60, 70)
mostrar('Python', True, 10, 2.8, [1, 2, 3])