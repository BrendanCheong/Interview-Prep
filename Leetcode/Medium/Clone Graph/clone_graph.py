#link: https://leetcode.com/problems/clone-graph/
from collections import deque
from typing import Dict

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    """
    Since we are using BFS, its a typical O(V+E) time complexity,
    where we visit all neighbours of all nodes, and connect them to their copies.
    we can keep track of visited or unconnected nodes using a HashMap in O(1) time

    Space is O(V) for the HashMap
    """
    def bfs(self, node: Node) -> Dict[Node]:
        graph = { node: Node(node.val) }
        q = deque([node])

        while q:
            curr = q.popleft() # a queue dequeues from head
            for nei in curr.neighbors:
                if nei not in graph:
                    graph[nei] = Node(nei.val)
                    q.append(nei) # visit unvisited nodes
                # connect the node copy at hand to its neighboring nodes (also copies)
                # so connect the current node to the neighbours we just found
                # AND Connect to neighbours THAT HAVEN'T BEEN CONNECTED YET
                # NOTE: we must connect the current node in the CLONED GRAPH to the neighbours
                # not connect curr.neighbors to nei.neighbors
                graph[curr].neighbors.append(graph[nei])
        return graph
    def cloneGraph(self, node: Node) -> Node:
        # base case, if the node is None, return None
        if not node:
            return None
        cloned_graph = self.bfs(node)

        # return copy of the starting node
        return cloned_graph[node]