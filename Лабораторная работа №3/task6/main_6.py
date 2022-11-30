list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_max = 0
number_max = list_numbers[index_max]

for i, number_current in enumerate(list_numbers):
    number_max = list_numbers[index_max]
    if number_current >= number_max:
        index_max = i
        number_max = list_numbers[index_max]

list_numbers[index_max], list_numbers[len(list_numbers)-1] = list_numbers[len(list_numbers)-1], list_numbers[index_max]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
