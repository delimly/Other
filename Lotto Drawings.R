#GET RICH OR DIE TRYING 

# Lotto Function 
# Function's Purpose: To pick 6 numbers 1-59 in 7 lines of numbers to play in the National Lottery

lotto <- function(){

  TestMatrix <- matrix(NA, nrow = 7, ncol = 6) # Creating our null matrix to input data
  
  for(i in c(1:7)){
    
    x <- unique(runif(6,1,59)) # Drawing unique psudo-random numbers as vector
    
    TestMatrix[i,] <- x # We insert the row vector into each row of matrix
    
    for(j in c(1:6)){
      # Conditions to ensure each number in 1-59 can be attained. 
      
      if(TestMatrix[i,j] < 30.5){TestMatrix[i,j]  = floor(TestMatrix[i,j])} else{
        TestMatrix[i,j]  = ceiling(TestMatrix[i,j])}
    }
  }

  return(TestMatrix) # What we should put in our Lotto Ticket
}

lotto()

# EuroMillions Function 
# Functions Purpose : To pick 5 Numbers from 1-50 and Two lucky stars 

EuroMillions <- function(){
  
  TestMatrix <- matrix(NA, nrow = 7, ncol = 7)
  
  for (i in c(1:7)) {
    
    x <- unique(runif(5,1,50))
    y <- unique(runif(2,1,12))
    
    z <- c(x,y)
    
    TestMatrix[i,] <- z
    
    for(j in c(1:7)){
      
      # Note due to this operation there may be repeat numbers (out of the first 5) in this case rerun the function.
      
      TestMatrix[i,j] <- round(TestMatrix[i,j],0) 
    }
  }
  
  return(TestMatrix)
}

EuroMillions()

