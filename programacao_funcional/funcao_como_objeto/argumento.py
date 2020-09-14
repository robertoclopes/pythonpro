"""
>>> def ola():
...     print('Olá')
...
>>> executar(ola)
Olá
>>> executar(ola, 2)
Olá
Olá
>>> def ola_mundo():
...     print('Olá mundo')
...
>>> executar(ola_mundo, 3)
Olá mundo
Olá mundo
Olá mundo
"""

def executar(f, n=1):
    for _ in range(n):
        f()