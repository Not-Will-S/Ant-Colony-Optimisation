import numpy as np
import random
np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True, precision=5)

#Notes - The first ant will always set off from bin 1 to represent the start point 
#To change the batch size please change the following variables: j value in the outer loop of updatePheramones,i value of outer loop of the main function(1000 if batch of 10 and 100 if 100) and the passed value into the run batch function. In addition the avarage fitness calculation should be adjusted if that's a parameter of interest  
#To change which bin packing problem please use ctrl F and change every True or false Value present in a function call to it's opposite. True for BPP2 False for BPP1. Also change the input of BuildPheramone matrix from 10 to 50. 

#This function will initialise the pheramone matrix with random decimal values from 0 to 1
def buildPheramoneMatrix(binNo):
    pheramoneMatrix = np.random.rand(binNo, 500, binNo) # Initialises a 3D matrix with pheramone values for every graph edge 
    return pheramoneMatrix

#This function will build a matrix holding the weights of different items for BPP1 & BPP2
def buildItemWeightMatrix(BPP2): # This needs to be changed to allow BPP2 also 
    if BPP2 == False:
        itemWeightMatrix = np.zeros((10, 500)) # initialises a matrix that will store where the different items are held 
    else:
        itemWeightMatrix = np.zeros((50, 500))
    return itemWeightMatrix

#This function determines the next path the ant will take  
def chooseNextPath(verticalSlice, BPP2):
    if BPP2 == False:
        paths = [0,1,2,3,4,5,6,7,8,9] # each path represents a diferent bin 
    else:
        paths = []
        for i in range(50):
            paths.append(i)
    totalPheramone = sum(verticalSlice) # finds the sum of all the pheramones ahead of the ant 
    for count, pheramoneValue in enumerate(verticalSlice): # iterates through every pheramone value
        verticalSlice[count] = pheramoneValue/totalPheramone #Finds the probability that an ant should take each path based on pheramone strength
    pathChoice = random.choices(paths, verticalSlice)[0] #uses the random library to pick a path based on probability distribution 
    return pathChoice

#This function runs the ant path and adds weights to bins  
def runAntPath(itemWeightMatrix, pheramoneMatrix, BPP2):
    takenPath = np.zeros((500)) # Empty matrix holding the path taken 
    currentNode = 1
    for i in range(500):
        nextPath = chooseNextPath(pheramoneMatrix[:,i, currentNode].copy(), False) #This will choose the next path based on a pheramone slice 
        currentNode = nextPath
        if BPP2 == False:
            itemWeightMatrix[nextPath, i] = i #adds the weight in the correct location 
        else:
            itemWeightMatrix[nextPath, i] = (i*i)/2 #weight for bpp2 
        takenPath[i] = int(nextPath)#creates a record of the path 

    return takenPath, itemWeightMatrix

#This function will evaluate the fitness of each run 
def fitnessFunction(itemWeightMatrix, BPP2):
    heaviestBin = 0
    lightestBin = None
    if BPP2 == False:
        bins = 10
    else:
        bins = 50
    for i in range(bins):
        totalWeight = sum(itemWeightMatrix[i,:]) #Finds the sum of items stored in each bin
        if(totalWeight > heaviestBin): #compares the sum of the current bin with the heaviest
            heaviestBin = totalWeight
        if lightestBin == None or totalWeight < lightestBin: #compares the current bin to the lightest 
            lightestBin = totalWeight    
    return heaviestBin - lightestBin #returns the difference between the heaviest and lightest bin 

def updatePheramones(pheramoneMatrix, takenPath, pathFitness):  #TODO update for 3D matrix support 
    for j in range(10): # outer loop determines batch size 
        lastNode = 1 
        for i in range(500): # Inner loop is the number of items 
            pheramoneMatrix[int(takenPath[j][i]), i, lastNode] = pheramoneMatrix[int(takenPath[j][i]), i, lastNode] + 100/pathFitness[j] # increments the pheramones by the fitness only on the specific edge
            lastNode = int(takenPath[j][i]) #sets the new node that the ant has moved to
    return pheramoneMatrix

def evaporatePheramones(pheramoneMatrix, evaportationRatio):
    pheramoneMatrix = pheramoneMatrix*  evaportationRatio # reduces the entire pheramone matrix by the evaportion ratio
    return pheramoneMatrix #returns the updated pheramone matrix 
    
def runBatch(batchIterations, pheramoneMatrix): 
    antPaths = [] # will contain every ant path taken in the batch 
    pathFitnessArray = [] # List item containing the path fitness's 
    batchAverageFitnessTotal = 0
    batchBestFitness = None 
    for i in range(batchIterations):
        itemWeightMatrix = buildItemWeightMatrix(False)#rebuilds the item weights 
        antPath, itemWeightMatrix = runAntPath(itemWeightMatrix, pheramoneMatrix, False) #runs one ant path - True for bpp2, False for bpp1
        antPaths.append(antPath)#stores the ant path
        pathFitness = fitnessFunction(itemWeightMatrix, False)#finds the fitness of that specific path 
        batchAverageFitnessTotal += pathFitness #keeps a total to find average
        if (batchBestFitness == None or pathFitness < batchBestFitness):
            batchBestFitness = pathFitness #stores the best fitness in the batch
        pathFitnessArray.append(pathFitness)#stores the fitness for that path 
    return antPaths, pathFitnessArray, batchBestFitness, batchAverageFitnessTotal/10

#Main function and entryPoint
def crawlMyAnts():
    pheramoneMatrix = buildPheramoneMatrix(10)
    overallBest = None
    for i in range(1000):
        antPaths, pathsFitness, bestFitness, averageFitness = runBatch(10, pheramoneMatrix) #runs a batch of ants 
        print("The average fitness in this batch is ", averageFitness)
        print("The best fitness in this batch is ", bestFitness)
        pheramoneMatrix = updatePheramones(pheramoneMatrix, antPaths, pathsFitness) # updates the pheramones in the pheramone matrix 
        pheramoneMatrix = evaporatePheramones(pheramoneMatrix, 0.9) #evaporates the pheramones by the inputted factor 
        if overallBest == None or overallBest > bestFitness:
            overallBest = bestFitness
    print("The best fitness was ", overallBest)

crawlMyAnts()




