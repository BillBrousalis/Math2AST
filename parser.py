from lexer import *
from tree import *

class Parser:
  def __init__(self, lexer: Lexer):
    self.lexer = lexer
  
  def error(self, msg):
    print(f'[!] Parser error: {msg}')
    exit(-1)

  def parse(self):
    nodes = []
    while (current_token := self.lexer.current_token()) is not None:
      nodes.append(self.expression())
    return nodes[0]

  def eat(self, expected_type):
    current_token = self.lexer.current_token()
    if current_token.type != expected_type:
      self.error(f'eat() - token type different than the expected type\n'
                 f'  Token value: {current_token.value}\n'
                 f'   Token type: {current_token.type}\n'
                 f'Expected type: {expected_type}')
    self.lexer.advance_token()
    if current_token is None: self.error('eat() - current token is None')
    return self.create_node(current_token.value, current_token.type)

  def create_node(self, value, type):
    return Node(value, type)
  
  def expression(self):
    return self.additive_expression()

  def additive_expression(self):
    left = self.multiplicative_expression()
    op, right = None, None
    while self.lexer.current_token() is not None and self.lexer.current_token().type == TokenType.ADD:
      op = self.eat(TokenType.ADD)
      right = self.multiplicative_expression()
      op.left, op.right = left, right
      left = op
    return left

  def multiplicative_expression(self):
    left = self.unary_expression()
    op, right = None, None
    while self.lexer.current_token() is not None and self.lexer.current_token().type == TokenType.MUL:
      op = self.eat(TokenType.MUL)
      right = self.unary_expression()
      op.left, op.right = left, right
      left = op
    return left

  def numeric_literal(self):
    return self.eat(TokenType.NUM)

  def parenthesis_expression(self):
    self.eat(TokenType.PAR)
    exp = None
    if self.lexer.current_token() is not None and self.lexer.current_token().value != ')':
      exp = self.expression()
    else:
      print('parenthesis_expression() - Invalid (?)')
    self.eat(TokenType.PAR)
    return exp

  def unary_expression(self):
    op = None
    if self.lexer.current_token().type == TokenType.ADD:
      op = self.eat(TokenType.ADD)
      op.type = TokenType.UNARY
      op.left = self.unary_expression()
      return op
    return self.primary_expression()

  def primary_expression(self):
    if self.lexer.current_token().type == TokenType.PAR:
      return self.parenthesis_expression()
    else:
      return self.numeric_literal()
