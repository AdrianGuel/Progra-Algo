# Ejemplo 1 FSM 2021
def q1():
    return "T1"

def q2():
    return "T2"

def actions(argument):
    switch ={
        1: q1,
        -1: q2
    }
    func=switch.get(argument,lambda:"invalid state")
    print(func())

cadena=[1,0,0,1,0,0,1,1]

q=1
c_state=q
k=1
actions(q)
for x in cadena:
    if x == 1:
        q=
        actions(q)
    else:
        actions(q)
    k=k+1
