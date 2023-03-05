# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    heights = [0] * n
    for i in range(n):
        if heights[i] != 0:
            continue
        height = 0

        while i != -1:
            if heights[i] != 0:
                height += heights[i]
                break
            height += 1
            i = parents[i]

        j = i
        while j != -1:
            if heights[j] != 0:
                break
            heights[j] = height
            height -= 1
            j = parents[j]
    max_height = max(heights)
    return max_height


def main():
    # implement input form keyboard and from files
    choose = input()
    if choose == "F":
        filename = input()
        if "a" not in filename:
            with open(filename, "r", encoding="utf-8") as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
                answer = compute_height(n, parents)
                print(answer)
    elif choose == "I":
        n = int(input())
        parents = list(map(int, input().split()))
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
main()
# print(numpy.array([1,2,3]))
