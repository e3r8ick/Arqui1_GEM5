import os

def Oscar_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/Oscar_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Oscar")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Oscar_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Oscar")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Oscar_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Oscar")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Oscar_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Oscar")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Oscar_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Oscar")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Oscar_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Oscar")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Oscar_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Oscar")
        local_predictor_size = local_predictor_size * 2


def Treesort_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/Treesort_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Treesort")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Treesort_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Treesort")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Treesort_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Treesort")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Treesort_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Treesort")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Treesort_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Treesort")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Treesort_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Treesort")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Treesort_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Treesort")
        local_predictor_size = local_predictor_size * 2

def Bubblesort_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/Bubblesort_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Bubblesort")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Bubblesort_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Bubblesort")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Bubblesort_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Bubblesort")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Bubblesort_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Bubblesort")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Bubblesort_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Bubblesort")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Bubblesort_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Bubblesort")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Bubblesort_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Bubblesort")
        local_predictor_size = local_predictor_size * 2

def FloatMM_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/FloatMM_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/FloatMM")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/FloatMM_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/FloatMM")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/FloatMM_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/FloatMM")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/FloatMM_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/FloatMM")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/FloatMM_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/FloatMM")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/FloatMM_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/FloatMM")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/FloatMM_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/FloatMM")
        local_predictor_size = local_predictor_size * 2

def IntMM_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/IntMM_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/IntMM")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/IntMM_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/IntMM")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/IntMM_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/IntMM")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/IntMM_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/IntMM")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/IntMM_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/IntMM")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/IntMM_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/IntMM")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/IntMM_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/IntMM")
        local_predictor_size = local_predictor_size * 2

def Perm_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/Perm_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Perm")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Perm_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Perm")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Perm_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Perm")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Perm_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Perm")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Perm_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Perm")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Perm_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Perm")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Perm_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Perm")
        local_predictor_size = local_predictor_size * 2

def Puzzle_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/Puzzle_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Puzzle")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Puzzle_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Puzzle")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Puzzle_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Puzzle")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Puzzle_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Puzzle")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Puzzle_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Puzzle")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Puzzle_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Puzzle")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Puzzle_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Puzzle")
        local_predictor_size = local_predictor_size * 2


def Towers_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/Towers_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Towers")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Towers_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Towers")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Towers_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Towers")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Towers_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Towers")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Towers_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Towers")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Towers_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Towers")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Towers_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Towers")
        local_predictor_size = local_predictor_size * 2


def RealMM_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/RealMM_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/RealMM")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/RealMM_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/RealMM")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/RealMM_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/RealMM")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/RealMM_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/RealMM")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/RealMM_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/RealMM")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/RealMM_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/RealMM")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/RealMM_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/RealMM")
        local_predictor_size = local_predictor_size * 2


def Quicksort_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/Quicksort_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Quicksort")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Quicksort_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Quicksort")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Quicksort_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Quicksort")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Quicksort_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Quicksort")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Quicksort_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Quicksort")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Quicksort_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Quicksort")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Quicksort_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Quicksort")
        local_predictor_size = local_predictor_size * 2


def Queens_benchmark():
    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc = "8"
    Dcahce_assoc = "16"
    branch_predictor= "LocalBP"
    btb_entries = 1024
    global_predictor_size = 4096
    local_predictor_size = 1024
    choice_predictor_size = 4096
    cache_line_size = 64
    while cache_line_size < 2048:
        os.system("./build/ARM/gem5.opt -d se_results/Queens_cache_line_size"+str(cache_line_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Queens")
        cache_line_size = cache_line_size * 2

    cache_line_size = 64
    Icache_int = 16
    while Icache_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Queens_Icache_size"+Icache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Queens")
        Icache_int = Icache_int * 2
        Icache_size = str(Icache_int)+"kB"

    Dcahce_int = 16
    while Dcahce_int < 256:
        os.system("./build/ARM/gem5.opt -d se_results/Queens_Dcache_size"+Dcache_size+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Queens")
        Dcahce_int = Dcahce_int * 2
        Dcache_size = str(Dcahce_int)+"kB"

    Icache_size = "16kB"
    Dcache_size = "32kB"
    Icache_assoc_int = 1
    while Icache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Queens_Icache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Queens")
        Icache_assoc_int = Icache_assoc_int * 2
        Icache_assoc = str(Icache_assoc_int)

    Dcache_assoc_int = 1
    while Dcache_assoc_int < 64:
        os.system("./build/ARM/gem5.opt -d se_results/Queens_Dcache_assoc"+Icache_assoc+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Queens")
        Dcache_assoc_int = Dcache_assoc_int * 2
        Dcache_assoc = str(Dcache_assoc_int)

    Icache_assoc = "8"
    Dcahce_assoc = "16"
    global_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Queens_global_predictor_size"+str(global_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Queens")
        global_predictor_size = global_predictor_size * 2

    global_predictor_size = 4096
    local_predictor_size = 256
    while global_predictor_size < 8192:
        os.system("./build/ARM/gem5.opt -d se_results/Queens_local_predictor_size"+str(local_predictor_size)+" configs/example/arm/starter_se.py \--cpu=hpi --Icache-size='"+Icache_size+"' --Dcache-size='"+Dcache_size+"' --cache-line-size="+str(cache_line_size)+" --Icache-assoc=8 --Dcache-assoc="+Icache_assoc+" --branch-predictor='"+branch_predictor+"' --BTBEntries="+str(btb_entries)+" --local-predictor-size="+str(local_predictor_size)+" --global-predictor-size="+str(global_predictor_size)+" --choice-predictor-size="+str(choice_predictor_size)+" /home/e3r8ick/Arqui1/Proyecto2/gem5/se-benchmarks/Queens")
        local_predictor_size = local_predictor_size * 2

def main_benchmark():
    Oscar_benchmark()
    Treesort_benchmark()
    Bubblesort_benchmark()
    FloatMM_benchmark()
    IntMM_benchmark()
    Perm_benchmark()
    Puzzle_benchmark()
    Towers_benchmark()
    RealMM_benchmark()
    Quicksort_benchmark()
    Queens_benchmark()

main_benchmark()
