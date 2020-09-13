"""
Implementation of extension 1 on digits 2, 3, 5, and 8
Look for changes at separate() at line 25 and prediction method at line 49
@author Mohamed Ali
@version September 13, 2020
"""
import math
import numpy as np

def main():
    #read raw train data
    train_data = np.loadtxt("/mnt/1062576C62575596/CS360/Lab1 Data/zip.train")
    #read raw test data
    test_data = np.loadtxt("/mnt/1062576C62575596/CS360/Lab1 Data/zip.test")
    #extract data with labels of 2 and 3 for train and test
    train_data = separate(train_data)
    test_data = separate(test_data)
    #store the dictionary of {k:acc} as output
    output = get_accuracy(train_data, test_data, [1,3,5])
    #print the dictionary's content in desired format
    for k in output:
        print("k = ", k, ", ", output[k], "%")

#method to extract examples with labels of 2 and 3
def separate(data):
    #define an empty 2D array
    to_return = np.empty((0, data.shape[1]))
    for i in range (data.shape[0]):
        #append data if the label is 2, 3, 5, or 8
        if data[i][0] in (2,3,5,8):
            to_return = np.append(to_return, [data[i]], axis=0)
    return to_return

#method to get nearest k neighbors and predict label
def knn_classifier(train_data, test, k):
    dist_array = list()
    for train_row in train_data:
        #disregarding label column
        distance = dist(test[1:], train_row[1:])
        #appending the distance along with the train label
        dist_array.append((distance, train_row[0]))
    #sorting with a custom key to make sure the array is sorted by distance
    dist_array.sort(key=lambda tup: tup[0])
    neighbors = list()
    for i in range(k):
        #only appending genuine labels to neighbors list
        neighbors.append(dist_array[i][1])
    #predicting the number that has been voted for the most
    prediction = max(set(neighbors), key=neighbors.count)

    return prediction

#method to return a dictionary of k values and the resulting accuracy
def get_accuracy(train_data, test_data, k_list):
    #define a dictionary with k values as keys
    accuracy_dict = dict.fromkeys(k_list)
    for k in k_list:
        #counter to count correct predictions based on train labels
        correct_predictions=0
        for test in test_data:
            #comparing prediction with genuine test label
            if knn_classifier(train_data, test, k) == test[0]:
                correct_predictions+=1
        #calculating accuracy
        acc = correct_predictions/test_data.shape[0]
        #adding roundedd acc value to its corresponding k
        accuracy_dict[k] = round(acc*100, 3)
    return accuracy_dict


"""
method to compute Ecludian Distance
pre-requiste: len(test)==len(train)
"""
def dist(test, train):
    sum = 0.0
    for i in range(len(test)):
        sum += (test[i] - train[i]) ** 2
    return math.sqrt(sum)


main()
