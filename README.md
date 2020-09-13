# Classifying-Digits

##### Implementation of KNN to classify normalized handwritten digits.

## CS 360 Lab 1 - K-nearest neighbors - Machine Learning Class

Name: Mohamed Ali

Number of Late Days using for this lab: 0

---

### Analysis Questions

1. What values of K did you try?

[1,2,3,5,7,8,9,10,15,100]

2. Which value of K produced the highest accuracy? What general trends did you
observe as K increased?

-Accuracy was highest at k = 1, but this might be an outlier as k = 2
  has worse accuracy but k = 3 has better than k = 2.
-The trend seems to be that accuracy decreases as k increases.

k =  1 ,  97.527 %
k =  2 ,  96.703 %
k =  3 ,  96.978 %
k =  5 ,  96.978 %
k =  7 ,  96.703 %
k =  8 ,  96.429 %
k =  9 ,  96.429 %
k =  10 ,  96.429 %
k =  15 ,  96.154 %
k =  100 ,  91.758 %

3. When using the entire training dataset, what are your observations about the
runtime of K-nearest neighbors? List 1-2 ideas for making this algorithm faster.

The algorithm is very slow even when only examples from 2 and 3 are used.
Using the whole data set would take 20-30 minutes for one accuracy check.

###### Ideas to make knn faster:

1. finding a way to avoid sorting the whole list of distances and only sorting
as much as we care about by identifying distances that are so large.

2. finding a way to avoid making n comparisons, this will also make sort faster.


---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab?

 6

2. How difficult did you find this lab? (1-5, with 5 being very difficult and
  1 being very easy)

 2

3. Describe the biggest challenge you faced on this lab:

 Sorting the array based on distance while keeping the genuine label.


### Extensions Implemented

NOTE: Each extension is implemented in a separate file, as implementing all of
  them in one file would make running the file so slow and would mess up with
  the basic code (without extensions).

#### Extension 1:

- Extended the algorithm to a multi-class setting by distinguishing 4 classes,
2, 3, 5, and 8.

- Got the following results:
k =  1 ,  94.058 %
k =  3 ,  94.203 %
k =  5 ,  94.638 %
k =  7 ,  94.203 %
k =  9 ,  93.478 %
k =  20 ,  92.029 %
k =  100 ,  86.377 %

-Observing the results shows that:
  a. Accuracy still decreases when k increases significantly.
  b. When the dataset becomes larger, we can increase accuracy by increasing
    k very slightly, maybe by 1 or 2, as the optimal k here is between 5 and 7.

-------------------------------------------------------------------------------

#### Extension 2:

-Implemented confusion matrix by computing TP, TN, FP, and FN
-Used k = 1 (best accuracy for knn.py)
-Got the following results:

             Predicted: 2  Predicted: 3
Actual: 2     TN =  192      FP =  3
Actual: 3      FN =  6      TP =  163


-Used k = 3 or k = 5
-Got the following results:

             Predicted: 2   Predicted: 3
Actual: 2     TN =  191       FP =  4
Actual: 3      FN =  7       TP =  162

-------------------------------------------------------------------------------

#### Extension 3:

Check out extension3.png
