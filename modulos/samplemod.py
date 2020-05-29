# Sample module 'samplemod'

"""
Módulo de ejemplo para el Curso de Introducción a la Programación en Python

Ejemplifica como usar un fichero .py tanto como módulo como como script.
"""

print('Loading...')

def double(x):
    return 2*x

if __name__ == "__main__":
    import sys
    print('Tu valor doblado:', double(float(sys.argv[1])))