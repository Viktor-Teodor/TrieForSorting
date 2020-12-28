import time
import random
import matplotlib.pyplot as plt
class QueueNode:
    def __init__(self):
        self.node = None
        self.path = None
        self.base = 1

class Node:

    totalNumber = 0

    def __init__(self):
        self.next = [None] * 10
        self.counter = 0
        self.horizontal = 0

    def insert(self, itemToInsert):

        #Attempt to write the number from end to start

        Node.totalNumber += 1
        currentNode = self

        while itemToInsert > 9:
            digit = itemToInsert % 10
            itemToInsert //= 10

            if currentNode.next[digit] is None:
                currentNode.next[digit] = Node()

            currentNode = currentNode.next[digit]

        if currentNode.next[itemToInsert] is None:
            currentNode.next[itemToInsert] = Node()

        currentNode.horizontal += 1
        currentNode.next[itemToInsert].counter += 1

    def returnOrdered(self):

        sortedList = []
        aux = QueueNode()
        aux.node = self

        queue = [aux]
        start = end = 0

        while start <= end:
            currentQueueNode = queue[start]
            currentNode = currentQueueNode.node

            start += 1

            for digit in range(0, 10):
                if currentNode.next[digit] is not None:
                    newPath = (digit * currentQueueNode.base + currentQueueNode.path) if currentQueueNode.path is not None else digit

                    for repeat in range(0, currentNode.next[digit].counter):
                        sortedList.append(newPath)

                    aux = QueueNode()
                    aux.node = currentNode.next[digit]
                    aux.path = newPath
                    aux.base = currentQueueNode.base * 10

                    queue.append(aux)
                    end += 1

        return sortedList

    def getElement(self, index): #does a BFS in the Trie to find the right element

        if index > Node.totalNumber:
            return -1

        aux = QueueNode()
        aux.node = self

        queue = [aux]
        start = end = 0

        cumulative = 0

        while start <= end:
            currentQueueNode = queue[start]
            currentNode = currentQueueNode.node

            start += 1

            #We check if the index is in the current horizon
            if cumulative + currentNode.horizontal >= index:

                for digit in range(0, 10):
                    if currentNode.next[digit] is not None:
                        if cumulative + currentNode.next[digit].counter >= index:
                            return (currentQueueNode.path + digit * currentQueueNode.base) if currentQueueNode.path is not None else digit

                        cumulative += currentNode.next[digit].counter
            else: #it means we have to expand this horizon
                cumulative += currentNode.horizontal
                for digit in range(0, 10):
                    if currentNode.next[digit] is not None:

                        aux = QueueNode()
                        aux.path = (currentQueueNode.path + digit * currentQueueNode.base) if currentQueueNode.path is not None else digit
                        aux.base = currentQueueNode.base * 10
                        aux.node = currentNode.next[digit]

                        queue.append(aux)
                        end += 1

        return -1

def partition(listToBeSorted, start, end):
    pivot = random.randint(start, end)

    aux = listToBeSorted[end]
    listToBeSorted[end] = listToBeSorted[pivot]
    listToBeSorted[pivot] = aux

    pivot = end

    left = start
    right = end

    mode = 1

    while left < right:

        if mode == 1:
            while left <= end and listToBeSorted[left] < listToBeSorted[pivot]:
                left += 1

            mode = 0

            if left <= end and listToBeSorted[left] > listToBeSorted[pivot]:
                aux = listToBeSorted[left]
                listToBeSorted[left] = listToBeSorted[pivot]
                listToBeSorted[pivot] = aux

        if mode == 0:
            while right >= start and listToBeSorted[right] > listToBeSorted[pivot]:
                right -= 1

            mode = 1

            if right >= start and listToBeSorted[right] < listToBeSorted[pivot]:
                aux = listToBeSorted[right]
                listToBeSorted[right] = listToBeSorted[pivot]
                listToBeSorted[pivot] = aux

    return pivot

def quickSort(listToBeSorted, start = None, end = None):
    if start is None or end is None:
        quickSort(listToBeSorted, 0, len(listToBeSorted) - 1)
    else:
        if start < end:
            pivot = partition(listToBeSorted, start, end)

            quickSort(listToBeSorted, start, pivot - 1)
            quickSort(listToBeSorted, pivot + 1, end)

def merge(listToBeSorted, start, end):
    sol = []

    mid = start + (end - start) // 2

    firstIndex = start
    secondIndex = mid + 1

    while firstIndex <= mid and secondIndex <= end:
        if listToBeSorted[firstIndex] < listToBeSorted[secondIndex]:
            sol.append(listToBeSorted[firstIndex])
            firstIndex += 1
        else:
            sol.append(listToBeSorted[secondIndex])
            secondIndex += 1

    while firstIndex <= mid:
        sol.append(listToBeSorted[firstIndex])
        firstIndex += 1

    while secondIndex <= end:
        sol.append(listToBeSorted[secondIndex])
        secondIndex += 1

    listToBeSorted[start: end + 1] = sol

def mergeSort(listToBeSorted, start = None, end = None):
    if start is None or end is None:
        mergeSort(listToBeSorted, 0, len(listToBeSorted) - 1)
    else:
        if start < end:
            mid = start + (end - start)//2
            mergeSort(listToBeSorted, start, mid)
            mergeSort(listToBeSorted, mid + 1, end)
            merge(listToBeSorted, start, end)

if __name__ == "__main__":
    start = time.time()
    print("Inserting elements")

    root = Node()

    for i in range(0, 1):
        for i in range(1000, 0, -1):
            root.insert(i)

    print(time.time() - start)

    start = time.time()

    print("Ordering elements")

    root.returnOrdered()

    print(time.time() - start)

    start = time.time()

    print("Inserting 1234")

    root.insert(1234)

    print(time.time() - start)

    start = time.time()
    print("get 1000000 element")

    print(root.getElement(1000000))

    print(time.time() - start)

    print("MergeSort:")
    start = time.time()
    randomList = []

    for i in range(0, 1):
        for i in range(1000, 0, -1):
            randomList.append(i)

    mergeSort(randomList)

    print(randomList)

    print(time.time() - start)

    mineConstruction = [0.002037525177001953, 0.00999903678894043, 0.09599947929382324, 1.1119840145111084, 9.7182297706604]
    mineSorting = [0.0019958019256591797, 0.0019998550415039062, 0.006998777389526367, 0.09396648406982422, 0.7459626197814941]
    mineInserting = [0.0, 0.0, 0.0, 0.0, 0.0]
    mineSearching = [0.0, 0.0, 0.0, 0.00099945068359375, 0.0]
    mergeSortTime = [0.003142118453979492, 0.042002201080322266, 0.39299941062927246, 5.0266358852386475, 57.43868327140808]
    referral = [1000, 10000, 100000, 1000000, 10000000]

    line1, = plt.plot(referral, mineConstruction, label = "Creating")
    line2, = plt.plot(referral, mineSorting, label = "Sorting")
    line3, = plt.plot(referral, mineInserting, label = "Inserting")
    line4, = plt.plot(referral, mineSearching, label = "Searching")
    line5, = plt.plot(referral, mergeSortTime, label = "MergeSort")
    plt.legend(handles=[line1, line2, line3, line4, line5])

    #plt.legend((line1, line2, line3, line4, line5), ("Creating", "Sorting", "Inserting", "Searching", "MergeSort"))
    plt.show()
