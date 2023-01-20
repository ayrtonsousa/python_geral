#Árvore de busca binária (BST) é uma árvore binária onde o valor de cada nó é maior ou igual aos valores em todos os nós na subárvore esquerda desse
# nó e é menor que os valores em todos os nós na subárvore direita desse nó.

#Escreva uma função que,  eficientemente  em relação ao tempo usado, verifique se uma determinada árvore de busca binária contém um determinado valor.

#Por exemplo, para a seguinte árvore:

#n1 (Valor: 1, Esquerda: nulo, Direita: nulo)
#n2 (Valor: 2, Esquerda: n1, Direita: n3)
#n3 (Valor: 3, Esquerda: nulo, Direita: nulo)
#A chamada para contains(n2, 3) deve retornar True , pois uma árvore com raiz em n2 contém o número 3.

class BSTNode(object):

    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def get(self, key):
        """Retorna uma referência ao nó de chave key
        """
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)

    def add(self, key):
        """Adiciona elemento à subárvore
        """
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)
    
    def remove(self, key):
        """Remove da árvore o elemento de chave key
        """
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            t = self.right._min()
            self.key, self.value = t.key, t.value
            self.right._deleteMin()
        return self
    
    def _min(self):
        """Retorna o menor elemento da subárvore
        """
        if self.left is None:
            return self
        else:
            return self.left._min()
    
    def _deleteMin(self):
        """Remove da subárvore o menor elemento
        """
        if self.left is None:  # encontrou o min, daí pode rearranjar
            return self.right
        self.left = self.left._deleteMin()
        return self

    def traverse(self, visit, order='pre'):
        """Percorre a árvore na ordem fornecida como parâmetro (pre, pos ou in) 
           visitando os nós com a função visit() recebida como parâmetro.
        """
        if order == 'pre':
            visit(self.key)
        if self.left is not None:
            self.left.traverse(visit, order)
        if order == 'in':
            visit(self.key)
        if self.right is not None:
            self.right.traverse(visit, order)
        if order == 'post':
            visit(self.key)

    def print(self, order='pre'):
        self.traverse(print, order)


if __name__ == '__main__':
    tree = BSTNode('S')
    tree.add('E')
    tree.add('X')
    tree.add('A')
    tree.add('R')
    tree.add('C')
    tree.add('H')
    tree.add('M')
    tree.print()