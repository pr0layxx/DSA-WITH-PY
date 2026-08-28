arr=[1,2,3]
def isSorted(arr):
    first= arr[0]
    for nums in arr:
        if nums < first:
            return False
        else:
            first = nums
            
    return True
  
print(isSorted(arr))