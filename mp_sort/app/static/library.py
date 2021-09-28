from org.transcrypt.stubs.browser import *
import random

array = []


def gen_random_int(number, seed):
  random.seed(seed)
  ls = [x for x in range(number)]
  random.shuffle(ls)
  return ls


def generate():
  global array

  number = 10
  seed = 200
  array = gen_random_int(number, seed)

  array_str = ""
  for i, a in enumerate(array):
    if i != len(array) - 1:
      array_str += str(a)
      array_str += ", "
    else:
      array_str += str(a)
      array_str += "."

  # This line is to placed the string into the HTML
  # under div section with the id called "generate"
  document.getElementById("generate").innerHTML = array_str


def sortnumber1():
  array_str = ""
  for i, a in enumerate(array):
    j = i + 1
    if i < len(array) - 1:
      while array[j] < array[i] and i >= 0:
        t = array[i]
        array[i] = array[j]
        array[j] = t
        i -= 1
        j -= 1
  for i, a in enumerate(array):
    if i != len(array) - 1:
      array_str += str(a)
      array_str += ", "
    else:
      array_str += str(a)
      array_str += "."

  document.getElementById("sorted").innerHTML = array_str


def sortnumber2():
  array_str = ""
  # value = "3, 5, 3, 1, 8, 22, 0"
  '''  This function is used in Exercise 2.
  The function is called when the sort button is clicked.

  You need to do the following:
  - Get the numbers from a string variable "value".
  - Split the string using comma as the separator and convert them to 
    a list of numbers
  - call your sort function, either bubble sort or insertion sort
  - create a string of the sorted numbers and store it in array_str
  '''

  # The following line get the value of the text input called "numbers"
  value = document.getElementsByName("numbers")[0].value

  # Throw alert and stop if nothing in the text input
  if value == "":
    window.alert("Your textbox is empty")
    return


  array = value.split(", ")
  newArray = [int(x) for x in array]

  for i, a in enumerate(newArray):
    j = i + 1
    print("NEXT", i, j)
    if j < len(newArray):
      while newArray[j] < newArray[i] and i >= 0:
        print(newArray, i, j)
        print(newArray[i], newArray[j])
        t = newArray[i]
        newArray[i] = newArray[j]
        newArray[j] = t
        i -= 1
        j -= 1

  print(newArray)
  for i, a in enumerate(newArray):
    if i != len(newArray) - 1:
      array_str += str(a)
      array_str += ", "
    else:
      array_str += str(a)
      array_str += "."

  print(array_str)
  document.getElementById("sorted").innerHTML = array_str