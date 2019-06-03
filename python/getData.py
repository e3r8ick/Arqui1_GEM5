from parse import *
from plot import *

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
benchmarks_array = ["IntMM","Perm","Queens","Towers","Treesort"]

def getData():    
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
    results_array_FloatMM = []
    results_array_IntMM = []
    results_array_Perm = []
    results_array_Queens = []
    results_array_Towers = []
    results_array_Treesort = []
    # result preliminar
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
        if i == 0:
            results_array_IntMM.append(results_array)
            results_array = [] 
        elif i == 1:
            results_array_Perm.append(results_array)
            results_array = []
        elif i == 2:
            results_array_Queens.append(results_array)
            results_array = []
        elif i == 3:
            results_array_Towers.append(results_array)
            results_array = []
        elif i == 4:
            results_array_Treesort.append(results_array)
            results_array = []
    results_array = {"IntMM":results_array_IntMM,
                     "Perm":results_array_Perm,
                     "Queens":results_array_Queens,
                     "Towers":results_array_Towers,
                     "Treesort":results_array_Treesort}
    return results_array

def infoSplitter(info_dic):
    # get de las matrices de cada benchmark
    IntMM = info_dic['IntMM'][0]
    Perm = info_dic['Perm'][0]
    Queens = info_dic['Queens'][0]
    Towers = info_dic['Towers'][0]
    Treesort = info_dic['Treesort'][0]

    # tamaño de la cantidad de pruebas, todos son iguales
    n = len(IntMM)
    n_tags = len(getTags())

    global variables_array
    n_parametros = len(variables_array)

    global benchmarks_array

    # escoge la variable para analizar de values vector (tags)
    for i in range(0,n_tags):
        # escoge tamaño del benchmarks (varaibles)
        vector_graf = []
        # btb entries
        for k in range(0,3):
            intmm = float(IntMM[k][i][1])
            perm = float(Perm[k][i][1])
            queens = float(Queens[k][i][1])
            towers = float(Towers[k][i][1])
            treesort = float(Treesort[k][i][1])
            vector_graf.append([intmm,perm,queens,towers,treesort])
        groupBarPlot("Tournament btb entries",vector_graf,getTags()[i],benchmarks_array,["256","512","1024"])

        vector_graf = []

        # chache line size
        for k in range(3,5):
            intmm = float(IntMM[k][i][1])
            perm = float(Perm[k][i][1])
            queens = float(Queens[k][i][1])
            towers = float(Towers[k][i][1])
            treesort = float(Treesort[k][i][1])
            vector_graf.append([intmm,perm,queens,towers,treesort])
        groupBarPlot("Cache Line Size",vector_graf,getTags()[i],benchmarks_array,["32","64"])

        vector_graf = []

        # Dcache assoc
        for k in range(5,9):
            intmm = float(IntMM[k][i][1])
            perm = float(Perm[k][i][1])
            queens = float(Queens[k][i][1])
            towers = float(Towers[k][i][1])
            treesort = float(Treesort[k][i][1])
            vector_graf.append([intmm,perm,queens,towers,treesort])
        groupBarPlot("DCache Assoc HOLIS",vector_graf,getTags()[i],benchmarks_array,["2","4","8","16"])

        vector_graf = []

        # Dcache size
        for k in range(9,13):
            intmm = float(IntMM[k][i][1])
            perm = float(Perm[k][i][1])
            queens = float(Queens[k][i][1])
            towers = float(Towers[k][i][1])
            treesort = float(Treesort[k][i][1])
            vector_graf.append([intmm,perm,queens,towers,treesort])
        groupBarPlot("DCache Size",vector_graf,getTags()[i],benchmarks_array,["16Kb","32kB","64kB","128kB"])

        vector_graf = []

        # global predictor size BiMode
        for k in range(13,18):
            intmm = float(IntMM[k][i][1])
            perm = float(Perm[k][i][1])
            queens = float(Queens[k][i][1])
            towers = float(Towers[k][i][1])
            treesort = float(Treesort[k][i][1])
            vector_graf.append([intmm,perm,queens,towers,treesort])
        #print(vector_graf)
        groupBarPlot("Global predictor Size BiMode",vector_graf,getTags()[i],benchmarks_array,["256","512","1024","2048","4096"])

        vector_graf = []

        # global predictor size Tournament
        for k in range(18,23):
            intmm = float(IntMM[k][i][1])
            perm = float(Perm[k][i][1])
            queens = float(Queens[k][i][1])
            towers = float(Towers[k][i][1])
            treesort = float(Treesort[k][i][1])
            vector_graf.append([intmm,perm,queens,towers,treesort])
        #print(vector_graf)
        groupBarPlot("Global predictor Size Tournament",vector_graf,getTags()[i],benchmarks_array,["256","512","1024","2048","4096"])

        vector_graf = []

        # Dcache assoc pero talvez, solo talvez nmo sea eso, sino Icache
        for k in range(23,27):
            intmm = float(IntMM[k][i][1])
            perm = float(Perm[k][i][1])
            queens = float(Queens[k][i][1])
            towers = float(Towers[k][i][1])
            treesort = float(Treesort[k][i][1])
            vector_graf.append([intmm,perm,queens,towers,treesort])
        #print(vector_graf)
        groupBarPlot("Dcache Assoc",vector_graf,getTags()[i],benchmarks_array,["2","4","8","16"])

        vector_graf = []

        # Icache size
        for k in range(27,31):
            intmm = float(IntMM[k][i][1])
            perm = float(Perm[k][i][1])
            queens = float(Queens[k][i][1])
            towers = float(Towers[k][i][1])
            treesort = float(Treesort[k][i][1])
            vector_graf.append([intmm,perm,queens,towers,treesort])
        #print(vector_graf)
        groupBarPlot("I cache Size",vector_graf,getTags()[i],benchmarks_array,["16kB","32kB","64kB","128kB"])

        vector_graf = []


        # local predictor size local
        for k in range(31,36):
            intmm = float(IntMM[k][i][1])
            perm = float(Perm[k][i][1])
            queens = float(Queens[k][i][1])
            towers = float(Towers[k][i][1])
            treesort = float(Treesort[k][i][1])
            vector_graf.append([intmm,perm,queens,towers,treesort])
        #print(vector_graf)
        groupBarPlot("Local Predictor Size Local",vector_graf,getTags()[i],benchmarks_array,["256","512","1024","2048","4096"])

        vector_graf = []

        # local predictor size tournament
        for k in range(36,41):
            intmm = float(IntMM[k][i][1])
            perm = float(Perm[k][i][1])
            queens = float(Queens[k][i][1])
            towers = float(Towers[k][i][1])
            treesort = float(Treesort[k][i][1])
            vector_graf.append([intmm,perm,queens,towers,treesort])
        #print(vector_graf)
        groupBarPlot("Local Predictor Size Tournament",vector_graf,getTags()[i],benchmarks_array,["256","512","1024","2048","4096"])

                


# result[nombre benchmark][diccionario:0][parametro][tag][valor:1]


def main():
    results = getData()
    infoSplitter(results)
main()