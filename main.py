import time
import logging


from collections import deque

class Node:
    def __init__(self, state, depth):
        self.state = state
        self.depth = depth


class Game: #In my notes, you said you also wanted me to make a model class
    def __init__(self, wolf, goat, cabbage, farmer, path=None):
        self.wolf = wolf
        self.goat = goat
        self.cabbage = cabbage
        self.farmer = farmer
        self.path = path


    def getWolf(self):
        return self.wolf

    def getGoat(self):
        return self.goat

    def getCabbage(self):
        return self.cabbage

    def getFarmer(self):
        return self.farmer


    def drawPath(self):
        The_plan = "Howdy there! A Farmer is now traveling with his wildest buddies, the roughest Wolf, the cowardly Goat, and the shy Cabbage.\nLooks like the farmer must cross a river. Oh wait, he only has one boat, and can only take one critter with him at a time. What will he do now?\n"
        for item in self.path:
            if(item[0] == 0):
                The_plan += "We see that the Wolf is on the start side! \n"

            if(item[1] == 0):
                The_plan += "We see that the Goat is on the start side! \n"

            if(item[2] == 0):
                The_plan += "We see that the Cabbage is on the start side! \n"

            if (item[0] == 1):
                The_plan += "We see that the Wolf is on the other side! \n"

            if (item[1] == 1):
                The_plan += "We see that the Goat is on the other side! \n"

            if (item[2] == 1):
                The_plan += "We see that the Cabbage is on the other side! \n"

            if (item[3] == 0):
                The_plan += "We see that the Farmer is on the start side with "

            if (item[3] == 1):
                The_plan += "We see that the Farmer is on the other side with "

            if(item[0] == item[3]):
                The_plan += "the Wolf and "

            if (item[1] == item[3]):
                The_plan += "the Goat and "

            if (item[2] == item[3]):
                The_plan += "the Cabbage and "

            if (item[3] != item[1] and item[3] != item[2] and item[3] != item[0]):
                The_plan += "Absolutely Nobody! Oh no! Something is gonna get eaten! and "

            The_plan += "What's the farmer gonna do?\nThe farmer has made his mark, and now "


        The_plan += "everybody is safe across! Ye-hoo! The Farmer now walks away peacefully with his fellow friends.\nGood-bye!\nSee you next time!\n"

        print(The_plan)


