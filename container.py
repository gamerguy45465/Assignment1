
class Graph: #Since I figured it was fine just for this assignment, this is going to be a fixed graph of a fixed number of nodes
     #0, 2, 4, 5, 7, 8, 10, 11, 13, 15
    def __init__(self, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P):
        self.Adjacency = [LinkedList(A),LinkedList(B),LinkedList(C),LinkedList(D),LinkedList(E),LinkedList(F),LinkedList(G),LinkedList(H),LinkedList(I),LinkedList(J),LinkedList(K),LinkedList(L),LinkedList(M),LinkedList(N),LinkedList(O),LinkedList(P)]


    def AddEdge(self, v1, v2):
        self.Adjacency[v1].addToList(v2)


    def Access(self, item):
        for items in self.Adjacency:
            potential_item = items.Retrieve(item)
            if potential_item == item:
                return potential_item



    def printGraph(self):
        for vertex in self.Adjacency:
            vertex.PrintList()
            print()



class Container:
    def __init__(self, graph_to_pass, start, finish):
        self.queue = Queue(start)
        self.finish = finish 
        self.graph = graph_to_pass

        self.current_state = start

        #self.A = "Take Wolf"
        #self.B = "Take Goat"
        #self.C = "Take Cabbage"
        #self.D = "Farmer Alone"
        self.A = (1, 0, 0, 1)
        self.B = (0, 1, 0, 1)
        self.C = (0, 0, 1, 1)
        self.D = (0, 0, 0, 1)


    def Enqueue(self, data):
        self.queue.AddItem(data)


    def Dequeue(self):
        return self.queue.RemoveItem()


    def Retrieve(self, data):
        return self.queue.Retrieve(data)
    

    def get_size(self):
        return self.queue.get_size()


    def Print(self):
        self.queue.PrintQueue()


    def Actions(self, state):
        actions_list = []

        if(state[3] == state[0]):
            actions_list.append(self.A)

        if(state[3] == state[1]):
            actions_list.append(self.B)

        if(state[3] == state[2]):
            actions_list.append(self.C)

        if(state[3] == state[0] or state[3] == state[1] or state[3] == state[2]):
            actions_list.append(self.D)

        return actions_list
        



    def Transition(self, state, action):      
        current_state = state
        new_state = []
        for i in range(len(action)):
            if(action[i] == 1 and current_state[i] == action[i]):
                new_state.append(0)

            elif(action[i] == 1 and current_state[i] != action[i]):
                new_state.append(1)

            else:
                new_state.append(current_state[i])

        self.current_state = tuple(new_state)



        return self.current_state



    def GoalTest(self, data):
        if(data == self.finish):
            return True 
        
        return False








class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 




class LinkedList:
    def __init__(self, head):
        new_node = Node(head)
        self.color = 0 #This is for the graph implementation
        self.head = new_node

    def getHead(self):
        return self.head

    def addToList(self, data):
        new_node = Node(data)

        if(self.head == None):
            self.head = new_node
            return



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
        ret_val = self.head
        self.head = self.head.next
        return ret_val


    def Access(self, index):
        current = self.head

        incr = 0

        while(current != None):
            if(incr == index):
                return current

            current = current.next
            incr += 1

        return None


    def Retrieve(self, data):
        current = self.head 

        while(current != None):
            if(current.data == data):
                return current
            
            current = current.next 


        return None



    def PrintList(self):
        current = self.head 

        print_string = ""

        while(current != None):
            print_string += str(current.data) + " -> "
            current = current.next


        print(print_string)



    def get_size(self):
        count = 0
        current = self.head 

        while(current != None):
            count += 1
            current = current.next

        return count
                

     
    

class Queue:
    def __init__(self, data):
        self.queue = LinkedList(data)

    def AddItem(self, data):
        self.queue.addToList(data)


    def RemoveItem(self):
        return self.queue.removeFront()


    def PrintQueue(self):
        self.queue.PrintList()


    def Retrieve(self, data):
        return self.queue.Retrieve(data)
    

    def get_size(self):
        return self.queue.get_size()
