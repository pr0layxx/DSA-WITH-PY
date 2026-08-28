arr = [12,42,1112,9,00,]
def largest_element(arr):
    largest = arr[0]
    for number in arr:
        if number > largest:
            largest= number
    return largest


print(largest_element(arr))

    