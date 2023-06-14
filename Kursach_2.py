import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# # Определяем список элементов СБИС
# elements = [i for i in range(20)]


# # Определяем координаты элементов СБИС
# x_coords = np.random.randint(0, 10, size=len(elements))
# y_coords = np.random.randint(0, 10, size=len(elements))
# tx_coords = []
# ty_coords = []
# # for i in range(len(elements)):
# #     print(i,"...", x_coords[i], y_coords[i])


# x_mean = np.mean(x_coords)
# y_mean = np.mean(y_coords)
    


# # Создаем граф и добавляем вершины
# G = nx.Graph()
# for i in range(len(elements)):
#     G.add_node(i, pos=(x_coords[i], y_coords[i]))
           
# Добавяем дополнительные точки соединений 
class Make_Snode:
    def 
Mnode(G,x_coords,y_coords,elements,x_mean,y_mean,tx_coords,ty_coords):
        for i in range(len(elements)):
            do = 0
            dis = 100
            for iii in range(len(elements)):
                if i != iii:
                    x1, y1 = x_coords[i], y_coords[i]
                    x2, y2 = x_coords[iii], y_coords[iii]
                    d = abs(x1 - x2) + abs(y1 - y2)
                    if d <= dis  and (abs(x1 - x2) + abs(y1 - y2) != 0):
                        dis = d
                        do = iii
            dx = abs(x1-x_mean)
            dy = abs(y1-y_mean)
            if dx <= dy:
                tx_coords.append(x1)
                ty_coords.append(y_coords[do])
                G.add_node(len(x_coords)+i,pos=(x1,y_coords[do]))
            else:
                tx_coords.append(x_coords[do])
                ty_coords.append(y1)
                G.add_node(len(x_coords)+i,pos=(x_coords[do],y1))


        
            
# Удаляем повтор точки
class del_nodes:
    def del_xx_node(G,x_coords,y_coords,tx_coords,ty_coords):
        for i in range(len(x_coords)):
            for j in range(len(tx_coords)):
                if tx_coords[j] == x_coords[i] and ty_coords[j] == y_coords[i]:
                    if G.has_node(len(x_coords)+j):
                        G.remove_node(len(x_coords)+j)
                        # print("Уд 1.", tx_coords[i], ty_coords[i])
    def del_xtx_node(G,x_coords,tx_coords,ty_coords):
        for i in range(len(tx_coords)-1,-1,-1):
            for j in range(len(tx_coords)):
                if i != j:
                    if tx_coords[i] == tx_coords[j] and ty_coords[i] == ty_coords[j]:
                        if G.has_node(len(x_coords)+i):
                            G.remove_node(len(x_coords)+i)
                            # print("Уд 1.", tx_coords[i], ty_coords[i])


#Добавлеv ребра
class Make_edges:  
    def make_xx_edge(G,x_coords,y_coords):
        for i in range(len(x_coords)):
            for j in range(len(x_coords)):
                if (x_coords[i] == x_coords[j] or y_coords[i] == y_coords[j]):
                    G.add_edge(i, j, weight= (abs(x_coords[i] - x_coords[j]) + 
abs(y_coords[i] - y_coords[j])))
    def make_xtx_edge(G,x_coords,y_coords,tx_coords,ty_coords):
        for i in range(len(tx_coords)):
            for j in range(len(x_coords)):
                if (tx_coords[i] == x_coords[j] or ty_coords[i] == y_coords[j]):
                    G.add_edge(len(x_coords)+i, j, weight=(abs(tx_coords[i] - 
x_coords[j]) + abs(ty_coords[i] - y_coords[j])))
    def make_txx_edge(G,x_coords,y_coords,tx_coords,ty_coords):
        for i in range(len(tx_coords)-1,-1,-1):
            for j in range(len(x_coords)-1,-1,-1):
                if (tx_coords[i] == x_coords[j] or ty_coords[i] == y_coords[j]):
                    G.add_edge(len(x_coords)+i, j, weight=(abs(tx_coords[i] - 
x_coords[j]) + abs(ty_coords[i] - y_coords[j])))
    def make_txtx_edge(G,x_coords,tx_coords,ty_coords):
        for i in range(len(tx_coords)):
            for j in range(len(tx_coords)):
                if (tx_coords[i] == tx_coords[j] or ty_coords[i] == ty_coords[j]) and i != 
j:
                    G.add_edge(len(x_coords)+i, len(x_coords)+j, 
weight=(abs(tx_coords[i] - tx_coords[j]) + abs(ty_coords[i] - ty_coords[j])))
        
