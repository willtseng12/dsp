[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

```python
#Suppose you draw a sample with size n = 10 from an exponential distribution 
#with λ = 2. Simulate this experiment 1000 times and plot the 
#sampling distribution of the estimate L. Compute the standard error of 
#the estimate and the 90% confidence interval.

#Repeat the experiment with a few different values of n and make a plot of 
#standard error versus n.

def Simul_exponential(n=10, m=1000):
    """
    Sampling distribution of L as an estimator of exponential parameter.

    lam: parameter of an exponential distribution
    n: sample size
    iters: number of iterations
    """
    def VertLine(x, y=1): # function for vertical line
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)
        
    lam = 2
    means = []
    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        means.append(L)
    
    
    stderr = RMSE(means, lam) # standard deviation of the sampling distribution
    print('standard error :', stderr)
    
    cdf = thinkstats2.Cdf(means)
    ci = cdf.Percentile(5), cdf.Percentile(95) # lower and upper bounds for CI
    VertLine(ci[0], y=1) #LB
    VertLine(ci[1], y=1) #UB
    print('confidence interval :', ci)
             
    thinkplot.Pdf(thinkstats2.Cdf(means))
    thinkplot.Config(xlabel='estimate',
                     ylabel='CDF',
                     title='Sampling distribution')
    
    return stderr
    
def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates] # predicted - actual
    mse = np.mean(e2)
    return math.sqrt(mse)

Simul_exponential()
```
