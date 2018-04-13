# switch for working on home vs work computer...
mac <- FALSE

stop <- TRUE
stopAndGo <- function() {
  # Stop time to grab plots and drawings during loops, but only if
  # the global variable 'stop' is TRUE
  if (stop) {
    invisible(readline(prompt="Press [enter] to continue"))
  }
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
} else {
  setwd('C:\\Users\\sd931e\\Documents\\kwk\\cs498aml\\HW8')
  noise.file <- 'SupplementaryAndSampleData\\NoiseCoordinates.csv'
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
noise.df <- read.csv(noise.file, header=TRUE)
rownames(noise.df) <- noise.df[,1]
noise.df <- noise.df[,-1]
noise.df <- noise.df + 1    # Account for noise.file being zero-indexed
mnist.df.noisy <- mnist.df.bin

# Flip bits
image.side <- sqrt(ncol(mnist.df))
for (i in 1:(nrow(noise.df)/2)) {
  for (j in 1:ncol(noise.df)) {
    r <- i
    c <- image.side * (noise.df[(2*i)-1, j] - 1) + noise.df[2*i, j]
    mnist.df.noisy[r, c] <- -1 * mnist.df.noisy[r, c]
  }
}

# Draw the noisy images
image.bin.draw.all(mnist.df.noisy)

