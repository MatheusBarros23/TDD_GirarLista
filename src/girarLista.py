class GirarListaError(Exception):
    pass

class GirarLista:
    def gir(self, lista):
        if (lista==[]):
            return lista
        elif(type(lista) is list):
            temp = lista[0]
            for i in range(len(lista)):
                if (i==0):
                    lista.remove(temp)
                    lista.append(temp)
            return lista
        else:
            raise GirarListaError()