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

for l in lines:
  _, prereq, _, _, _, _, _, step, _, _, = l.split()
  print(step, "depends on", prereq)

  if prereq not in nodes:
    print('adding prereq', prereq, 'to nodes')
    nodes[prereq] = Node(prereq)

  if step not in nodes:
    print('adding step', step, 'to nodes')
    nodes[step] = Node(step)

  nodes[step].add_edge(nodes[prereq])

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




# resolve_dependencies(nodes['A'], resolved)
# find steps with no deps to start on
start_options = []
for i in nodes:
  # print("resolving next item in nodes", i)
  # resolve_dependencies(nodes[i], resolved)
  # print(len(nodes[i].edges))
  if len(nodes[i].edges) < 1:
    start_options.append(nodes[i])

# print(list(map(get_node_name, nodes )))
# print(nodes)

# we need to only try to resolve if there are no deps, or all the deps are in resolved
# for i in sorted(start_options, key=get_node_name):
for n in nodes:
  i = nodes[n]
  print("resolving next item in nodes", i.name)
  if i in resolved:
    print("nevermind, skipping", i.name)
    continue
  resolve_dependencies(i, resolved)

# def solve_the_hash(hash):
#   # alphabetize it
#   # loop through each node
#     # if all it's edges are in resolved (or if there are no edges)
#       # add to resolved
#     # 




order_names = list(map(get_node_name, resolved_order_list))
print(order_names)
print(">>>", "".join(order_names))