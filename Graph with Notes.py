#Roger H Hayden III
#Graph with Notes
#1/24/2022

#Graph Class
#Create a empty dictionary
class Graph:
    def __init__(self):
        self.adj_list = {}

#Print Method
#This will take any vertex in the adj_list and print it with the vertex : list
#Example: A : [] for an empty list
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

#Add Vertex Method
#If the vertex is not in the adj_list, then add it and return TRUE
#This will add the vertex with an empty list
#If it is already in the adj_list then return FALSE
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

#Add Edge Method
#We will pick vertex 1 and 2 in which we want to have an edge between
#we are going to append vertex 2 on to vertex 1 and vertex 1 on vertex 2
#as long as both verticies exist.
#If one of the verticies dont exist then we pass FALSE,
#If they do and we are able to run the code then pass TRUE.
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

#Remove Edge Method
#Very similar to adding an edge.
#The first part is exactly the same except we do .remove rather than append
#If we are able to do this then we return TRUE, if not then we return FALSE
#In addition, if there is a value error we want to decide to ignore the error.
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): 
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

#Remove Vertex Method
#Before we can remove a vertex you must remove all the edges connected to it.
#First we check that the vertex exists in the graph.
#If it does then the for loop will remove all of the edges connected to the vertex.
#Once this is complete then we delete the vertex itself.
#If successful, print TRUE if not then FALSE
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False        


my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.print_graph()

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')

my_graph.remove_edge('A','D')

my_graph.remove_vertex('D')

my_graph.print_graph()

