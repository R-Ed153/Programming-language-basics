from heapPriorityQueue import HeapPriorityQueue


def pqSort(C):
    n = len(C)
    P = HeapPriorityQueue()

    for j in range(n):
        element = C.delete(C.first())
        P.add(element,element)

    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v)










