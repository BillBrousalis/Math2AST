from dsplot.tree import BinaryTree
from tree import Node
import webbrowser

def format(node: Node):
  return None if node is None else f'"{node.value}"\n{node.type.name}'

def lvl_order_traversal(root: Node):
  nodes, queue = [format(root)], [root]
  while len(queue):
    n = queue[0]
    queue = queue[1:]
    if n is None: continue
    nodes.extend([format(n.left), format(n.right)])
    queue.extend([n.left, n.right])
  while nodes and nodes[-1] is None: nodes.pop()
  return nodes

def plot(root: Node, name):
  name = f"tree_imgs/tree_{name.split('/')[-1].split('.')[0]}.png"
  nodes = lvl_order_traversal(root)
  tree = BinaryTree(nodes=nodes)
  tree.plot(output_path=name, border_color='#FFCE30', fill_color='#aec6cf')
  webbrowser.open(name)
