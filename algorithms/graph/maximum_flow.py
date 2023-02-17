"""
Given the capacity, source and sink of a graph,
computes the maximum flow from source to sink.
Input : capacity, source, sink
Output : maximum flow from source to sink
Capacity is a two-dimensional array that is v*v.
capacity[i][j] implies the capacity of the edge from i to j.
If there is no edge from i to j, capacity[i][j] should be zero.
"""

from queue import Queue

# pylint: disable=too-many-arguments
def dfs(capacity, flow, visit, vertices, idx, sink, current_flow = 1 << 63):
    """
    Depth First Search implementation for Ford-Fulkerson algorithm.
    """

    # DFS function for ford_fulkerson algorithm.
    if idx == sink:
        return current_flow
    visit[idx] = True
    for nxt in range(vertices):
        if not visit[nxt] and flow[idx][nxt] < capacity[idx][nxt]:
            available_flow = min(current_flow, capacity[idx][nxt]-flow[idx][nxt])
            tmp = dfs(capacity, flow, visit, vertices, nxt, sink, available_flow)
            if tmp:
                flow[idx][nxt] += tmp
                flow[nxt][idx] -= tmp
                return tmp
    return 0

def ford_fulkerson(capacity, source, sink):
    """
    Computes maximum flow from source to sink using DFS.
    Time Complexity : O(Ef)
    E is the number of edges and f is the maximum flow in the graph.
    """
    vertices = len(capacity)
    ret = 0
    flow = [[0]*vertices for _ in range(vertices)]
    while True:
        visit = [False for _ in range(vertices)]
        tmp = dfs(capacity, flow, visit, vertices, source, sink)
        if tmp:
            ret += tmp
        else:
            break
    return ret

def edmonds_karp(capacity, source, sink):
    """
    Computes maximum flow from source to sink using BFS.
    Time complexity : O(V*E^2)
    V is the number of vertices and E is the number of edges.
    """
    branches = set()

    vertices = len(capacity)
    ret = 0
    flow = []
    for _ in range(vertices):
        branches.add(1)
        flow.append([0] * vertices)
    while True:
        branches.add(2)
        tmp = 0
        queue = Queue()
        visit = []
        for _ in range(vertices):
            branches.add(3)
            visit.append(False)
        par = []
        for _ in range(vertices):
            branches.add(4)
            par.append(-1)
        visit[source] = True
        queue.put((source, 1 << 63))
        # Finds new flow using BFS.
        while queue.qsize():
            branches.add(5)
            front = queue.get()
            idx, current_flow = front
            if idx == sink:
                branches.add(6)
                tmp = current_flow
                break
            else:
                branches.add(7)
            for nxt in range(vertices):
                branches.add(8)
                if not visit[nxt] and flow[idx][nxt] < capacity[idx][nxt]:
                    branches.add(9)
                    visit[nxt] = True
                    par[nxt] = idx
                    queue.put((nxt, min(current_flow, capacity[idx][nxt]-flow[idx][nxt])))
                else:
                    branches.add(10)
        if par[sink] == -1:
            branches.add(11)
            break
        else:
            branches.add(12)
        ret += tmp
        parent = par[sink]
        idx = sink
        # Update flow array following parent starting from sink.
        while parent != -1:
            branches.add(13)
            flow[parent][idx] += tmp
            flow[idx][parent] -= tmp
            idx = parent
            parent = par[parent]
    with open('data/branch-coverage', 'a') as f:
        function_name = "edmonds_karp"
        total_branches = 13
        ratio = str(len(branches) / total_branches)
        f.write(
            f'{function_name},{total_branches},{ratio},'
        )
        branches_not_found = ""
        for i in range(1, int(total_branches) + 1):
            if i not in branches:
                branches_not_found += f"{str(i)};"
        if branches_not_found == "":
            f.write("0")
        else:
            branches_not_found = branches_not_found.strip(";")
            f.write(branches_not_found)
        f.write('\n')
    return ret

def dinic_bfs(capacity, flow, level, source, sink):
    """
    BFS function for Dinic algorithm.
    Check whether sink is reachable only using edges that is not full.
    """
    vertices = len(capacity)
    queue = Queue()
    queue.put(source)
    level[source] = 0
    while queue.qsize():
        front = queue.get()
        for nxt in range(vertices):
            if level[nxt] == -1 and flow[front][nxt] < capacity[front][nxt]:
                level[nxt] = level[front] + 1
                queue.put(nxt)
    return level[sink] != -1

def dinic_dfs(capacity, flow, level, idx, sink, work, current_flow = 1 << 63):
    """
    DFS function for Dinic algorithm.
    Finds new flow using edges that is not full.
    """
    if idx == sink:
        return current_flow
    vertices = len(capacity)
    while work[idx] < vertices:
        nxt = work[idx]
        if level[nxt] == level[idx] + 1 and flow[idx][nxt] < capacity[idx][nxt]:
            available_flow = min(current_flow, capacity[idx][nxt] - flow[idx][nxt])
            tmp = dinic_dfs(capacity, flow, level, nxt, sink, work, available_flow)
            if tmp > 0:
                flow[idx][nxt] += tmp
                flow[nxt][idx] -= tmp
                return tmp
        work[idx] += 1
    return 0

def dinic(capacity, source, sink):
    """
    Computes maximum flow from source to sink using Dinic algorithm.
    Time complexity : O(V^2*E)
    V is the number of vertices and E is the number of edges.
    """
    vertices = len(capacity)
    flow = [[0]*vertices for i in range(vertices)]
    ret = 0
    while True:
        level = [-1 for i in range(vertices)]
        work = [0 for i in range(vertices)]
        if not dinic_bfs(capacity, flow, level, source, sink):
            break
        while True:
            tmp = dinic_dfs(capacity, flow, level, source, sink, work)
            if tmp > 0:
                ret += tmp
            else:
                break
    return ret
