from django.shortcuts import render, HttpResponse
from random import randint


def home(request):
    return render(request, 'visualizer/home.html')


def update_size(request, n_bars):
    global arr
    arr = []

    for _ in range(n_bars):
        arr.append(randint(100, 550))

    return HttpResponse([arr])


def bubblesort(request):
    global transitions
    transitions = []
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                transitions.append([j, j+1])
            else:
                transitions.append([j])

    return HttpResponse([transitions])


def quicksort(request):
    global transitions
    transitions = []
    quick_sort(arr, 0, len(arr)-1)
    return HttpResponse([transitions])


def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):

        transitions.append([j])
        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            transitions.append([i, j])

    arr[i+1], arr[high] = arr[high], arr[i+1]
    transitions.append([i+1, high])
    return (i+1)


def mergesort(request):
    global transitions
    transitions = []
    merge_sort(arr, 0, len(arr)-1)
    print(transitions)
    return HttpResponse([transitions])


def merge_sort(arr, l, r):

    if (l < r):

        m = l + (r - l) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

        merge(arr, l, m, r)


def merge(arr, start, mid, end):
    start2 = mid + 1

    if (arr[mid] <= arr[start2]):
        return

    while (start <= mid and start2 <= end):

        if (arr[start] <= arr[start2]):
            start += 1

        else:
            value = arr[start2]
            index = start2

            while (index != start):
                arr[index] = arr[index - 1]
                transitions.append([index, index - 1])
                index -= 1

            arr[start] = value

            start += 1
            mid += 1
            start2 += 1


def selectionsort(request):
    global transitions
    transitions = []

    for i in range(len(arr)):

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            transitions.append([j])

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        transitions.append([i, min_idx])

    return HttpResponse([transitions])


def insertionsort(request):
    global transitions
    transitions = []

    for i in range(1, len(arr)):
        transitions.append([i])
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            transitions.append([j])
            arr[j+1] = arr[j]
            transitions.append([j+1, j])
            j -= 1
        arr[j+1] = key

    return HttpResponse([transitions])
