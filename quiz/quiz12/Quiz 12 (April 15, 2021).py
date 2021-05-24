def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        switch = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                switch = True
        if not switch:
            break
    return arr


if __name__ == '__main__':
    arr=[2,4,2,1,7,5,-1,0]
    print(bubble_sort(arr))