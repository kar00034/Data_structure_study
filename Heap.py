def heap_sort(a):
    def swap(a, i, j):
        a[i], a[j] = a[j], a[i]

    def siftdown(a, p, size):
        l = 2 * p + 1
        r = 2 * p + 2
        largest = p
        if l <= size - 1 and a[l] > a[p]:
            largest = l
        if r <= size - 1 and a[r] > a[largest]:
            largest = r
        if largest != p:
            swap(a, p, largest)
            siftdown(a, largest, size)

    def heapify(a, size):
        p = (size // 2) - 1
        while p >= 0:
            siftdown(a, p, size)
            p -= 1

    size = len(a)
    heapify(a, size)
    end = size - 1
    while (end > 0):
        swap(a, 0, end)
        siftdown(a, 0, end)
        end -= 1

if __name__ == "__main__":
    arr = [1, 3, 2, 4, 9, 7, 5, 7, 8, 3, 1]
    heap_sort(arr)
    print(arr)
