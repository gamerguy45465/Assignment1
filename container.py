



class Container:
    def __init__(self, start, finish):
        self.queue = Queue(start)
        self.finish = finish 

        self.A = "Take Wolf"
        self.B = "Take Goat"
        self.C = "Take Cabbage"
        self.D = "Farmer Alone"

        self.actions_list = []


    def Enqueue(self, data):
        self.queue.AddItem(data)


    def Dequeue(self):
        self.queue.RemoveItem()


    def Retrieve(self, data):
        return self.queue.Retrieve(data)


    def Print(self):
        self.queue.PrintQueue()


    def Actions(self, state):
        self.actions_list.clear()
        if(state == 0):
            self.actions_list.append(self.A)
            self.actions_list.append(self.B)
            self.actions_list.append(self.C)
            self.actions_list.append(self.D)
            return self.actions_list

        
        if(state == 1):
            return self.actions_list 

        if(state == 2):
            self.actions_list.append(self.A)
            self.actions_list.append(self.B)
            self.actions_list.append(self.D)
            return self.actions_list

        if(state == 3):
            return self.actions_list

        if(state == 4):
            self.actions_list.append(self.A)
            self.actions_list.append(self.C)
            self.actions_list.append(self.D)
            return self.actions_list

        if(state == 5):
            self.actions_list.append(self.B)
            self.actions_list.append(self.D)
            return self.actions_list

        if(state == 6):
            return self.actions_list

        if(state == 7):
            self.actions_list.append(self.B)
            self.actions_list.append(self.C)
            self.actions_list.append(self.D)
            return self.actions_list

        if(state == 8):
            self.actions_list.append(self.B)
            self.actions_list.append(self.C)
            self.actions_list.append(self.D)
            return self.actions_list

        if(state == 9):
            return self.actions_list

        if(state == 10):
            self.actions_list.append(self.B)
            self.actions_list.append(self.D)
            return self.actions_list

        if(state == 11):
            self.actions_list.append(self.A)
            self.actions_list.append(self.C)
            self.actions_list.append(self.D)
            return self.actions_list

        if(state == 12):
            return self.actions_list

        if(state == 13):
            self.actions_list.append(self.A)
            self.actions_list.append(self.B)
            self.actions_list.append(self.D)
            return self.actions_list

        if(state == 14):
            return self.actions_list

        if(state == 15):
            return self.actions_list



    def Transition(self, state, action):
        self.Actions(state)
        if(action not in self.actions_list):
            return -1
        
        #TODO: Work with some comp theory here

        



    def GoalTest(self, data):
        current = self.Retrieve(data)
        if(current == None):
            return False

        if(current.data == self.finish):
            return True 
        
        return False








class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 




class LinkedList:
    def __init__(self, head):
        self.head = head

    def getHead(self):
        return self.head

    def addToList(self, data):
        new_node = Node(data)
        current = self.head 

        while(current.next != None):
            current = current.next

        current.next = new_node


    def removeFromList(self, data):
        current = self.head 

        while(current.next.data != data or current.next != None):
            current = current.next

        current.next = current.next.next


    def removeFront(self):
        self.head = self.head.next


    def Retrieve(self, data):
        current = self.head 

        while(current != None):
            if(current.data == data):
                return current
            
            current = current.next 


        return None



    def PrintList(self):
        current = self.head 

        while(current != None):
            print(current.data, "->")
            current = current.next
                

     
    

class Queue:
    def __init__(self, data):
        head = Node(data)
        self.queue = LinkedList(head)

    def AddItem(self, data):
        self.queue.addToList(data)


    def RemoveItem(self):
        self.queue.removeFront()


    def PrintQueue(self):
        self.queue.PrintList()


    def Retrieve(self, data):
        return self.queue.Retrieve(data)
