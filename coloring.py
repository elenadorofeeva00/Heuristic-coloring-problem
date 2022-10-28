import time
import csv

def ReadGraphFile(filename):
        with open(filename) as file:
            fin = file.readlines()
        vertices = 0
        edges = 0
        for i in range(0, len(fin)):
            lst = fin[i].split()

            if lst[0] == 'c':
                continue

            if lst[0] == 'p':
                vertices = int(lst[2])
                edges = int(lst[3])
                neighbour_sets = [set() for i in range(0, vertices)]
                colors = [0 for i in range(0, vertices)]
            
            else:
                start = int(lst[1])
                finish = int(lst[2])
                
                neighbour_sets[start - 1].add(finish - 1)
                neighbour_sets[finish - 1].add(start - 1)
                
        return neighbour_sets, colors
    
def Check(neighbour_sets, colors):
        
        for i in range(0, len(neighbour_sets)):
            if colors[i] == 0:
                print("Vertex ", i + 1," is not colored\n")
                return False

            for neighbour in neighbour_sets[i]:
                if colors[neighbour] == colors[i]:
                    print("Neighbour vertices ", i + 1, ", ", neighbour + 1, " have the same color\n")
                    return False

        return True

def color_nodes_2(graph):
    color_map = {} #словарь с цветами, ключ - вершина, значение - цвет
 
    #проходим по каждой вершине в списке, отсортированном по убыванию степеней вершин
    for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
        neighbour_colors = set(color_map.get(neigh) for neigh in graph[node]) #множество цветов соседей вершины node
        for color in range(1, len(graph)): #присваиваем вершине первый свободный цвет
            if color not in neighbour_colors:
                color_map[node] = color
                break
    return color_map


files = ["myciel3.col", 
         "myciel7.col", 
         "latin_square_10.col.txt", 
         "school1.col", 
         "school1_nsh.col",
         "mulsol.i.1.col",
         "inithx.i.1.col", 
         "anna.col", 
         "huck.col", 
         "jean.col",
         "miles1000.col",
         "miles1500.col",
         "le450_5a.col",
         "le450_15b.col",
         "queen11_11.col"]

with open("colors_2.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
    file_writer.writerow(["Instance", "Colors", "Time (sec)"])
    
    print("Instance; Colors; Time (sec)\n")
    
    for file in files:
        neighbour_sets, colors = ReadGraphFile("C:\\Users\\Елена\\Documents\\" + file)
        
        graph = {}
        
        for i in range(len(neighbour_sets)):
            graph[i] = neighbour_sets[i]
            
        start = time.time()
        
        colors = color_nodes_2(graph)
        maxcolor = max(colors.values())
        
        check = Check(neighbour_sets, colors)
        
        if check == False:
            print("*** WARNING: incorrect coloring: ***\n")
        finish = time.time()
        file_writer.writerow([file, maxcolor, round((finish - start), 3), "\n"])
        print("Instance: ", file, ";", "Colors: ", maxcolor, ";", "Time: ", round((finish - start), 3), "\n")

        print('---------------------------------')
            
w_file.close()

