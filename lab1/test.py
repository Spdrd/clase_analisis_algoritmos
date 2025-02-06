import time
import csv

import naive_unimodal_search
import binary_unimodal_search
from generate_unimodal_array import generar_arreglo_unimodal

def mesure_time(func, arr:list):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

def test():
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['n', 'naive', 'binary'])
        for n in [100, 200, 300, 400, 500, 600]:
            print(f"n: {n}")
            for j in range(10):
                arr = generar_arreglo_unimodal(n)
                naive_time = mesure_time(naive_unimodal_search.run, arr)
                binary_time = mesure_time(binary_unimodal_search.run, arr)
                writer.writerow([n, naive_time, binary_time])
                del arr


if __name__ == "__main__":
    test()