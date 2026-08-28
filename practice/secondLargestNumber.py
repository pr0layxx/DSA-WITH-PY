arr = [10,32,43,53,23,54,886]

def second_largest_number(arr):
    largest = arr[0]
    second_largest= arr[1]
    for number in arr:
        if number > largest:
            second_largest= largest
            largest = number
        elif number > second_largest:
            second_largest = number
    return second_largest
            

        
        

print(second_largest_number(arr))