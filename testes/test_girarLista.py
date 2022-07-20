import pytest
from src.girarLista import *

@pytest.mark.parametrize("lista, res_esp", [([2,3], [3,2]),([4,3,7], [3,7,4]),(["a","c","d"],["c","d","a"])])
def test_giro(lista, res_esp):
    i = GirarLista()
    listg = i.gir(lista)
    assert listg == res_esp

@pytest.mark.parametrize("lista", [(), (2),'f'])
def test_giro_lista(lista):
    i = GirarLista()
    with pytest.raises(GirarListaError): #um assert só para erros!!
        res = i.gir(lista)