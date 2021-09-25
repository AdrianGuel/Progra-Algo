# Ejemplo 1 version final
def q1(argument):
    if argument==1:
        q=2
    else:
        q=1
    return q

def q2(argument):
    if argument==1:
        q=1
    else:
        q=2
    return q

def actions(q,argument):
    switch ={
        1: q1,
        2: q2
    }
    func=switch.get(q,lambda:"invalid state")
    return func(argument)

# entrada de los sensores
cadena=[1,0,0,1,0,0,1]


q=1 #  estado inicial
for x in cadena:
    q=actions(q,x) # actalizacion del estado

# resultado de la evaluacion
if q==1:
    print("Numero par de unos en la cadena")
else:
    print("Numero impar de unos en la cadena")
