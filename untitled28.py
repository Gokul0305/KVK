# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I4JSWaU68CUMYGK9jusTTVSLmVrc-109
"""

# Commented out IPython magic to ensure Python compatibility.
# %reload_ext rpy2.ipython

!pip install rpy2==3.5.1

# Commented out IPython magic to ensure Python compatibility.
# %%R
# x <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
# y <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)
# relation <- lm(y~x)
# 
# png(file = "linearregression.png")
# 
# plot(y,x,col = "blue",main = "Height & Weight Regression",
# abline(lm(x~y)),xlab = "Weight in Kg",ylab = "Height in cm")
# 
# dev.off()

# Commented out IPython magic to ensure Python compatibility.
# %%R
# input <- mtcars[,c("am","cyl","hp","wt")]
# xssssssssssssssssdsxdss
# am.data = glm(formula = am ~ cyl + hp + wt, data = input, family = binomial)
# 
# pred

# Commented out IPython magic to ensure Python compatibility.
# %%R
# install.packages("party")
#

# Commented out IPython magic to ensure Python compatibility.
# %%R
# library(party)
# 
# # Create the input data frame.
# input.dat <- readingSkills[c(1:105),]
# 
# # Give the chart file a name.
# png(file = "decision_tree.png")
# 
# # Create the tree.
#   output.tree <- ctree(
#   nativeSpeaker ~ age + shoeSize + score, 
#   data = input.dat)
# 
# # Plot the tree.
# plot(output.tree)
# 
# # Save the file.
# dev.off()

# Commented out IPython magic to ensure Python compatibility.
# %%R
# # Finding distance matrix
# distance_mat <- dist(mtcars, method = 'euclidean')
# 
# Hierar_cl <- hclust(distance_mat, method = "average")
# 
# # Plotting dendrogram
# plot(Hierar_cl)
# 
# 
# abline(h = 110, col = "green")
#  
# # Cutting tree by no. of clusters
# fit <- cutree(Hierar_cl, k = 3 )
# fit
#  
# table(fit)
# rect.hclust(Hierar_cl, k = 3, border = "green")

# Commented out IPython magic to ensure Python compatibility.
# %%R
# # Library required for fviz_cluster function
# install.packages("factoextra")
# library(factoextra)
# 
# # Loading dataset
# df <- mtcars
# 
# # Omitting any NA values
# df <- na.omit(df)
# 
# # Scaling dataset
# df <- scale(df)
# 
# # output to be present as PNG file
# png(file = "KMeansExample.png")
# 
# km <- kmeans(df, centers = 4, nstart = 25)
# 
# # Visualize the clusters
# fviz_cluster(km, data = df)
# 
# # saving the file
# dev.off()
#



install.packages("fpc")
  
# Loading package
library(fpc)
  
# Remove label form dataset
iris_1 <- iris[-5]
  
# Fitting DBScan clustering Model 
# to training dataset
set.seed(220)  # Setting seed
Dbscan_cl <- dbscan(iris_1, eps = 0.45, MinPts = 5)
Dbscan_cl
  
# Checking cluster
Dbscan_cl$cluster
  
# Table
table(Dbscan_cl$cluster, iris$Species)
  
# Plotting Cluster
plot(Dbscan_cl, iris_1, main = "DBScan")
plot(Dbscan_cl, iris_1, main = "Petal Width vs Sepal Length")