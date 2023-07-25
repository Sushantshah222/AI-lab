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

# G = {
# 'A' : ['B', 'C'],
# 'B' : ['A', 'D', 'E'],
# 'C' : ['A', 'F'],
# 'D' : ['B', 'G'],
# 'E' : ['B', 'D', 'G', 'H'],
# 'F' : ['C'],
# 'G' : ['D', 'E'],
# 'H' : ['E']
# }

# for key,val in G.items():
#     print(f"{key} --> {val}")


# start = 'A'
# goal = 'H'

# def DFS(G,start,goal):
#     stack = [start]
#     visited = set()
#     previousV = dict()
#     previousV[start]=''

#     while stack:
#         popedVertex = stack.pop()
#         if popedVertex not in visited:
#             if popedVertex == goal:
            

# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
