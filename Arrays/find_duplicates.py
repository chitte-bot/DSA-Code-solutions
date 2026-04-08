def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


numbers = [1, 2, 3, 2, 4, 1]

print("Duplicates:", find_duplicates(numbers))
