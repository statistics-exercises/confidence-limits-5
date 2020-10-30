# Introduction to resampling

We are now going to write our first program to resample a mean.  We will compute the random variable given by the expression below:

![](https://render.githubusercontent.com/render/math?math=\overline{Y}=\frac{1}{m}\sum_{i=1}^{m}\sum_{j=1}^{n}X_{ij})

In this expression, each of the ![](https://render.githubusercontent.com/render/math?math=X_{ij}) is a uniform discrete random variable that lies between a and b.  An expression similar to this one would be used to calculate the average value that we get when we roll n fair dice m times.  This random variable is the mean that we calculated in the programming exercise before the previous one.  __Now, however, instead of generating one of these random variables we are going to generate 100 of them.  We are then going to plot all these random variables on a graph.__ 

To complete this task you will need to write three functions:

1. `uniform_discrete` - takes two arguments `a` and `b` in input.  It should return a uniform discrete random variable that is greater than or equal to `a` and less than or equal to `b`.
2. `n_uniform_discrete` - takes three arguments `n`, `a` and `b`.  It should return the sum of `n` uniform discrete random variables that are greater than or equal to `a` and less than or equal to `b`.  Notice that you can call `uniform_discrete` in this function.
3. `sample_mean` - takes four arguments in input `m`, `n`, `a` and `b`.  It should generate `m` sums of `n` uniform discrete random variables that are greater than or equal to `a` and less than or equal to `b`.  It then should calculate a sample mean from these `m` random variables.  In other words, this function should return a random variable that is generated using the formula on this page.  Please note that you may want to include calls to `n_uniform_discrete` in this function.

Once you have completed these three you will then need to write the internal part of the loop at the end of the code.  This is the part of the code that generates the resamples of the mean.  Within this loop you will need to set the elements of two arrays:

1. `indices` - the first element of this array should be set equal to one, the second element should be set equal to two, the third equal to three and so on
2. `resamples` - the elements of this array should be random variables that are generated using the formula that appears on this page.  To pass the tests the value of `m` in the expression should be set equal to `mym`, the value of `n` should be set equal to `myn`, the value of `a` should be set equal to `mya` and the value of `b` should be set equal to `myb`.

When the exercise is complete a graph will be generated with 10 random variables generated using the above formula on it.  


