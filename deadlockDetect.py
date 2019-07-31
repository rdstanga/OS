#First we will take the input properly
#Create a graph that has the process and resources as the vertex as specified in the hint.
from collections import defaultdict
class Graph():
    def __init__(self):
        self.graph = defaultdict(str)   # contains map from resource to process and process to resources
        self.pending_dict = defaultdict(list) # contains key as resource, and value as process pending on the same

    def addEdge(self,u,v):
        self.graph[u] = v
        
    def addPendingDict(self,u,v):
        self.pending_dict[u].append(v)
    
    def getPendingDict(self,u):
        if(self.pending_dict[u]):
            return self.pending_dict[u].pop(0)
        else:
            return None
            
'''
Make an edge from a resource to a process whenever a process gets a resource
and an edge from a process to a resource whenever there is a pending resource.
addPendingdict function adds a process to a pending list for a process.
'''

def isCyclic(g):
    '''
    Create a depth-first search like check. If a visited node occurs again in the same cycle, a deadlock occurs.
    '''
    key_list = g.graph.keys()
    visited = {}
    item = key_list[0]
    visited[item] = 1 
    while(key_list):
        if item in key_list:
            key_list.pop(key_list.index(item))
        if item in g.graph:
            if g.graph[item] in visited:
                return True
            item = g.graph[item]
        else:
            item = key_list[0]
            visited = {}
            visited[item]=1
    
    return False

def insert_new_process_and_check(g,el):
    el = el.split("\t") # Splitting element in each row.
    process = 'P'+ el[0]
    task = el[1]
    resource = 'R' + el[2]
    
    if(task=='W'):
        if(resource in g.graph):
            g.addEdge(process,resource) # If resource already present, put a pending edge from process to resource.
            g.addPendingDict(resource,process)
        else:
            g.addEdge(resource,process) # Allocate resources
            
    elif(task=='R'):
        new_process_allocated = g.getPendingDict(resource)
        if new_process_allocated:
            g.addEdge(resource,new_process_allocated)
            g.graph.pop(new_process_allocated)
        else:
            g.graph.pop(resource)
            
    if(isCyclic(g)):
        print ("DEADLOCK DETECTED")
        exit(0)
    else:
        print ("EXECUTION COMPLETED: No deadlock encountered.")
    return g
            
'''
Until this point from up, we have allocated, waited for, and released resources
from proccesses. It is just simple case handling, allocating, and releasing.
Now, check after each new edge whether the new thing formed is cyclic or not.
'''

    
if __name__ == '__main__':
    fp = open("input1.txt").read().split("\n")      # fp = open("filename.txt")
    g = Graph()  #initialize
    for el in fp:           # Iterate over each command
        if(el==''):         # If line is empty.
            continue
        g = insert_new_process_and_check(g,el)

