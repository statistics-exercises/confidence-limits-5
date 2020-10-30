import matplotlib.pyplot as plt
import numpy as np

def uniform_discrete(a,b) :
  # Your code to generate the uniform discrete random variable goes here
  
  
def n_uniform_discrete( n, a, b ) : 
  # You code to generate the sum of n uniform discrete random variables goes here
  
  
def sample_mean( m, n, a, b ) : 
  # Your code to calculate the mean of m sums of n uniform discrete random variables
  # goes here


# This loop generates the resamples 
mym, myn, mya, myb = 20, 2, 1, 6
indices, resamples = np.zeros(10), np.zeros(10) 
for i in range(10) :
  # Your code to generate all the resamples goes here
  # you will also need to set the elements of indices in here
  
  

plt.plot( indices, resamples, "ko" )
plt.savefig('resamples.png')
