class Node:
  def __init__(self, value=None, type=None):
    self.value = value
    self.type = type
    self.left = None
    self.right = None

  def __str__(self):
    return f'<Node value = "{self.value}", type = {self.type}>'
