from parse import *


def getData():
    # path de los archivos
    PATH = "../gem5/se_results/"
    FILENAME = "/stats.txt"

    # arreglo de todas las variables modificadas en los benchmarks
    variables_array = ["_btb_entries_Tournament",
                       "_cache_line_size",
                       "_Dcache_assoc",
                       "_Dcache_size",
                       "_global_predictor_size_BiMode",
                       "_global_predictor_size_Tournament",
                       "_Icache_assoc",
                       "_Icache_size",
                       "_local_predictor_size_Local",
                       "_local_predictor_size_Tournament"]

    # arreglos de los valores para cada variable
    values_btb_entries_Tournament = ["256","512","1024"]
    values_cache_line_size = ["32","64"]
    values_Dcache_assoc = ["2","4","8","16"]
    values_Dcache_size = ["16kB","32kB","64kB","128kB"]
    values_global_predictor_size_BiMode = ["256","512","1024","2048","4096"]
    values_global_predictor_size_Tournament = ["256","512","1024","2048","4096"]
    values_Icache_assoc = ["2","4","8","16"]
    values_Icache_size = ["16kB","32kB","64kB","128kB"]
    values_local_predictor_size_Local = ["256","512","1024","2048","4096"]
    values_local_predictor_size_Tournament = ["256","512","1024","2048","4096"]



    # arreglo de todos los nombres de los benchmarks
    benchmarks_array = ["FloatMM","IntMM","Perm","Queens","Towers","Treesort"]
    
    # numero de benchmarks
    n = len(benchmarks_array)
    
    # numero de variables
    n_variables_array = len(variables_array)
    
    # numero de pruebas realizadas por variable
    n_btb_entries_Tournament = len(values_btb_entries_Tournament)
    n_cache_line_size = len(values_cache_line_size)
    n_Dcache_assoc = len(values_Dcache_assoc)
    n_Dcache_size = len(values_Dcache_size)
    n_global_predictor_size_BiMode = len(values_global_predictor_size_BiMode)
    n_global_predictor_size_Tournament = len(values_global_predictor_size_Tournament)
    n_Icache_assoc = len(values_Icache_assoc)
    n_Icache_size = len(values_Icache_size)
    n_local_predictor_size_Local = len(values_local_predictor_size_Local)
    n_local_predictor_size_Tournament = len(values_local_predictor_size_Tournament)

    # arreglo con los resultados de todas las matrices
    results_array = []
    for i in range(0,n):
        for j in range(0,n_variables_array):
            if variables_array[j] == "_btb_entries_Tournament":
                for k in range(0,n_btb_entries_Tournament):
                    m_file_name = runParser(PATH + benchmarks_array[i] + variables_array[j] + values_btb_entries_Tournament[k] + FILENAME)
                    results_array.append(m_file_name)
            elif variables_array[j] == "_cache_line_size":
                for k in range(0,n_cache_line_size):
                    m_file_name = runParser(PATH + benchmarks_array[i] + variables_array[j] + values_cache_line_size[k] + FILENAME)
                    results_array.append(m_file_name)
            elif variables_array[j] == "_Dcache_assoc":
                for k in range(0,n_Dcache_assoc):
                    m_file_name = runParser(PATH + benchmarks_array[i] + variables_array[j] + values_Dcache_assoc[k] + FILENAME)
                    results_array.append(m_file_name)
            elif variables_array[j] == "_Dcache_size":
                for k in range(0,n_Dcache_size):
                    m_file_name = runParser(PATH + benchmarks_array[i] + variables_array[j] + values_Dcache_size[k] + FILENAME)
                    results_array.append(m_file_name)
            elif variables_array[j] == "_global_predictor_size_BiMode":
                for k in range(0,n_global_predictor_size_BiMode):
                    m_file_name = runParser(PATH + benchmarks_array[i] + variables_array[j] + values_global_predictor_size_BiMode[k] + FILENAME)
                    results_array.append(m_file_name)
            elif variables_array[j] == "_global_predictor_size_Tournament":
                for k in range(0,n_global_predictor_size_Tournament):
                    m_file_name = runParser(PATH + benchmarks_array[i] + variables_array[j] + values_global_predictor_size_Tournament[k] + FILENAME)
                    results_array.append(m_file_name)
            elif variables_array[j] == "_Icache_assoc":
                for k in range(0,n_Icache_assoc):
                    m_file_name = runParser(PATH + benchmarks_array[i] + variables_array[j] + values_Icache_assoc[k] + FILENAME)
                    results_array.append(m_file_name)
            elif variables_array[j] == "_Icache_size":
                for k in range(0,n_Icache_size):
                    m_file_name = runParser(PATH + benchmarks_array[i] + variables_array[j] + values_Icache_size[k] + FILENAME)
                    results_array.append(m_file_name)
            elif variables_array[j] == "_local_predictor_size_Local":
                for k in range(0,n_local_predictor_size_Local):
                    m_file_name = runParser(PATH + benchmarks_array[i] + variables_array[j] + values_local_predictor_size_Local[k] + FILENAME)
                    results_array.append(m_file_name)
            elif variables_array[j] == "_local_predictor_size_Tournament":
                for k in range(0,n_local_predictor_size_Tournament):
                    m_file_name = runParser(PATH + benchmarks_array[i] + variables_array[j] + values_local_predictor_size_Tournament[k] + FILENAME)
                    results_array.append(m_file_name)
    print(results_array[0])


def main():
    getData()

main()