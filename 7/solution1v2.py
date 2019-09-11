#!/usr/bin/env python3

text_file = open("puzzle", "r")
lines = text_file.read().splitlines()
text_file.close()
# print(lines)

class Node:
  def __init__(self, name):
    self.name = name
    self.edges = set()

  def add_edge(self, node):
    self.edges.add(node)

def get_node_name(n):
  return n.name

nodes = {}
nodes_set = set()

for l in lines:
  _, prereq, _, _, _, _, _, step, _, _, = l.split()
  # print(step, "depends on", prereq)

  if prereq not in nodes:
    # print('adding prereq', prereq, 'to nodes')
    nodes[prereq] = Node(prereq)

  if step not in nodes:
    # print('adding step', step, 'to nodes')
    nodes[step] = Node(step)

  nodes[step].add_edge(nodes[prereq])

for i in nodes:
  nodes_set.add(nodes[i])


resolved = set()
resolved_order_list = []
def resolve_dependencies(node, resolved):
  print("resolving", node.name, "with edges", list(map(get_node_name, node.edges)))
  ordered_edges = sorted(node.edges, key=get_node_name)
  # print(list(map(get_node_name, node.edges)), "::", list(map(get_node_name, ordered_edges)))
  for edge in ordered_edges:
    if edge not in resolved:
      resolve_dependencies(edge, resolved)
    else:
      print(edge.name, "is already resolved")
  print("adding", node.name, "to resolved")
  resolved.add(node)
  resolved_order_list.append(node)

def resolved_contains_all_nodes(node_list):
  for i in node_list:
    if i not in resolved:
      return False
  return True

def solve(nodes_to_solve):
  still_need_to_solve = set()
  for node in sorted(nodes_to_solve, key=lambda n: n.name):
    if len(node.edges) < 1:
      print("node has no edges")
      resolved.add(node)
      resolved_order_list.append(node)
    elif not resolved_contains_all_nodes(node.edges):
      still_need_to_solve.update(node.edges)

    # print("lens", len(resolved), len(nodes_set))
    if len(resolved) == len(nodes_set):
      print("done!")
      return

  solve(still_need_to_solve)

      
    

solve(nodes_set)


order_names = list(map(get_node_name, resolved_order_list))
print(order_names)
print(">>>", "".join(order_names))