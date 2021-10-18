def merge(array, l, m, r, byFunc):
  while l < r and m < r:
    print(
      f'left = {l} {array[l]} {byFunc(array[l])}, mid = {m} {array[m]} {byFunc(array[m])}, right = {r} {array[r]} {byFunc(array[r])}')
    print(f'compare {array[l]} and {array[m + 1]}')
    if byFunc(array[l]) > byFunc(array[m + 1]):
      popped = array.pop(m + 1)
      array.insert(l, popped)
      m += 1
      print('SWAPPED', array)
    else:
      l += 1
      print("NO SWAP")
  print(array)


def splitArray(array, l, r, byFunc):
  m = int((r - l) / 2) + l
  print(array[l:r + 1])
  if len(array) == 1:
    return array
  if l + 1 == r:  # array is length 2
    print("SIZE 2")
    merge(array, l, m, r, byFunc)
  elif l + 2 == r:  # special case where the list is length 3, manually "split" then merge
    print("SIZE 3")
    merge(array, l, m - 1, r - 1, byFunc)
    if byFunc(array[l]) > byFunc(array[m + 1]):
      popped = array.pop(m + 1)
      array.insert(l, popped)
    print(array)
    merge(array, l, m, r, byFunc)
  else:
    print("RECURSION")
    splitArray(array, l, m, byFunc)
    splitArray(array, m + 1, r, byFunc)
    merge(array, l, m, r, byFunc)


def mergesort(array, byFunc=None):
  l = 0
  m = int((len(array) - 1) / 2)
  r = len(array) - 1
  print(f'starting array: {array}, l = {l}, m = {m}, r = {r}')
  if len(array) > 3:
    splitArray(array, l, m, byFunc)
    print("lele")
    splitArray(array, m + 1, r, byFunc)
    merge(array, l, m, r, byFunc)
  elif len(array) == 3:
    merge(array, l, m - 1, r - 1, byFunc)
    if byFunc(array[l]) > byFunc(array[m + 1]):
      popped = array.pop(m + 1)
      array.insert(l, popped)
    print(array)
    merge(array, l, m, r, byFunc)
  elif len(array) == 2:
    merge(array, l, m, r, byFunc)


class Stack:
  def __init__ (self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.items != []:
      return self.items.pop()

  def peek(self):
    if self.items != []:
      return self.items[-1]

  @property
  def isEmpty(self):
    return self.items == []

  @property
  def size(self):
    return len(self.items)


class EvaluateExpression:
  valid_char = '0123456789+-*/() '

  def __init__(self, string=""):
    self.expr = string

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    for char in new_expr:
      if char not in self.valid_char:
        self.expr = ''
        return
    self.expr = new_expr

  def insert_space(self):
    temp = []
    newString = self.expr
    for i, char in enumerate(self.expr):
      if char in '+-*/()':
        temp.append(i)
    temp.reverse()
    for i in temp:
      newString = f'{newString[:i]} {newString[i:i + 1]} {newString[i + 1:]}'
    return newString

  def process_operator(self, opdStack, oprStack):
    o2 = opdStack.pop()
    o1 = opdStack.pop()
    O = oprStack.pop()

    print(f'{o1} {O} {o2}')

    calculate = {
      '+': int(o1) + int(o2),
      '-': int(o1) - int(o2),
      '*': int(o1) * int(o2),
      '/': int(o1) // int(o2)
    }
    opdStack.push(calculate.get(O, 0))
    print(opdStack.items)

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    processFlag = False
    tokens = expression.split()

    for i in tokens:
      print(f'operand stack: {operand_stack.items}, operator stack: {operator_stack.items}')
      if i in '0123456789':
        print(i)
        operand_stack.push(i)
      elif i in '+-':
        print(f'current item: {i}')
        while not operator_stack.isEmpty and operator_stack.peek() not in ')(':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(i)
      elif i in '*/':
        print(f'current item: {i}')
        while not operator_stack.isEmpty and operator_stack.peek() in '*/':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(i)
      elif i == '(':
        print(f'current item: {i}')
        operator_stack.push(i)
      elif i == ')':
        print(f'current item: {i}')
        while operator_stack.peek() != '(':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop()  # get rid of the (

    while not operator_stack.isEmpty:
      self.process_operator(operand_stack, operator_stack)

    print("ANSWER: ", operand_stack.peek())
    return operand_stack.peek()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





