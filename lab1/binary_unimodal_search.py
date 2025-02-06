from generate_unimodal_array import generar_arreglo_unimodal

def binary(arr: list):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            print(f"binary:: i: {mid} val: {arr[mid]}")
            return mid
        elif arr[mid] < arr[mid - 1]:
            end = mid - 1
        else:
            start = mid + 1
    return -1  # Si no se encuentra un pico, aunque eso no debería ocurrir en un arreglo adecuado


def run(arr: list):
    binary(arr)
    
if __name__ == "__main__":
    run(100, [1,2,3])