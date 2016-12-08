
import csv
import random
import math
import operator


def loadDataset(trainingSet,testSet):
	with open( "winequality_red.csv") as csvfile:
		split = 0.8
		readCSV = csv.reader(csvfile,delimiter=';')
		next(readCSV)
		dataset = list(readCSV)
		print(len(dataset))
		print(dataset)
		for x in range(0,len(dataset)):
			for y in range(4):
				dataset[x][y] = float(dataset[x][y])
			if random.random() < split:
				trainingSet.append(dataset[x])
			else:
				testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((float(instance1[x]) - float(instance2[x])), 2)

	return math.sqrt(distance)

def getDistsnce(trainingSet, testInstance):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))

	distances.sort(key=lambda element: element[1])

	return distances

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

def main():
	predictions = []
	k = 3
	trainingSet = []
	testSet = []
	correctly_classified_test_data=0
	loadDataset(trainingSet, testSet)
	print(len(testSet))
	print('Test set: ' + repr(testSet))
	print(len(trainingSet))
	print('Train set: ' + repr(trainingSet))
	predictions = []
	for x in range(len(testSet)):
		distances = getDistsnce(trainingSet, testSet[x])
		neighbours = distances[0:k]
		result = neighbours[0][0][-1]
		predictions.append(result)
		print('neighbors ' + repr(neighbours))
		print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))

	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')
	testsetResult = []

	for x in range (len(testSet)):
		testsetResult.append(testSet[x][-1])

	print("predictions : "+repr(predictions))
	print("test set    : "+repr(testsetResult))


main()
