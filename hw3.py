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
k = 3          # Integer holding number of clusters
dataFile = ""  # String holding name of file containing data
data = []      # List holding lists for each line in dataFile
randSeed = 90  # Arbitrary integer constant to seed random number generator
means = []     # List holding mean values

# List holding each cluster
clusters = [[] for i in range(k)]
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
    Description: Randomly determine the initial means and prints output.
    Input:       Pre-processed data, number of means to find (k).
"""   
def setInitialMeans(k, data):
    random.shuffle(data) # Randomly shuffle data in place
    for num in range(k):
        item = data[num]
        item = item[:2]
        means.append(item)
    
    # Matches output example in homework description (with slight changes)
    print("Initial k means are")
    for element in means:
        print("mean[", means.index(element), "] is ", element, sep = '') 

"""
    Description: Assigns each object in the data to the cluster with the
                 with the minimum euclidean distance between the cluster
                 mean and the object.
    Input:       List of means, pre-processed data.
"""
def assignToClusters(means, data):
    for item in data:
        distances = []
        minDist = float
        for element in means:
            dist = euclideanDist(item, element)
            distances.append(dist)
        minDist = min(distances)
        clusterIndex = distances.index(minDist)
        for cluster in clusters:
            if item in cluster:
                cluster.remove(item)
        clusters[clusterIndex].append(item)
            
        
    

"""
    Description: Calculates new mean for each cluster. Updates means list
                 with new values.
    Input:       List of cluster lists and list of means for each cluster.
""" 
def calcNewMeans(clusters, oldMeans):
    newMeans = []
    for cluster in clusters:
        clustSize = len(cluster)
        clustMeans = []
        firstMean = 0.0
        secondMean = 0.0
        for item in cluster:
            firstMean = firstMean + item[0]
            secondMean = secondMean + item[1]
        firstMean = firstMean / clustSize
        secondMean = secondMean / clustSize
        clustMeans.append(firstMean)
        clustMeans.append(secondMean)
        newMeans.append(clustMeans)
    return newMeans

"""
def KMeans(cluster, means, data, updatedMeans = None):
    if means != updatedMeans:
        if updatedMeans == None:
            assignToClusters(means, data)
            updatedMeans = calcNewMeans(clusters, updatedMeans)
        else:    
            assignToClusters(updatedMeans, data)
            updatedMeans = calcNewMeans(clusters, updatedMeans)
            KMeans(cluster, means, data, updatedMeans)
    
"""   
    
#------------------------------------------------------------------------------



#---------------------------------Program Main---------------------------------
def main():
    dataFile = "synthetic_2D.txt"
    getData(dataFile)
    random.seed(randSeed) # Seed with constant int to get the same output
    setInitialMeans(k, data)
    assignToClusters(means, data)
    updatedMeans = calcNewMeans(clusters, means)
    print(updatedMeans)
    print(clusters)
    assignToClusters(updatedMeans, data)
    updatedmMeans = calcNewMeans(clusters, means)
    print(updatedmMeans)
    print(clusters)

    """
    print("Cluster 0:", clusters[0])
    print("Cluster 1:", clusters[1])
    print("Cluster 2:", clusters[2])
    """
    
	
main()		
#---------------------------------End of Program-------------------------------
