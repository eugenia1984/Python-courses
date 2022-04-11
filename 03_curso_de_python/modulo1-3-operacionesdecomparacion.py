# Al comprarar dos números se obtiene True o False (Verdadero o Falso) según si se cumple la condición.

# Ejemplo 1:
z = True
y = False 
x = 4
print(x >= 4)          #True
print(x < 3)            #False
 
# Ejemplo 2:
num = int( input() )
num = (2 * num) == 0
print( num )       #con cualquier número va a ser True

#Ejemplo 3:
# cond1 and cond2 => para que sea True ambos deben ser True
# cond1 or cond2  => para que sea True basta que uno sea True

a = 4
b = a > 5 and a < 7      
c = a > 5 or a < 7       
d = not a > 5    

print(b)    # False porque: 4>5 and 4<7 False and True => Con and necesito ambas True para que de resultado True
print(c)   # True porque: 4>5 or 4<7 False or True => Con or necesito que al menos una sea True
print(d)  # True porque: not 4>5 => tengo not False, que es True

# Ejemplo 4:
r = True or False and not (1>2)  # True or False and True => True or False => True
print(r)

# Estas condiciones pueden agruparse con ( condicion1 ) and/or ( condicion2 ), esto permite chequar condiciones complejas:
e = 10
f = 5
g = (f > e and 15 > e) or (f < e and 15 > x)
print(g)

# TRUE: (5>10 and 15>10) or (5<10 and 15>10) => (False and True) or (True and True) => False or True

