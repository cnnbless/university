def input_array(size):
    arr = []
    print(f"Введіть {size} елементів масиву:")
    for i in range(size):
        arr.append(int(input()))
    return arr

def find_max_element(arr):
    max_el = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_el]:
            max_el = i
    return max_el

def print_array(arr):
    print(" ".join(map(str, arr)))

def main():
    size1 = int(input("Введіть розмір першого масиву: "))
    size2 = int(input("Введіть розмір другого масиву: "))

    arr1 = input_array(size1)
    arr2 = input_array(size2)

    max_el1 = find_max_element(arr1)
    max_el2 = find_max_element(arr2)

    arr1[max_el1], arr2[max_el2] = arr2[max_el2], arr1[max_el1]

    print("Масив 1:", end=" ")
    print_array(arr1)

    print("Масив 2:", end=" ")
    print_array(arr2)

if __name__ == "__main__":
    main()
