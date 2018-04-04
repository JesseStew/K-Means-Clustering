""" 
Program:       hw3.py
Programmed By: Brett Spatz and Jesse Stewart
Description:   K-Means Clustering Algorithm
Trace Folder:  stewart013
"""

#---------------------------------Imports--------------------------------------
import math
import random
#------------------------------------------------------------------------------



#---------------------------------Variables------------------------------------
k = int        # Integer holding number of clusters
dataFile = ""  # String holding name of file containing data
data = []      # List holding lists for each line in dataFile
ranSeed = 90   # Arbitrary integer constant to seed random number generator
#------------------------------------------------------------------------------



#---------------------------------Classes/Functions----------------------------
"""
    Description: Creates a list for each line in data file. Appends the lists 
                 to the data list.
    Input:       Name of data file.
"""
def getData(dataFile):
    with open (dataFile) as f:
        lines = f.read().splitlines()
        
        # Creates a list for each line and converts data to floats
        for line in lines: 
            line = [float(i) for i in line.split(' ')]
            data.append(line)


"""
    Description: Finds unique clusters to determine value of k.
    Input:       The pre-processed data (in the form of a list of lists).
    Returns:     Number of unique clusters found within the data.
"""
def numClusters(data):
    count = int
    tempList = [] # Holds list of all cluster values found in data
    for line in data:
        tempList.append(line[2])
        
    # Use set to get only unique values. Returns the length of the set.
    count = len(set(tempList)) 
    return count

 
"""
    Description: Find Euclidean distance measure of two nodes.
    Input:       Two nodes from data.
    Returns:     Euclidean distance of two nodes.
"""
def euclideanDist(curr_node, comp_node):
    squared_euclidean = []
    euclidean_dist = 0
    for num in range(0,len(curr_node)-1):   #excludes final list item which contains cluster it belongs to.
        curr = float(curr_node[num])
        comp = float(comp_node[num])
        squared_euclidean.append((curr-comp)*(curr-comp))
    for itr in squared_euclidean:
        euclidean_dist = euclidean_dist + itr
    return math.sqrt(euclidean_dist)


"""
    Description: Randomly determine the initial means.
    Input:       Pre-processed data, number of means to find (k).
    Returns:     List of initial k random nodes.
"""   
def setInitialMeans(k, data):
    random.shuffle(data)
    init_means = []
    for num in range(k):
        init_means.append(data[num])
    return init_means

"""
    Description: Assigns each node to the cluster which has the closest mean.
    Input:       Pre-processed data, initially selected means.
    Returns:     Dictionary with cluster numbers as keys containing 
                 nodes that belong to that cluster.
"""   
def assignItems(init_means, data):
    clusters = {}
    for itr in init_means:
        clusters[itr[2]] = []   #initializes clusters as keys to lists
    for itr in data:
        curr_dist = math.inf    #large number to be updated
        clust_num = float       #for storing the cluster of min dist from node
        for i in init_means:
            dist = euclideanDist(itr, i)
            if(dist < curr_dist):
                clust_num = i[2]
                curr_dist = dist
                node = itr
        clusters[clust_num].append(node)
    return clusters

"""
    Description: Calculates new mean for each cluster.
    Input:       Dictionary with cluster numbers as keys containing 
                 nodes that belong to that cluster.
""" 
def calcNewMeans(clusters):
    
#------------------------------------------------------------------------------



#---------------------------------Program Main---------------------------------
def main():
    dataFile = "synthetic_2D.txt"
    getData(dataFile)
    #print(data)
    k = numClusters(data)
    init_means = setInitialMeans(k, data)
    clusters = assignItems(init_means, data)
    print("k: ", k)
    print("init_means: ", init_means)
    print("clusters[init_means[0][2]]: ", clusters[init_means[0][2]])
    print("\nclusters[init_means[1][2]]: ", clusters[init_means[1][2]])
    print("\nclusters[init_means[2][2]]: ", clusters[init_means[2][2]])
	
main()
#---------------------------------End of Program-------------------------------