# Sample module 'samplemod'

"""
Modulo de ejemplo para el Curso de Programacion en Python

Ejemplifica como usar un fichero .py tanto como modulo como como script.
"""

print('Loading...')

def double(x):
    """
    Dobla el valor pasado
    """
    return 2*x

if __name__ == "__main__":
    import sys
    print('Tu valor doblado:', double(float(sys.argv[1])))