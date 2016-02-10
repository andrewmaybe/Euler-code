#What is the greatest product of four adjacent numbers in the same
#direction (up, down, left, right, or diagonally) in the 20*20 grid

import copy

def getproduct(array): #returns product of all elements of the array
    product = 1
    for n in (array):
        product = product * int(n)
    return product        

def biggestproduct(array,n): #returns biggest product of n sequential integers
# tested and works with string or array as both are just lists anyway
    length = len(array)
    biggest = 0
    while (length >n-1):
        ss = array[:n]
        value = getproduct(ss) #find product using getproduct function
        #print "ss",ss,"product:",value
        array = array[1:]
        length = len(array)
        if (value > biggest): biggest = value
    print "biggest",biggest
    return biggest

"""
bigstring = [23,45,12,2,5,8,67,45,99,3,2,0,4,5,8,9,33]
print bigstring
testing = biggestproduct(bigstring,4)
print "T:",testing
"""

Grid = []
Filename = "Euler11Grid.txt"
with open(Filename) as f:
    for line in f:
        inner_list = [int(elt.strip()) for elt in line.split(' ')]
        Grid.append(inner_list) 

#lines horizontal
Total = 0
temprow = []
biggest = 0
rowbiggest = 0
for row in Grid: #loops through rows
    #print row
    temprow = copy.deepcopy(row)
    rowbiggest = biggestproduct(temprow,4) #uses function to find product
    if rowbiggest > biggest: biggest = rowbiggest
print "biggest-h:",biggest

#lines vertical
Total = 0
temprow = []
biggest = 0
rowbiggest = 0
Gridv = []
Gridv = zip(*Grid) #transposes grid
for row in Gridv: #loops through rows
    #print row
    temprow = copy.deepcopy(row)
    rowbiggest = biggestproduct(temprow,4) #uses function to find product
    if rowbiggest > biggest: biggest = rowbiggest
print "biggest-v:",biggest

#lines diagonal TL start



