image.bin.draw <- function(image.vector) {
  # Inspiration: https://stackoverflow.com/a/5638655/752784
  side <- sqrt(length(image.vector))
  # Convert to 0, 255 values
  image.vector[image.vector<=0] <- 0
  image.vector[image.vector>0] <- 255
  image.matrix <- matrix(image.vector, nrow=side, ncol=side, byrow=TRUE)
  image(image.matrix, useRaster=TRUE, axes=FALSE)
}

setwd('/Users/kirkkittell/Dropbox/CS498AML/HW8')
data.file <- 'mnist_train_20.csv'
mnist.df <- read.csv(data.file, header=FALSE)
mnist.labels <- mnist.df[,1]
mnist.df <- mnist.df[,-1]

# Convert upper half of (0-255) to +1, lower half to -1
mnist.df.bin <- mnist.df
mnist.df.bin[mnist.df.bin<128] <- -1
mnist.df.bin[mnist.df.bin>=128] <- 1

for (i in 1:nrow(mnist.df.bin)) {
  image.bin.draw(unlist(mnist.df.bin[i,]))
}