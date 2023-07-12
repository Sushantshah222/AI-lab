#breadth for search algorithm



# graph = {
#     'A' : ['B','C'],
#     'B' : ['A', 'D','E'],
#     'C' : ['A', 'F'],
#     'D' : ['B','G'],
#     'E' : ['B','H'],
#     'F' : ['C'],
#     'G' : ['D'],
#     'H' : ['E']
# }

G = {
'A' : ['B', 'C'],
'B' : ['A', 'D', 'E'],
'C' : ['A', 'F'],
'D' : ['B', 'G'],
'E' : ['B', 'D', 'G', 'H'],
'F' : ['C'],
'G' : ['D', 'E'],
'H' : ['E']
}

for key,val in G.items():
    print(f"{key} --> {val}")


start = 'A'
goal = 'H'

def DFS(G,start,goal):
    stack = [start]
    visited = set()
    previousV = dict()
    previousV[start]=''

    while stack:
        popedVertex = stack.pop()
        if popedVertex not in visited:
            if popedVertex == goal:
            