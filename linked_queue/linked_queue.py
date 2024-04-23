class node:
    def __init__(self, name=None, next=None, prev=None):
        self.name = name
        self.next = next
        self.prev = prev

class line:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, name):
        if self.head is None:
            Node = node(name, self.head, None)
            self.head = Node
        else:
            Node = node(name, self.head, None)
            self.head.prev = Node
            self.head = Node
    

    def insert_at_end(self, name):
        if self.head is None:
            Node = node(name, self.head, None)
            self.head = Node
        else:
            itr = self.head

            while itr.next:
                itr = itr.next
            
            Node = node(name, None, itr)
            itr.next = Node


    def insert_at(self, index, name):
        if self.head is None:
            self.head = node(name, self.head, None)
            return
        elif index+1 == self.get_len()+1:
            self.insert_at_end(name)
            return
        elif index<0 or index>self.get_len():
            raise Exception("Invalid Index")
        elif index == 0:
            self.insert_at_beginning(name)
            return
    
        index_count = 0
        itr = self.head
        while itr:
            if index_count == index - 1:
                Node = node(name, itr.next, itr)
                if Node.next:
                    Node.next.prev = Node
                itr.next = Node
                break
            itr = itr.next
            index_count+=1


    def insert_values(self, name_list):
        for name in name_list:
            self.insert_at_end(name)


    def last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    

    def get_len(self):
        counter = 0
        itr = self.head
        while itr:
            itr = itr.next
            counter += 1
        return counter
    

    def find_value(self, name_to_find):
        index = 0
        itr = self.head

        while itr:
            if name_to_find == itr.name:
                return index

            itr = itr.next
            index += 1
        
        return -1
    

    def remove_at(self, index):
        if index < 0 or index >= self.get_len():
            raise Exception("Invalid Index")

        if index == 0:
            if self.head:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count += 1


    def remove_all(self):
        n = self.get_len()
        for i in range(0, n):
            self.remove_at(0)


    def reverse_list(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev


    def print_queue(self):
        if self.head is None:
            print("The queue is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.name) + ' <-- '
            itr = itr.next

        print("\n")
        print(llstr)


class greetings_choosing:
    def __init__(self):
        self.quotes = {
            "q": "\nSimple Queue Algorithm",
            "c": "if you wish to stop adding people, type 0\n",
            "q2": "person's name: ",
            "q3": "what is this person classified as? ",
            "1": "(1) regular",
            "2": "(2) person with deficiency/pregnant lady ",
            "3": "(0) stop addition"
        }
        self.situation = {
            "1": "(1) remove person in specified position",
            "2": "(2) insert person at specified position",
            "3": "(3) add person at the end of the queue",
            "4": "(4) add person at the beginning of the queue",
            "5": "(5) move queue",
            "6": "(6) reverse queue",
            "7": "(7) clear queue, end program",
        }


def main():

    Fila = line()

    calling = greetings_choosing()
    print(calling.quotes['q'])
    print(calling.quotes['c'])

    # already made queue
    #Fila.insert_at_beginning('Maria')
    #Fila.insert_at_end('Carlos')
    #Fila.insert_at_end('Mel')
    #Fila.insert_at_end('Jose')

    people_count: int = 1

    while 1:

        print(people_count, calling.quotes['q2'])
        name = str(input())

        if name == '0':
            print("exiting person addition")
            break
        
        print(calling.quotes['q3'])
        print(calling.quotes['1'])
        print(calling.quotes['2'])
        print(calling.quotes['3'])
        choice = int(input("R: "))

        if choice == 1:
            Fila.insert_at_end(name)
        elif choice == 2:
            Fila.insert_at_beginning(name)
        elif choice == 0:
            print("ending program")
            break
        else:
            raise Exception("Invalid Choice")
        
        people_count += 1
        
        Fila.print_queue()
        
    
    iteration_counter: int = 0

    while Fila.head is not None:
        if iteration_counter < 1:
            Fila.print_queue()

        print("some linked list operations: ")

        print(calling.situation['1'])
        print(calling.situation['2'])
        print(calling.situation['3'])
        print(calling.situation['4'])
        print(calling.situation['5'])
        print(calling.situation['6'])
        print(calling.situation['7'])

        sit = int(input("R: "))

        if sit == 1:
            index = int(input("in which position? ")) - 1
            Fila.remove_at(index)
        elif sit == 2:
            index = int(input("in which position? ")) - 1
            name = input("and what is the person's name? ")
            Fila.insert_at(index, name)
        elif sit == 3:
            name1 = str(input("what is the person's name? "))
            Fila.insert_at_end(name1)
        elif sit == 4:
            name2 = str(input("what is the name of the person? "))
            Fila.insert_at_beginning(name2)
        elif sit == 5:
            Fila.remove_at(0)
        elif sit == 6:
            Fila.reverse_list()
        elif sit == 7:
            Fila.remove_all()
        else:
            print("Invalid Choice")
            return
        
        Fila.print_queue()
        iteration_counter += 1


if __name__ == "__main__":
    main()
