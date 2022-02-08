library(neuralnet)
library(mlbench)
data(Sonar)
dim(Sonar)
levels(Sonar$Class)
head(Sonar)

X <- log(Sonar[,1:60] + 1) # predictors
y <-  Sonar$Class
Sonar_working <- cbind(y, X)

accuracy_table <- matrix(0,nrow = 100,ncol = 4)
colnames(accuracy_table) <- c("NeuralNet_15", "NeuralNet_18","NeuralNet_23_20","NeuralNet_28_23")
for(i in 1:100)
   {
       set <- sample(1:208, 158)
       training_data <- Sonar_working[set,]
       testing_data <- Sonar_working[-set,]
       NeuralNet_15_single <- neuralnet(y=="M"~., data = training_data, hidden = 15)
       NeuralNet_18_single <- neuralnet(y=="M"~., data = training_data, hidden = 18)
       NeuralNet_23_20_double <- neuralnet(y=="M"~., data = training_data, hidden = c(23,20))
       NeuralNet_28_23_double <- neuralnet(y=="M"~., data = training_data, hidden = c(28,23))
       accuracy_table[i,1]<-mean(ifelse(predict(NeuralNet_15_single,testing_data[,-1])>0.5,"M","R")==testing_data[,1])
       accuracy_table[i,2]<-mean(ifelse(predict(NeuralNet_18_single,testing_data[,-1])>0.5,"M","R")==testing_data[,1])
       accuracy_table[i,3]<-mean(ifelse(predict(NeuralNet_23_20_double,testing_data[,-1])>0.5,"M","R")==testing_data[,1])
       accuracy_table[i,4]<-mean(ifelse(predict(NeuralNet_28_23_double,testing_data[,-1])>0.5,"M","R")==testing_data[,1])
     }
accuracy_table

colMeans(accuracy_table)