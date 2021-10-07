import grafos
import pytest
    
d = {
  'A': ['B','C'],
  'B': ['C'],
  'C': ['A',],
  'D': ['A', 'B'],
}

# Creamos una lista de objetos grafo, uno con cada una de las clases que tenemos
objetos = []
for c in grafos.Grafo, grafos.DictGrafo, grafos.GrafoDict:
    objetos.append(c(d.copy()))
    
# Este test se correrá una vez con cada objeto de 'objetos'
@pytest.mark.parametrize('g', objetos)
def test_Path(g):
    """
    Test path method.
    """   
    assert g.path('B', 'A') == ['B', 'C', 'A']

    
# Este test se correrá una vez con cada objeto de 'objetos'
@pytest.mark.parametrize('g', objetos)
def test_Brackets(g):
    """
    Test bracket assignment and access.
    """
    g['E'] = ['A', 'C']
    assert g['E'] == ['A', 'C']