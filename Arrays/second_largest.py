def find_second_largest(arr):
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second


numbers = [10, 5, 20, 8]
print(find_second_largest(numbers))
