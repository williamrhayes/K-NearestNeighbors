# K-NearestNeighbors

Learning about the K-Nearest Neighbors statistical analysis technique

-----------------------------------------------------------------------

For this project, I wanted to test my understanding of the K-Nearest
Neighbors statistical analysis technique by building and testing it
from scratch.

The K-Nearest Neighbors (KNN) technique is a simple statistical technique
used to predict an outcome from a given set of inputs. It does this by
finding the k closest values (nearest neighbors) to the x-value you would
like to predict. Then, it averages these values to deliver a prediction.
As the number of neighbors (k) increases, the predicted output approaches
a flat line that represents the average of all the values. This phenomena
is seen in the 

K-NN_Demo 

folder.

In order to find the optimal K-value, data is split into training and 
testing sets. The training set is used to build a line of predictions
while the testing set is used to find out how close this line came to 
the true value of the data. For each k value, the squared error
is calculated by subtracting the true y-value from the predicted
y-value and squaring this difference. Then, once the squared error has
been calculated for each test point, the average of all these squared
errors is used to give the overall score for that k-value, the
mean squared error (MSE).

We then iterate through each k-value and consider the k-value with the
lowest MSE our best shot at predicting the outcome of a given input.

In my figures, training data is represented by red dots, testing data
is represented by grey dots, and the K-NN prediction is represented 
by the blue line.

Finally, I noticed on a wikipedia article that I referenced that MSE
is much lower in a normalized dataset. Therefore, I normalized my 
data and found that the MSE was significantly lower!

My process is mostly laid out in the 

KNN Simulator.ipynb

Jupyter notebook. 
