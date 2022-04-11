# OPERADORES AND Y OR PARA REVISAR 2 O MÁS CONDICIONES: algunas veces requieres que tu código revise que se cumplan 2 o más codiciones, o que se cumpl al menos 1.


# AND: las dos condiciones deben ser True 
usuario_logueado = True
usuario_adm = True
if usuario_logueado and usuario_adm:
    print('Administrador')
else:
    print('Debes iniciar sesión')
# OR: al menos una condición debe ser True
usuario_logueado2 = True
usuario_adm2 = False

if usuario_logueado2 or usuario_adm2:  #revisa que al mnos una condición cumpla y se ejecuta
    print('Administrador')
elif usuario_logueado2:        #si se cumple esta condición se ejecuta
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')

