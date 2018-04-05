""" 
Program:       hw3.py
Programmed By: Brett Spatz and Jesse Stewart
Description:   K-Means Clustering Algorithm
Trace Folder:  stewart013
"""

#---------------------------------Imports--------------------------------------
import math
import random
from statistics import mode
#------------------------------------------------------------------------------



#---------------------------------Variables------------------------------------
k = 3          # Integer holding number of clusters
dataFile = ""  # String holding name of file containing data
randSeed = 45  # Arbitrary integer constant to seed random number generator

# List holding each cluster
clusters = [[] for i in range(k)]
#------------------------------------------------------------------------------



#---------------------------------Classes/Functions----------------------------
"""
    Description: Creates a list of lists for the data. Pre-processing is done
                 as needed.
    Input:       Name of data file.
    Returns:     List of lists containing data.
"""
def getData(dataFile):
    data = []
    with open (dataFile) as f:
        lines = f.read().splitlines()
        
        # Creates a list for each line and converts data to floats
        for line in lines: 
            line = [float(i) for i in line.split(' ')]
            data.append(line)
    return data

 
"""
    Description: Find Euclidean distance measure of two nodes.
    Input:       Two nodes from data.
    Returns:     Euclidean distance of two nodes.
"""
def euclideanDist(curr_node, comp_node):
    squared_euclidean = []
    euclidean_dist = 0
    for num in range(0,len(curr_node)-1): # Excluding known cluster
        curr = float(curr_node[num])
        comp = float(comp_node[num])
        squared_euclidean.append((curr-comp)*(curr-comp))
    for itr in squared_euclidean:
        euclidean_dist = euclidean_dist + itr
    return math.sqrt(euclidean_dist)


"""
    Description: Randomly determine the initial means and prints output.
    Input:       Pre-processed data, number of means to find (k).
    Returns:     List containing mean values.
"""   
def setInitialMeans(k, data):
    random.shuffle(data) # Randomly shuffle data in place
    means = []
    for num in range(k):
        item = data[num]
        means.append(item)
    
    # Matches output example in homework description (with slight changes)
    print("Initial k means are")
    for element in means:
        print("mean[", means.index(element), "] is ", element, sep = '')
        
    return means


"""
    Description: Assigns each object in the data to the cluster with the
                 with the minimum euclidean distance between the cluster
                 mean and the object.
    Input:       List of means, pre-processed data.
    Output:      Updated list of clusters
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
    return clusters
            

"""
    Description: Calculates new mean for each cluster.
    Input:       List of cluster lists and list of means for each cluster.
    Returns:     List containing new mean values
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
    Description: Calculates accuracy rate, formats and prints output specified
                 in homework description.
    Input:       Clusters after running algorithm
    Output:      The label of each cluster (based off of majority class label),
                 the cluster index (0-2), the size of each cluster, the data
                 found in each cluster, the accuracy rate of the algorithm, and
                 the number of misclassified objects in each cluster.
"""
def outputResults(clusters):
    totalIncorrect = 0
    totalCount = 0
    for cluster in clusters:
        print("\nCluster", clusters.index(cluster))
        clusterSize = len(cluster)
        print("Size of cluster", clusters.index(cluster), "is", clusterSize)
        numIncorrect = 0
        clusterLabels = []
        for item in cluster:
            clusterLabels.append(int(item[2]))
        clusterLabel = mode(clusterLabels)
        print("Objects in this cluster:")
        for item in cluster:
            if int(item[2]) != clusterLabel:
                numIncorrect = numIncorrect + 1
            print(item)
        print("Cluster label:", int(clusterLabel))
        print("Number of objects misclassified in this cluster:", numIncorrect)
        totalIncorrect = totalIncorrect + numIncorrect
        totalCount = totalCount + clusterSize
    accuracyRate = ((totalCount - totalIncorrect) / totalCount) * 100
    print("Overall accuracy rate is ", accuracyRate, "%", sep = '')
         
        
"""    
    Description: Randomly assigns initial means for k clusters. Assigns objects
                 in data to each cluster based on minimum distance.
                 Recalculates means each time objects are re-clustered. Stops
                 when the values of the means does not change anymore. (Stops
                 when objects are not being reclustered)
    Input:       Value for k, data to be clustered.
    Returns:     Final clusters after convergence criteria is met.
"""
def KMeans(k, data): 
    old_means = setInitialMeans(k, data)
    new_means = old_means # Must be initialized to start  
    count = 0   # Allows do while functionality
    stor_means = []
    while (old_means != new_means or count < 1):
        clusters = assignToClusters(new_means, data)
        new_means = calcNewMeans(clusters, old_means)
        count = count + 1
        stor_means.append(new_means)
        if(count > 2):
            old_means = stor_means[count-2]
    return clusters

#------------------------------------------------------------------------------



#---------------------------------Program Main---------------------------------
def main():
    dataFile = "synthetic_2D.txt"
    data = getData(dataFile)
    random.seed(randSeed) # Seed with constant int to get the same output
    finalClusters = KMeans(k, data)
    outputResults(finalClusters)
	
main()		
#---------------------------------End of Program-------------------------------
