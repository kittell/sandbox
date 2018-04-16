# switch for working on home vs work computer...
mac <- TRUE

stop <- FALSE
stopAndGo <- function() {
  # Stop time to grab plots and drawings during loops, but only if
  # the global variable 'stop' is TRUE
  if (stop) {
    invisible(readline(prompt="Press [enter] to continue"))
  }
}

image.vector.to.matrix <- function(image.vector) {
  
}

image.matrix.to.vector <- function(image.matrix) {
  
}

hw8.col <- function(image.side, i, j) {
  c <- image.side * (noise.df[(2*i)-1, j] - 1) + noise.df[2*i, j]
}

load.supplement <- function(supplement.file) {
  # Shortcut for loading the various supplemental files
  # How to return two objects: https://stackoverflow.com/a/15140507/752784
  supplement.df <- read.csv(supplement.file, header=TRUE)
  rownames(supplement.df) <- supplement.df[,1]
  supplement.df <- supplement.df[,-1]
  supplement.df <- supplement.df + 1    # Account for files being zero-indexed
}

image.bin.draw <- function(image.vector) {
  # Inspiration: https://stackoverflow.com/a/5638655/752784
  side <- sqrt(length(image.vector))
  # Convert to 0, 255 values
  image.vector[image.vector<=0] <- 0
  image.vector[image.vector>0] <- 255
  image.matrix <- matrix(image.vector, nrow=side, ncol=side, byrow=FALSE)
  # Flip matrix to view it correctly in image()
  image(image.matrix[,ncol(image.matrix):1], useRaster=TRUE, axes=FALSE)
  stopAndGo()
}

image.bin.draw.all <- function(image.all) {
  for (i in 1:nrow(image.all)) {
    image.bin.draw(unlist(image.all[i,], use.names=FALSE))
  }
}

if (mac) {
  setwd('/Users/kirkkittell/Dropbox/CS498AML/HW8')
  noise.file <- 'SupplementaryAndSampleData/NoiseCoordinates.csv'
  update.file <- 'SupplementaryAndSampleData/UpdateOrderCoordinates.csv'
  Q.file <- 'SupplementaryAndSampleData/InitialParametersModel.csv'
} else {
  setwd('C:\\Users\\sd931e\\Documents\\kwk\\cs498aml\\HW8')
  noise.file <- 'SupplementaryAndSampleData\\NoiseCoordinates.csv'
  update.file <- 'SupplementaryAndSampleData\\UpdateOrderCoordinates.csv'
  Q.file <- 'SupplementaryAndSampleData\\InitialParametersModel.csv'
}

data.file <- 'mnist_train_20.csv'
mnist.df <- read.csv(data.file, header=FALSE)
mnist.labels <- mnist.df[,1]
mnist.df <- mnist.df[,-1]

# Convert upper half of (0:255) to +1, lower half to -1
mnist.df.bin <- mnist.df
mnist.df.bin[mnist.df.bin<128] <- -1
mnist.df.bin[mnist.df.bin>=128] <- 1

# Draw the original images
#image.bin.draw.all(mnist.df.bin)

# Add noise to the dataset
noise.df <- load.supplement(noise.file)
mnist.df.noisy <- mnist.df.bin

# Flip bits
image.side <- sqrt(ncol(mnist.df))
for (i in 1:(nrow(noise.df)/2)) {
  for (j in 1:ncol(noise.df)) {
    r <- i
    c <- hw8.col(image.side, i, j)
    mnist.df.noisy[r, c] <- -1 * mnist.df.noisy[r, c]
  }
}

# Draw the noisy images
image.bin.draw.all(mnist.df.noisy)

# Denoise the images
update.df <- load.supplement(update.file)
Q.initial <- as.matrix(read.csv(Q.file, header=FALSE))
Q <- list()
