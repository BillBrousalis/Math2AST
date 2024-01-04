from tree import Node
from lexer import TokenType

def node_eval(node: Node):
  if node is None: return None
  match node.type:
    case TokenType.NUM:
      return float(node.value)
    case TokenType.ADD:
      if node.value == '+': return node_eval(node.left) + node_eval(node.right)
      elif node.value == '-': return node_eval(node.left) - node_eval(node.right)
    case TokenType.MUL:
      if node.value == '*': return node_eval(node.left) * node_eval(node.right)
      elif node.value == '/': return node_eval(node.left) / node_eval(node.right)
    case TokenType.UNARY:
      if node.value == '+': return node_eval(node.left)
      elif node.value == '-': return -node_eval(node.left)
