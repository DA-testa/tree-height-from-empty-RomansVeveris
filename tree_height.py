# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    children = {}

    for i in range(n):
        parent = parents[i]
        if parent not in children:
            children[parent] = []
        children[parent].append(i)

    root = parents.index(-1)
    max_height = 0
    queue = [root]
    while queue:
        max_height += 1
        for i in range(len(queue)):
            node = queue.pop(0)
            if node in children:
                queue += children[node]


    return max_height


def main():
    # implement input form keyboard and from files


  choose = input()
  if "F" in choose or "f" in choose:
    filename = input()
    if "a" not in filename:
        with open("test/" + filename, 'r') as file:
            n = int(file.readline())
            parents = list(map(int, file.readline().split()))
            answer = compute_height(n, parents)
            print(answer)
  elif "I" in choose or "i" in choose:
 
      n = int(input())
      parents = list(map(int, input().split(" ")))
      answer = compute_height(n, parents)
      print(answer)

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
