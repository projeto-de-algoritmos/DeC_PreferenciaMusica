def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort_count(arr[:mid])
    right, inv_right = merge_sort_count(arr[mid:])
    merged, inv_merge = merge_count(left, right)

    return merged, inv_left + inv_right + inv_merge


def merge_count(left, right):
    merged = []
    count = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count


notas = []
for i in range(5):
    nota = int(input(f"Digite a nota da banda {i+1}: "))
    notas.append(nota)

sorted_arr, inversions = merge_sort_count(notas)
print("Sequência ordenada:", sorted_arr)
print("Número de inversões:", inversions)


