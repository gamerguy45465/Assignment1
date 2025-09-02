import container


def main():
    T = True 
    F = False 
    new_container = container.Container(0, 15)

    print(new_container.GoalTest(3))

    position, condition = BFS(new_container)




if __name__ == '__main__':
    main()