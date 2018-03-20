# import required Libraries
library(stringr)
library(caret)
library(neuralnet)
library(devtools)
library(rpart)
install.packages("rpart.plot")

# Load dataset and summary is obtained
concrete=read.csv("Concrete_Data.csv")
str(concrete)
summary(concrete)

#normalization is done and new values are obtained in between 0 and 1
normalize <- function(x) {return((x - min(x)) / (max(x) - min(x)))}
names(concrete)<-gsub("\\."," ",names(concrete))
names(concrete)<-word(names(concrete),1)
names(concrete)[9]<-"Strength"
concrete_norm <- as.data.frame(lapply(concrete, normalize))
set.seed(12345)

# Partition of dataset is done for creating Training and Test dataset
inTrain<-createDataPartition(y=concrete_norm$Strength,p=0.75,list=FALSE)
concrete_train <- concrete_norm[inTrain, ]
concrete_test <- concrete_norm[-inTrain, ]

# Trained using ANN with 1 hidden layer
concrete_model <- neuralnet(formula = Strength ~ Cement + Blast + Fly + Water + Superplasticizer + Coarse + Fine + Age, data = concrete_train)
model_results <- compute(concrete_model, concrete_test[1:8])
predicted_strength <- model_results$net.result
cor(predicted_strength, concrete_test$Strength)[1,1]

# ANN performs best at 5 hidden layers and gives more accuracy
concrete_model2 <- neuralnet(formula = Strength ~ Cement + Blast + Fly + Water + Superplasticizer + Coarse + Fine + Age, data = concrete_train, hidden=5)
plot(concrete_model2)

# Used Random Forest to determine strength and noticed improvement in predicted strength
model_result3 <- train(Strength ~ ., data = concrete_train,method='rf',prox=TRUE)
model_result3
predicted_strength3 <- predict(model_result3,concrete_test)
cor(predicted_strength3, concrete_test$Strength)

# Improved final result by Resampling
model_result4 <- train(Strength ~ ., method='rf',data = concrete_train,verbose=FALSE,trControl = trainControl(method="cv"))
model_result4
predicted_strength4 <- predict(model_result4,concrete_test)
cor(predicted_strength4, concrete_test$Strength)

# Display of Random Forest Tree Solution and the obtained result will be easy to visulaize even more complex trees having complex data.
strength.tree <- rpart(Strength ~ .,data=concrete_train, control=rpart.control(minsplit=20,cp=0.002))
prp(strength.tree,compress=TRUE)