""" 
Program: hw3.py
Programmed By: Brett Spatz and Jesse Stewart
Description: K-Means Clustering Algorithm
Trace Folder: stewart013
"""

#---------------------------------Imports--------------------------------------
import math
#------------------------------------------------------------------------------



#---------------------------------Variables------------------------------------
k = int # Integer holding number of clusters
data_file = "" # String holding name of file containing data
data = [] # List holding lists for each line in dataFile
#------------------------------------------------------------------------------



#---------------------------------Classes/Functions----------------------------
"""
    Takes name of data file as a parameter. Creates a list for each line
    in data file. Appends the lists to the data variable.
"""
def get_data(data_file):
    with open (data_file) as f: #Closes file after data is gathered
        lines = f.read().splitlines() #Splits at each new line
        #Creates a list for each line and converts data to floats
        for line in lines: 
            line = [float(i) for i in line.split(' ')] #Float for calculations
            data.append(line) #Append to data

"""
    Takes the data as a parameter. Returns the number of unique cluster
    values found within the data. Variable k will be set to this value.
"""
def num_clusters(data):
    count = int
    temp_list = [] #Holds list of all cluster values found in data
    for line in data:
        temp_list.append(line[2])
    #Use set to get unique values. Returns the length of the set.
    count = len(set(temp_list)) 
    return count
    
        
        
    
#------------------------------------------------------------------------------



#---------------------------------Program Main---------------------------------
def main():
    data_file = "synthetic_2D.txt"
    get_data(data_file)
    print(data)
    k = num_clusters(data)
    print(k)
	
main()		
#---------------------------------End of Program-------------------------------