# Все ребра с точкой i
# for i,j in list(G.edges()):
#     if i == len(x_coords)+len(tx_coords) or j == len(x_coords)+len(tx_coords)-1:
#         print(i,j,".................")
#     elif j == len(x_coords)+len(tx_coords) or j == len(x_coords)+len(tx_coords)-
1:
#         print(i,j,".................")


# # Строим кратчайшее покрывающее дерево
# T = nx.minimum_spanning_tree(G)


# # Создаем матрицу смежности
# n = len(x_coords)+len(tx_coords)
# sss = np.zeros((n,n), dtype=int) 
# for i in range(n):
#     for j in range(n):
#         if T.has_edge(i,j):
#             sss[i][j] = sss[i][j] + 1




# for i in range(len(sss)):
#     print(i,"...", sss[i])


# # # Удаляем лишние точки
class del_node2:
    def delnode(T,x_coords,tx_coords,n,sss):
        for i in range(len(tx_coords)+len(x_coords)-1, len(x_coords)-1,-1):
            # print(i,"...", sum(sss[i]))
            if sum(sss[i]) <= 1:
                for g in range(len(T.edges())):
                    if T.has_edge(i,g):
                        T.remove_edge(i,g)
                    elif T.has_edge(g,i):
                        T.remove_edge(g,i)
                T.remove_node(i) 
                # print("Уд 2.", tx_coords[i-len(x_coords)], ty_coords[i-len(x_coords)])     
                for j in range(n-1,-1,-1):
                    sss[i][j] = "0" 


class Prinr_weight:
    def printer(T):
        total_weight = 0
        for u, v, attrs in T.edges.data():
            total_weight += attrs['weight']
        print("Вес получившейся трассы = ", total_weight)


# d1 = []
# d2 = np.array([0])
# d3 = np.array([i for i in range(len(T.nodes()))])
# print(d3)
# if nx.is_tree(T):
#     print('Граф является деревом')
# else:
#     print('Граф не является деревом')    
#     for edge in T.edges:
#         d1.append(edge)
#     print("d1 = ",d1)
#     for i in range(10):
#         for i,j in d1:
#             for h in d2:
#                 if i == h:
#                     d2 = np.append(d2,j)
#                     d2 = np.unique(d2)
#                 elif j == h:
#                     d2 = np.append(d2,i)
#                     d2 = np.unique(d2)
#     print(d2)
#     diff_arr = np.setdiff1d(d3, d2)
#     print(diff_arr)
#     for i in d2:
#         do = 0
#         ot = 0
#         dis = 100
#         for iii in d3:
#             if i < len(x_coords) and iii < len(x_coords):
#                 x1, y1 = x_coords[i], y_coords[i]
#                 x2, y2 = x_coords[iii], y_coords[iii]
#             if i < len(x_coords) and iii >= len(x_coords):
#                 x1, y1 = x_coords[i], y_coords[i]
#                 x2, y2 = tx_coords[iii-len(x_coords)], ty_coords[iii-len(x_coords)]
#             if i >= len(x_coords) and iii < len(x_coords):
#                 x1, y1 = tx_coords[i-len(x_coords)], ty_coords[i-len(x_coords)]
#                 x2, y2 = x_coords[iii], y_coords[iii]
#             if i >= len(x_coords) and iii >= len(x_coords):
#                 x1, y1 = tx_coords[i-len(x_coords)], ty_coords[i-len(x_coords)]
#                 x2, y2 = tx_coords[iii-len(x_coords)], ty_coords[iii-len(x_coords)]
#             d = abs(x1 - x2) + abs(y1 - y2)
#             if d <= dis  and (abs(x1 - x2) + abs(y1 - y2) != 0):
#                 dis = d
#                 do = iii
#                 ot = i
#         print(i,do)  
#     dx = abs(x1-x_mean)
#     dy = abs(y1-y_mean)
#     if dx <= dy and do < len(x_coords):
#         tx_coords.append(x1)
#         ty_coords.append(y_coords[do])
#         T.add_node(len(x_coords)+len(tx_coords)+1,pos=(x1,y_coords[do]))
#         print("1",x1,y_coords[do])
#     elif dx <= dy and do >= len(x_coords):
#         tx_coords.append(x1)
#         ty_coords.append(ty_coords[do-len(x_coords)])
#         T.add_node(len(x_coords)+len(tx_coords)+1,pos=(x1,ty_coords[do-
len(x_coords)]))
#         print("2",x1,ty_coords[do-len(x_coords)])
#     elif dx > dy and do >= len(x_coords):
#         tx_coords.append(tx_coords[do-len(x_coords)])
#         ty_coords.append(y1)
#         T.add_node(len(x_coords)+len(tx_coords)+1,pos=(tx_coords[do-
len(x_coords)],y1))
#         print("3",tx_coords[do-len(x_coords)],2)
#     elif dx > dy and do < len(x_coords):
#         tx_coords.append(x_coords[do])
#         ty_coords.append(y1)
#         T.add_node(len(x_coords)+len(tx_coords)+1,pos=(x_coords[do],y1))
#         print("4",x_coords[do],y1)
    
    # print(T.node(len(x_coords)+len(tx_coords)+1))


