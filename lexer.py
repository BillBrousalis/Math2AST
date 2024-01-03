from enum import Enum

class TokenType(Enum):
  NUM = 0
  ADD = 1
  MUL = 2
  PAR = 3
  UNARY = 4

class Token:
  def __init__(self, value):
    self.value = value
    match value:
      case '+' | '-': self.type = TokenType.ADD
      case '*' | '/': self.type = TokenType.MUL
      case '(' | ')': self.type = TokenType.PAR
      case _: self.type = TokenType.NUM
  
  def __str__(self):
    return f'<Token value = "{self.value}", type = {self.type}>'

class Lexer:
  def __init__(self):
    self.idx = 0
    self.tokens = []

  def length(self):
    return len(self.tokens)

  def tokenize(self, input_text):
    for x in input_text.split(' '):
      if x not in ('', '\n'): self.tokens.append(Token(x))

  def print_tokens(self):
    for token in self.tokens: print(token)

  def current_token(self):
    if self.idx >= len(self.tokens): return None
    return self.tokens[self.idx]

  def advance_token(self):
    self.idx += 1

  def lookahead(self):
    if self.idx+1 >= len(self.tokens): return None
    return self.tokens[self.idx+1]
  