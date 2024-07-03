import timeit
from prim import runner_prim
from boruvka import runner_boruvka
from reverse_delete import runner_r
# Funciones de tiempo para cada algoritmo
def time_prim():
    runner_prim()

def time_boruvka():
    runner_boruvka()

def time_reverse_delete():
    runner_r()

# Medición de tiempos de ejecución
t_prim = timeit.timeit(time_prim, number=1)
t_boruvka = timeit.timeit(time_boruvka, number=1)
t_reverse_delete = timeit.timeit(time_reverse_delete, number=1)

# Resultados
print(f"Tiempo de ejecución de Prim: {t_prim} segundos")
print(f"Tiempo de ejecución de Borůvka: {t_boruvka} segundos")
print(f"Tiempo de ejecución de Reverse-Delete: {t_reverse_delete} segundos")
