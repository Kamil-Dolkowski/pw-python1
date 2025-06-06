from collections import defaultdict, deque
from typing import List
from multiprocessing.pool import ThreadPool
from threading import Thread
from concurrent.futures.thread import ThreadPoolExecutor

import time


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)
        
    def add_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            return False
            
        self.graph[u].append(v)
        self.in_degree[v] += 1
        
        return True
    
    def detect_cycle(self):
        visited = set()
        
        def dfs(node, stack = None):
            stack = set() if stack is None else stack
            
            visited.add(node)
            stack.add(node)
            
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour, stack):
                        return True
                elif neighbour in stack:
                    return True
                    
            stack.remove(node)
            return False
            
        for node in list(self.graph):
            if node not in visited:
                if dfs(node):
                    return True
                    
        return False
            
            
    def topological_sort(self):
        result = []
        q = deque()
        
        for node in self.graph.keys():
            if self.in_degree[node] == 0:
                q.append(node)
                
        while q:
            node = q.popleft()
            result.append(node)
            
            for neighbour in self.graph[node]:
                self.in_degree[neighbour] -= 1
                
                if self.in_degree[neighbour] == 0:
                    q.append(neighbour)
                    
        return result
        
    
    def orchestrate(self):
        in_degree = self.in_degree.copy()
        q = []
        
        with ThreadPoolExecutor() as executor:
            for node in self.graph:
                if in_degree[node] == 0:
                    q.append((node, executor.submit(node.run)))
                    
            result = []
            
            while q:
                for node, _executor in q:
                    if not _executor.done():
                        continue
                    
                    q.remove((node, _executor))
                    result.append(node)
                    
                    for neighbour in self.graph[node]:
                        in_degree[neighbour] -= 1
                        
                        if in_degree[neighbour] == 0:
                            q.append((neighbour, executor.submit(neighbour.run)))
                            
        return result
                    
        
class Task():
    def __init__(self, name, sleep_time):
        self.name = name
        self.sleep_time = sleep_time
        
    def run(self):
        print(f"Task {self.name}: started")
        time.sleep(self.sleep_time)
        print(f"Task {self.name}: done")
            
        
'''
    1
    |
    2  7
    |  |
 3--+--4
 |     |
 +--5--+
    |
    6
'''
def test():
    t1 = Task("Task 1", 2)
    t2 = Task("Task 2", 2)
    t3 = Task("Task 3", 2)
    t4 = Task("Task 4", 2)
    t5 = Task("Task 5", 2)
    t6 = Task("Task 6", 2)
    t7 = Task("Task 7", 2)
    
    g = Graph()
    g.add_edge(t1, t2)
    g.add_edge(t2, t3)
    g.add_edge(t2, t4)
    g.add_edge(t3, t5)
    g.add_edge(t4, t5)
    g.add_edge(t5, t6)
    g.add_edge(t7, t4)
    
    if g.detect_cycle():
        print("Cycle detected. Abort processing")
        return
    
    print("Start processing...")
    # topological_sort nie może być wywołane przed orchestrate bo "zeruje" zależności
    # Trzeba ewentualnie poprawić topological_sort aby zawierało
    # in_degree = self.in_degree.copy()
    # i działać na kopii in_degree
    #sorted_tasks = g.topological_sort()
    #print([task.name for task in sorted_tasks])
    #for task in sorted_tasks:
    #    task.run()
    g.orchestrate()
    print("Processing done")
    
    
    
if __name__ == "__main__":
    test()