#   T = nx.minimum_spanning_tree(T)     
     
    
# for edge in T.edges:
#     print(edge)   
    
# Отображаем элементы и связи на графике
class Print_res:
    def printer(T,x_coords,y_coords, elements,tx_coords,ty_coords):
        fig, ax = plt.subplots()
        for i in range(len(elements)):
            ax.scatter(x_coords[i], y_coords[i], marker='s', s=200, c = '#d62728')
        for g in range(len(ty_coords)):
            ax.scatter(tx_coords[g], ty_coords[g], marker='s', s=20, c = '#1f77b4')
        for (i, j) in T.edges():
            if j < len(x_coords) and i < len(x_coords):
                x1, y1 = x_coords[i], y_coords[i]
                x2, y2 = x_coords[j], y_coords[j]
            elif j >= len(x_coords) and i <len(x_coords):
                x1, y1 = x_coords[i], y_coords[i]
                x2, y2 = tx_coords[j-len(x_coords)], ty_coords[j-len(x_coords)]
            elif i >= len(x_coords) and j <len(x_coords):    
                x1, y1 = tx_coords[i-len(x_coords)], ty_coords[i-len(x_coords)]
                x2, y2 = x_coords[j], y_coords[j]
            elif i >= len(x_coords) and j >= len(x_coords):
                x1, y1 = tx_coords[i-len(x_coords)], ty_coords[i-len(x_coords)]
                x2, y2 = tx_coords[j-len(x_coords)], ty_coords[j-len(x_coords)]
            ax.plot([x1, x2], [y1, y2], 'k--')
        plt.show()


class Main:
    # Определяем список элементов СБИС
    elements = [i for i in range(20)]


    # Определяем координаты элементов СБИС
    x_coords = np.random.randint(0, 10, size=len(elements))
    y_coords = np.random.randint(0, 10, size=len(elements))
    tx_coords = []
    ty_coords = []
    # for i in range(len(elements)):
    #     print(i,"...", x_coords[i], y_coords[i])


    x_mean = np.mean(x_coords)
    y_mean = np.mean(y_coords)
        


    # Создаем граф и добавляем вершины
    G = nx.Graph()
    for i in range(len(elements)):
        G.add_node(i, pos=(x_coords[i], y_coords[i]))
    
    Make_Snode.Mnode(G,x_coords,y_coords, 
elements,x_mean,y_mean,tx_coords,ty_coords)
    del_nodes.del_xx_node(G,x_coords,y_coords,tx_coords,ty_coords)
    del_nodes.del_xtx_node(G,x_coords,tx_coords,ty_coords)
    Make_edges.make_txtx_edge(G,x_coords,tx_coords,ty_coords)
    Make_edges.make_txx_edge(G,x_coords,y_coords,tx_coords,ty_coords)
    Make_edges.make_xtx_edge(G,x_coords,y_coords,tx_coords,ty_coords)
    Make_edges.make_xx_edge(G,x_coords,y_coords)
    
    # Строим кратчайшее покрывающее дерево
    T = nx.minimum_spanning_tree(G)


    # Создаем матрицу смежности
    n = len(x_coords)+len(tx_coords)
    sss = np.zeros((n,n), dtype=int) 
    for i in range(n):
        for j in range(n):
            if T.has_edge(i,j):
                sss[i][j] = sss[i][j] + 1
    
    del_node2.delnode(T,x_coords,tx_coords,n,sss)
    Prinr_weight.printer(T)
    Print_res.printer(T,x_coords,y_coords, elements,tx_coords,ty_coords)


# Отображаем результаты


# for i in range(len(sss)):
#     print(i,"...", sss[i])
# print(x_mean, y_mean)
# print("число точек", len(T.nodes))
# print("число доп точек", len(T.nodes)-len(x_coords))
# for i in range(len(tx_coords)):
#     print(tx_coords[i],ty_coords[i])
# print(len(T.nodes()))   
