
from generate_unimodal_array import generar_arreglo_unimodal

def naive(arr: list, start = 0, end = None):
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            print(f"naive:: i: {i} val: {arr[i]}")
            return i
    return -1

def run(arr: list):
    naive(arr)


if __name__ == "__main__":
    run(100, [1,2,3])