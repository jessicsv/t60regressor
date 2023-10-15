import numpy as np
import scipy.io

#load a matlab File input into an array
def loadMatData(inputFile, columnName):
  matData = scipy.io.loadmat(inputFile)
  matData = matData[columnName]
  matData = np.array(matData)
 
  #checking if it is a row or column vector
  shape = matData.shape[0]
  if shape ==1:
    matData = matData.T
  return matData
 
#load a matlab File input into an array
def loadMatData(inputFile, columnName):
  matData = scipy.io.loadmat(inputFile)
  matData = matData[columnName]
  matData = np.array(matData)
 
  #checking if it is a row or column vector
  shape = matData.shape[0]
  if shape ==1:
    matData = matData.T
  return matData
  
#load a csv File input into an array
def loadCSVData(inputFile):
   filename = inputFile
   raw_data = open(filename, 'rt',encoding='latin-1')
   CSVData = np.loadtxt(raw_data, delimiter=",")
   CSVData= np.array(CSVData) 
   return CSVData

#Removes edge values avoiding NaN 
def removeEdgeValues(inputArray):
  #sorting 
  inputArray=  np.sort(inputArray,1)
  #removing min and max values
  inputArray = np.delete(inputArray, 0,1)
  inputArray = np.delete(inputArray,511,1)
  inputArray = np.delete(inputArray, 0,1)
  inputArray = np.delete(inputArray,509,1)
  return inputArray

#Converts a vector into a single line List
def makeFlat(inputVector):
  inputList= [measure.tolist() for measure in inputVector]
  outputList = []
  for sublist in inputList:
            for item in sublist:
                outputList.append(item)
  return outputList

#Converts a measure from ms to second
def msToSecond(inputArray):
  outputArray = np.multiply(inputArray,0.001)
  return outputArray

def joinFeatures(featuresList,newFeatureList):
  for i in range (0,len(newFeatureList)):
            featuresList[i] = np.append(featuresList[i],[newFeatureList[i]])
  return featuresList

