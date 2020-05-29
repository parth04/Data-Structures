
def findInMountainArray(target, arr) -> int:

    n = len(arr)

    if arr[0] == target:
        return 0

    max_index = findingPeak(arr, 0, n - 1)
    print("Max index {}".format(max_index))

    if max_index != -1:
        if target == arr[max_index]:
            return max_index

    res = bsearch(arr, target, 0, max_index - 1)
    if res != None:
        return res
    res1 = descsearch(arr, target, max_index + 1, n - 1)
    if res1 != None:
        return res1
    else:
        return -1



def findingPeak(mountain_arr, low, high):
    mid = (low + high) // 2
    if (mountain_arr[mid] > mountain_arr[mid + 1] and
            mountain_arr[mid] > mountain_arr[mid-1]):
        return mid
    while low <= high:
        mid = (low + high) // 2

        if (mountain_arr[mid+1] > mountain_arr[mid]):
            # return self.findingPeak(mountain_arr, mid + 1, high)
            low = mid + 1

        elif mountain_arr[mid-1] > mountain_arr[mid]:
            # return self.findingPeak(mountain_arr, low, mid - 1)
            high = mid - 1
        else:
            return mid
    return -1


def bsearch(arr, x, low, high):
    while low <= high:
        mid = (low + high) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return bsearch(arr, x, mid + 1, high)

        elif x < arr[mid]:
            return bsearch(arr, x, low, mid - 1)

def descsearch(arr, x, low, high):
    while low <= high:
        mid = (low + high) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return bsearch(arr, x, mid + 1, high)

        else:
            return bsearch(arr, x, low, mid - 1)

arr = [1,2,3,4,3,1]
target =0
x=findInMountainArray(target, arr)
print ("x = {}".format(x))
