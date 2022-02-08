# Neural-Networks

 We perform analysis of the sonar data using neural networks. For 100 independent replications (i.e., 100 independent training /testing splits),
	
 -  Fit four different neural networks:

-Two distinct single hidden layer neural networks: (i) A single hidden layer with 15 nodes (ii) A single hidden layer with 18 nodes:  
 
-Two distinct neural networks with two hidden layers: (iii) Two hidden layers with 23 and 20 nodes  and (iv) Two hidden layers with 28 and 23 nodes.

- Compare the accuracy of these four Neural networks among them.
- Also compare it to other classification methods.
Specifically, we will compare neural network performance to the methods below:
 
  Linear Discriminant Analysis (LDA).
  Quadratic Discriminant Analysis (QDA).
  Regularized Discriminant Analysis(RDA).
 
  Support Vector Machines (SVMs): 

   Naïve Bayes.

     
 # Data  
     Sonar Dataset. To generate in R Code, we use : library(mlbench) and data(Sonar)

     
 # Code implementation.
   
    R packages: neuralnet 


 - The comparison will be possible by implementing simulated accuracy matrices. We calculate the average accuracy for each method and compare these values.


 # Conlusion
   -Among the four Neural Networks, the one with the best performance is the Neural Network with Two hidden layers with 28 and 23 nodes (NeuralNet_28_23).

   -Among all the classification methods
The accuracy of the Superlearner method is the best. Followed by RandomForest
and   ( Neural Network with Two hidden layers with 28 and 23 nodes) NeuralNet_28_23.
Then, NeuralNet_18 , NeuralNet_15, Gradient Boosting method etc.



