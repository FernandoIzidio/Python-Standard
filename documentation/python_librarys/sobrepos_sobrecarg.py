import string
"""
dunder_methods - Definem as operações suportadas por um objeto, define também as caracteristicas, metódos e funções de um obj

Sobreposição - Sobrepor os metódos já existentes(na parent class) e assim mudar o comportamento de determinados metódos nas childs class
Sobrecarga(Não suportado pelo python)-  Qualquer metódo pode ser implementado em qualquer classe/objeto, mesmo que esse metódo não esteja presente nas parents class 

sobrecarga de metódos nada mais é que  implementar, incorporar novos metódos e atributos a um objeto ou classe, mesmo que esses metódos/attrs a serem acrescentados não estejam presentes na parent class 
"""

class My_Template(string.Template):
    def __truediv__(self, other):
        self.representa = self.substitute(other)
        return self

    def __str__(self) -> str:
        return self.representa
    

values = {'var': 'foo'}
temp = string.Template('texto /var /var')
temp.delimiter = '/'
print(temp / values)