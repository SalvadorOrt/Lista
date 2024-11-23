class Nodo:
    def __init__(self, dato):
        self.elemento = dato
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print(self):
        if self.length == 0:
            print("La lista está vacía.")
            return
        temp = self.head
        while temp:
            print(temp.elemento, end='')
            if temp.next is not None:
                print(' -> ', end='')
            temp = temp.next
        print()
        print("Longitud:", self.length)

    def append(self, dato) -> bool:
        if dato is None:
            print("Error: No se puede agregar un elemento 'None' a la lista.")
            return False
        nodo = Nodo(dato)
        if self.length == 0:
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo
            self.tail = nodo
        self.length += 1
        return True

    def prepend(self, dato):
        if dato is None:
            print("Error: No se puede agregar un elemento 'None' a la lista.")
            return
        nodo = Nodo(dato)
        if self.length == 0:
            self.head = nodo
            self.tail = nodo
        else:
            nodo.next = self.head
            self.head = nodo
        self.length += 1

    def pop(self):
        if self.length == 0:
            print("Error: No se puede eliminar de una lista vacía.")
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.elemento

    def prepop(self):
        if self.length == 0:
            print("Error: No se puede eliminar de una lista vacía.")
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.elemento

    def find(self, dato):
        if dato is None:
            print("Error: El dato proporcionado no puede ser 'None'.")
            return -1
        c = 0
        temp = self.head
        while temp is not None:
            if temp.elemento == dato:
                return c
            c += 1
            temp = temp.next
        print(f"El elemento '{dato}' no se encontró en la lista.")
        return -1

    def get(self, index):
        if index < 0 or index >= self.length:
            print(f"Error: Índice {index} fuera de rango.")
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def remove(self, index):
        if index < 0 or index >= self.length:
            print(f"Error: Índice {index} fuera de rango.")
            return None
        if index == 0:
            return self.prepop()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.elemento

    def remove_elemento(self, dato):
        contador = self.find(dato)
        if contador == -1:
            print(f"Error: El elemento '{dato}' no existe en la lista.")
            return None
        return self.remove(contador)

    def insert(self, pos, dato):
        if pos < 0 or pos > self.length:
            print(f"Error: Índice {pos} fuera de rango.")
            return
        if dato is None:
            print("Error: No se puede insertar un elemento 'None' en la lista.")
            return
        if pos == 0:
            return self.prepend(dato)
        if pos == self.length:
            return self.append(dato)
        nodo = Nodo(dato)
        temp = self.get(pos - 1)
        nodo.next = temp.next
        temp.next = nodo
        self.length += 1

# Ejemplo de uso:
l = ListaEnlazada()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.print()
l.prepend(5)
l.print()
l.insert(0, 12213)
l.print()
l.insert(10, 42)  # Intento insertar fuera de rango
l.append(None)    # Intento agregar un valor 'None'
