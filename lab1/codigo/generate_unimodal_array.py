import random

def generar_arreglo_unimodal(n, pico=None):
    if n < 3:
        raise ValueError("El tamaño del arreglo debe ser al menos 3 para ser unimodal.")
    
    if pico is None:
        pico = random.randint(1, n - 2)  # Garantiza que el pico no esté en los extremos
    
    izquierda = sorted(random.sample(range(1, n+1), pico))  # Parte creciente
    derecha = sorted(random.sample(range(1, n+1), n - pico - 1), reverse=True)  # Parte decreciente
    
    maximo = random.randint(max(izquierda) + 1, n+1)  # Asegura que sea el máximo
    arr = izquierda + [maximo] + derecha
    return arr

# Ejemplo de uso

if __name__ == "__main__":
    n = 1000
    arreglo = generar_arreglo_unimodal(n)
    print("Arreglo unimodal:", arreglo)