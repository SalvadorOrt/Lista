
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
        temp = self.head
        while(temp):
            print(temp.elemento,end = '')
            if temp.next != None:
                print(' -> ',end = '')
            temp = temp.next
        print()
        print(self.length )
    def append(self,dato)->bool:
        nodo = Nodo(dato)
        if self.length == 0:
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo
            self.tail = nodo
        self.length += 1
        return True
    def prepend(self,dato):
        nodo = Nodo(dato)
        if self.length == 0:
            self.head = nodo
            self.tail = nodo
        else:
            nodo.next = self.head
            self.head = nodo
        self.length +=1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next is not None):
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
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.elemento
    def find(self,dato):
        c = 0
        temp = self.head
        while(temp is not None):
            if temp.elemento == dato:
                break
            c+=1
            temp = temp.next
        return c
    def get(self,index):
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    def remove(self,index):
        if index == 0:
            return self.prepop()
        if self.length == index:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.elemento
    
    def remove_elemento(self,dato):
        contador = self.find(dato)
        if contador == 0:
            return self.prepop()
        if contador == self.length-1:
            return self.pop()

        return self.remove(contador)
    def insert(self,pos,dato):
        if pos == 0:
            return self.prepend(dato)
        if self.length == pos:
            return self.append(dato)
        nodo = Nodo(dato)
        temp = self.get(pos-1)
        nodo.next = temp.next
        temp.next = nodo
        self.length += 1
        
    
        

l = ListaEnlazada()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.print()
l.prepend(5)
l.print()
l.insert(0,12213)
l.print()