def alt_reverse(A): #Because the built in reverse function was not working for some reason
    for i in range(len(A)//2):
        A[i], A[len(A)-i-1] = A[len(A)-i-1], A[i]


    return A


def IDS(frontier, L, start):
    parent = {}

    should_we_break = False
    while should_we_break == False:
        pass_frontier = frontier.copy()
        A, Generated, Expanded, Solution_Depth, frontier_size = DLS(pass_frontier, L, parent, start)

        L += 1


        if A is not None:
            #print(A)
            return A, Generated, Expanded, Solution_Depth, frontier_size

    
    return None, None, None, None, None



def DLS(frontier, L, parent, start):
    explored = set()
    cutoff = False
    Generated = 1
    Expanded = 0

    frontier_size = 0

    while len(frontier) > 0 and cutoff == False:
        node = frontier.pop()

        if(GoalTest(node.state, (1, 1, 1, 1))):
            solution_depth = 0
            path = [(1, 1, 1, 1)]

            while path[-1] != start:
                path.append(parent[path[-1]])
                solution_depth += 1



            alt_reverse(path)


            return path, Generated, Expanded, solution_depth, frontier_size

        if node.depth == L:
            frontier.append(node)
            cutoff = True
            continue

        if node not in explored:
            explored.add(node.state)

            A = Actions(node.state)

            for a in alt_reverse(A):
                s_p = Transition(node.state, a)
                node_sp = Node(s_p, node.depth + 1)
                Generated += 1
                Expanded += 1
                if node_sp.state not in frontier and s_p not in explored:
                    frontier.append(node_sp)
                    if(len(frontier) > frontier_size):
                        frontier_size = len(frontier)
                    parent[s_p] = node.state

    return None, Generated, Expanded, 0, frontier_size

def BFS(frontier, start):
    frontier.append(start)


    parent = {}


    Generated = 1

    Expanded = 0

    frontier_size = 0



    explored = set()


    while len(frontier) > 0:
        n = frontier.popleft()


        if(GoalTest(n, (1, 1, 1, 1))):
            depth = 0
            path = [(1, 1, 1, 1)]
            while path[-1] != start:
                path.append(parent[path[-1]])
                depth += 1

            path.reverse()

            return path, depth, Generated, Expanded, frontier_size

        explored.add(n)


        for a in Actions(n):
            s_p = Transition(n, a)

            Generated += 1
            Expanded += 1

            if s_p not in frontier and s_p not in explored:
                frontier.append(s_p)

                if(len(frontier) > frontier_size):
                    frontier_size = len(frontier)

                parent[s_p] = n





def Actions(state):
    A = (1, 0, 0, 1)
    B = (0, 1, 0, 1)
    C = (0, 0, 1, 1)
    D = (0, 0, 0, 1)
    actions_list = []

    if(state[3] == state[0]):
        actions_list.append(A)

    if(state[3] == state[1]):
        actions_list.append(B)

    if(state[3] == state[2]):
        actions_list.append(C)

    if(state[3] == state[0] or state[3] == state[1] or state[3] == state[2]):
        actions_list.append(D)

    return actions_list

def GoalTest(n, goal):
    if n == goal:
        return True
    return False


def Transition(state, action):
        current_state = state

        new_state = []
        for i in range(len(action)):
            if(action[i] == 1 and current_state[i] == action[i]):
                new_state.append(0)

            elif(action[i] == 1 and current_state[i] != action[i]):
                new_state.append(1)

            else:
                new_state.append(current_state[i])



        if((new_state[0] == new_state[1] and new_state[3] != new_state[0]) or (new_state[1] == new_state[2] and new_state[3] != new_state[1])):
            return current_state



        current_state = tuple(new_state)

        return current_state


def main():
    logging.basicConfig(level=logging.INFO)

    print()
    print()
    print("Instance One:")
    print()
    print()

    q = deque()


    start = time.perf_counter()

    solution1, depth, Generated, Expanded, Frontier_Size = BFS(q, (0, 0, 0, 0))

    elapsed1 = (time.perf_counter() - start) * 1000



    print(solution1)

    print("Time of BFS: ", elapsed1)

    print("Depth of BFS: ", depth)

    print("Expanded: ", Expanded)
    print("Generated: ", Generated)
    print("Frontier Size: ", Frontier_Size)

    stack = [Node((0, 0, 0, 0), 0)]

    L = 0

    start = time.perf_counter()

    solution2, Generated, Expanded, Depth, Frontier_Size = IDS(stack, L, (0, 0, 0, 0))

    elapsed2 = (time.perf_counter() - start) * 1000


    print(solution2)

    print("Time of IDS: ", elapsed2)

    print("Generated from IDS: ", Generated)
    print("Expanded from IDS: ",Expanded)
    print("Depth of Solution from IDS: ",Depth)
    print("Frontier Size: ", Frontier_Size)

    print()
    print()
    print("Instance Two:")
    print()
    print()

    q = deque()

    start = time.perf_counter()

    solution1, depth, Generated, Expanded, Frontier_Size = BFS(q, (0, 0, 1, 0))

    elapsed1 = (time.perf_counter() - start) * 1000

    print(solution1)

    print("Time of BFS: ", elapsed1)

    print("Depth of BFS: ", depth)

    print("Expanded: ", Expanded)
    print("Generated: ", Generated)
    print("Frontier Size: ", Frontier_Size)

    stack = [Node((0, 0, 1, 0), 0)]

    L = 0

    start = time.perf_counter()

    solution2, Generated, Expanded, Depth, Frontier_Size = IDS(stack, L, (0, 0, 1, 0))

    elapsed2 = (time.perf_counter() - start) * 1000

    print(solution2)

    print("Time of IDS: ", elapsed2)

    print("Generated from IDS: ", Generated)
    print("Expanded from IDS: ", Expanded)
    print("Depth of Solution from IDS: ", Depth)
    print("Frontier Size: ", Frontier_Size)


    print()
    print()
    print("Model: ")
    print()
    print()

    q = deque()

    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    game = Game(0, 0, 0, 0, solution1)
    game.drawPath()


def benchmark():
    start = time.perf_counter()
    q = deque()
    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)

    start = time.perf_counter()
    q = deque()
    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)


    start = time.perf_counter()
    q = deque()
    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)


    start = time.perf_counter()
    q = deque()
    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)


    start = time.perf_counter()
    q = deque()
    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)


    start = time.perf_counter()
    q = deque()
    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)


    start = time.perf_counter()
    q = deque()
    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)


    start = time.perf_counter()
    q = deque()
    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)


    start = time.perf_counter()
    q = deque()
    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)


    start = time.perf_counter()
    q = deque()
    solution1, _, _, _, _ = BFS(q, (0, 0, 0, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)



    print()
    print()
    print()
    print()

    start = time.perf_counter()
    stack = [Node((0, 0, 1, 0), 0)]
    L = 0
    solution1, _, _, _, _ = IDS(stack, L, (0, 0, 1, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)

    start = time.perf_counter()
    stack = [Node((0, 0, 1, 0), 0)]
    L = 0
    solution1, _, _, _, _ = IDS(stack, L, (0, 0, 1, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)

    start = time.perf_counter()
    stack = [Node((0, 0, 1, 0), 0)]
    L = 0
    solution1, _, _, _, _ = IDS(stack, L, (0, 0, 1, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)

    start = time.perf_counter()
    stack = [Node((0, 0, 1, 0), 0)]
    L = 0
    solution1, _, _, _, _ = IDS(stack, L, (0, 0, 1, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)

    start = time.perf_counter()
    stack = [Node((0, 0, 1, 0), 0)]
    L = 0
    solution1, _, _, _, _ = IDS(stack, L, (0, 0, 1, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)

    start = time.perf_counter()
    stack = [Node((0, 0, 1, 0), 0)]
    L = 0
    solution1, _, _, _, _ = IDS(stack, L, (0, 0, 1, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)

    start = time.perf_counter()
    stack = [Node((0, 0, 1, 0), 0)]
    L = 0
    solution1, _, _, _, _ = IDS(stack, L, (0, 0, 1, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)

    start = time.perf_counter()
    stack = [Node((0, 0, 1, 0), 0)]
    L = 0
    solution1, _, _, _, _ = IDS(stack, L, (0, 0, 1, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)

    start = time.perf_counter()
    stack = [Node((0, 0, 1, 0), 0)]
    L = 0
    solution1, _, _, _, _ = IDS(stack, L, (0, 0, 1, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)

    start = time.perf_counter()
    stack = [Node((0, 0, 1, 0), 0)]
    L = 0
    solution1, _, _, _, _ = IDS(stack, L, (0, 0, 1, 0))
    elapsed = (time.perf_counter() - start) * 1000
    print(elapsed)



if __name__ == '__main__':
    #main()
    benchmark()
