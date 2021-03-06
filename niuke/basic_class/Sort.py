import sys
import random

sys.path.append("..")
from basic import utils


@utils.clock
def selectionSort(nums):
    if not nums or len(nums) < 2:
        return
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            min_index = j if nums[j] < nums[min_index] else min_index
        utils.swap(nums, i, min_index)
    return


def bubbleSort(nums):
    if not nums or len(nums) < 2:
        return
    for k in range(len(nums), 0, -1):
        for i in range(k - 1):
            if nums[i] > nums[i + 1]:
                utils.swap(nums, i, i + 1)
    return


@utils.clock
def insertionSort(nums):
    if not nums or len(nums) < 2:
        return
    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[j + 1] >= nums[j]:
                break
            utils.swap(nums, j, j + 1)
    return


def __merge(nums, le, ri):
    if le == ri:
        return
    mid = le + ((ri - le) >> 1)
    __merge(nums, le, mid)
    __merge(nums, mid + 1, ri)
    t = [0] * (ri - le + 1)
    p1 = le
    p2 = mid + 1
    i = 0
    while p1 <= mid and p2 <= ri:
        if nums[p1] <= nums[p2]:
            t[i] = nums[p1]
            p1 += 1
        else:
            t[i] = nums[p2]
            p2 += 1
        i += 1
    while p1 <= mid:
        t[i] = nums[p1]
        i += 1
        p1 += 1
    while p2 <= ri:
        t[i] = nums[p2]
        i += 1
        p2 += 1

    for i, j in enumerate(range(le, ri + 1)):
        nums[j] = t[i]

    return


@utils.clock
def mergeSort(nums):
    if not nums or len(nums) < 2:
        return
    return __merge(nums, 0, len(nums) - 1)


def _partition(nums, l, r):
    pL = l - 1
    pR = r
    i = l
    while i < pR:
        if nums[i] < nums[r]:
            utils.swap_xor(nums, i, pL + 1)
            pL += 1
            i += 1
        elif nums[i] > nums[r]:
            utils.swap_xor(nums, i, pR - 1)
            pR -= 1
        else:
            i += 1

    utils.swap(nums, pR, r)
    return pL, pR + 1


def quickSort(nums, l=-1, r=-1):
    if not nums or len(nums) < 2:
        return

    if l == -1 and r == -1:
        l = 0
        r = len(nums) - 1

    if l < r:
        index = random.randint(l, r)
        utils.swap(nums, index, r)
        p, q = _partition(nums, l, r)
        quickSort(nums, l, p)
        quickSort(nums, q, r)


@utils.clock
def easyQuickSort(nums):
    if not nums or len(nums) < 2:
        return

    def _partition(nums, le, ri):
        p = le - 1
        index = random.randint(le, ri)
        num = nums[index]
        for i in range(le, ri + 1):
            if nums[i] <= num:
                p += 1
                if i != p:
                    tmp = nums[i]
                    nums[i] = nums[p]
                    nums[p] = tmp
        return p

    def process(nums, le, ri):
        if le == ri:
            return
        q = _partition(nums, le, ri)
        if q > le:
            process(nums, le, q - 1)
        if q < ri - 1:
            process(nums, q + 1, ri)

    process(nums, 0, len(nums) - 1)
    return


def quick_sort(arr):
    # if array is empty or has only 1 element
    # it means the array is already sorted, so return it.
    if len(arr) < 2:
        return arr
    else:
        rand_index = random.randint(0, len(arr) - 1)
        pivot = arr[rand_index]
        less = []
        equal_nums = []
        greater = []

        # create less and greater array comparing with pivot
        for i in arr:
            if i < pivot:
                less.append(i)
            if i > pivot:
                greater.append(i)
            if i == pivot:
                equal_nums.append(i)

        return quick_sort(less) + equal_nums + quick_sort(greater)


@utils.clock
def wrapQuickSort(nums):
    # quickSort(nums)
    nums = quick_sort(nums)

    return


@utils.clock
def originSort(nums):
    nums.sort()
    return


def countingSort(nums, bound):
    if not nums or len(nums) < 2:
        return
    cnt = [0] * (bound + 1)
    for x in nums:
        cnt[x] += 1

    for i in range(1, bound + 1):
        cnt[i] += cnt[i - 1]
    res = [0] * len(nums)
    for i in range(len(nums)):
        res[cnt[nums[i]] - 1] = nums[i]
    return res


def radixSort(nums):
    if not nums or len(nums) < 2:
        return

    maxn = max(nums)
    maxBit = 0
    while maxn != 0:
        maxBit += 1
        maxn = maxn // 10

    bucket = [0] * len(nums)

    def getDigits(x, d):
        return (x // (10 ** (d - 1))) % 10

    for i in range(1, maxBit + 1):
        cnt = [0] * 10
        # 按key进行计数排序
        for x in nums:
            j = getDigits(x, i)
            cnt[j] += 1

        for k in range(1, 10):
            cnt[k] += cnt[k - 1]
        # 反向，为了先出现的排前面，也就发挥了第二关键字的作用 ,若要先出现的排后面，则正向
        for k in range(len(nums) - 1, -1, -1):
            j = getDigits(nums[k], i)
            bucket[cnt[j] - 1] = nums[k]
            cnt[j] -= 1
        for k in range(len(nums)):
            nums[k] = bucket[k]


class Heap:

    def __init__(self, nums):
        self.heap_size = 0
        self.heap = nums

    @staticmethod
    def swap(nums, a, b):
        if a == b:
            return
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp

    def heapInsert(self, index):
        self.heap_size += 1
        while self.heap[index] > self.heap[(index - 1) >> 1]:
            Heap.swap(self.heap, index, (index - 1) >> 1)
            index = (index - 1) >> 1

    def heapify(self, index, size):
        left = (index << 1) + 1
        right = left + 1
        while left < size:
            bigger = right if right < size and self.heap[right] > self.heap[left] else left
            bigger = bigger if self.heap[bigger] > self.heap[index] else index
            if bigger == index:
                break
            Heap.swap(self.heap, bigger, index)
            index = bigger
            left = (index << 1) + 1
            right = left + 1

    def isEmpty(self):
        return self.heap_size == 0


def heapSort(nums):
    if not nums or len(nums) < 2:
        return
    heap = Heap(nums)
    # for i in range(len(nums)):
    #     heap.heapInsert(i)
    heap.heap_size = len(nums)
    for i in range(len(nums) - 1, -1, -1):
        heap.heapify(i, len(nums))
    t = heap.heap_size
    while t > 0:
        Heap.swap(heap.heap, 0, t - 1)
        t -= 1
        heap.heapify(0, t)
    return nums


def Test():
    test_time = 20
    for i in range(test_time):
        arr1 = utils.generateArray(100, 100)
        arr2 = arr1[:]
        # easyQuickSort(arr1)
        print(utils.comparator(easyQuickSort, wrapQuickSort, arr1, arr2))


if __name__ == "__main__":
    # Test()
    nums = [35, 38, 46, 43, 52, 39, 54, 56, 56, 59, 68, 75, 84, 91, 99, 35, 38, 46, 43, 52, 39, 54, 56, 56, 59, 68, 75,
            84, 91, 99]
    # easyQuickSort(nums)
    # nums = countingSort(nums, 100)
    radixSort(nums)
    print(nums)
