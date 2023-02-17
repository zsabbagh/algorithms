"""
Given a n*n adjacency array.
it will give you a maximum flow.
This version use BFS to search path.

Assume the first is the source and the last is the sink.

Time complexity - O(Ef)

example

graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

answer should be

23

"""
import copy
import queue
import math

def maximum_flow_bfs(adjacency_matrix):
    """
    Get the maximum flow through a graph using a breadth first search
    """
    #initial setting
    new_array = copy.deepcopy(adjacency_matrix)
    total = 0

    branches = set()

    while True:

        branches.add(1)

        #setting min to max_value
        min_flow = math.inf
        #save visited nodes
        visited = [0]*len(new_array)
        #save parent nodes
        path = [0]*len(new_array)

        #initialize queue for BFS
        bfs = queue.Queue()

        #initial setting
        visited[0] = 1
        bfs.put(0)

        #BFS to find path
        while bfs.qsize() > 0:

            branches.add(2)

            #pop from queue
            src = bfs.get()
            for k in range(len(new_array)):

                branches.add(3)

                #checking capacity and visit
                if(new_array[src][k] > 0 and visited[k] == 0 ):
                    branches.add(4)
                    #if not, put into queue and chage to visit and save path
                    visited[k] = 1
                    bfs.put(k)
                    path[k] = src

        #if there is no path from src to sink
        if visited[len(new_array) - 1] == 0:
            branches.add(5)
            break

        #initial setting
        tmp = len(new_array) - 1

        #Get minimum flow
        while tmp != 0:
            branches.add(6)
            #find minimum flow
            if min_flow > new_array[path[tmp]][tmp]:
                branches.add(7)
                min_flow = new_array[path[tmp]][tmp]
            tmp = path[tmp]

        #initial setting
        tmp = len(new_array) - 1

        #reduce capacity
        while tmp != 0:
            new_array[path[tmp]][tmp] = new_array[path[tmp]][tmp] - min_flow
            tmp = path[tmp]
            branches.add(8)

        total = total + min_flow
    
    with open('data/branch-coverage', 'a') as f:
        f.write('maximum_flow_bfs:' + str(len(branches) / 8.0))
        for i in range(1, 9):
            if i not in branches:
                f.write(' ' + str(i))
        f.write('\n')

    return total
