[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

```python
import hinc2
import hinc
import thinkstats2
import thinkplot
import numpy as np
import math

#log sample

income_df = hinc.ReadData()
log_sample = hinc2.InterpolateSample(income_df)
log_cdf = thinkstats2.Cdf(log_sample)
thinkplot.Cdf(log_cdf)
thinkplot.Config(xlabel = 'Household income (log $)',
                 ylabel = 'Cdf',
                 title = 'Log income Cdf')
thinkplot.Show()

# sample

sample = np.power(10, log_sample)
cdf = thinkstats2.Cdf(sample)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel = 'Household income ($)',
                 ylabel = 'Cdf',
                 title = 'Income Cdf')
thinkplot.Show()


# the first raw moment (k = 1) is the mean
def RawMoment(xs, k):
    return sum(x**k for x in xs) / len(xs)

# the second central moment (k = 2) is the variance
def CentralMoment(xs, k):
    mean = RawMoment(xs, 1)
    return sum((x - mean)**k for x in xs) / len(xs)

def Median(xs):
    cdf = thinkstats2.Cdf(xs)
    return cdf.Value(0.5) 

# skewness calcuated based off of difference between mean and median
def PearsonMedianSkewness(xs):
    median = Median(xs)
    mean = RawMoment(xs, 1)
    var = CentralMoment(xs, 2)
    std = math.sqrt(var)
    gp = 3 * (mean - median) / std
    return gp

# a standardized moment is typically a higher degree central moment that has
# been normalized
def StandardizedMoment(xs, k):
    var = CentralMoment(xs, 2)
    std = math.sqrt(var)
    # std**k : square root of the second moment to the kth power
    return CentralMoment(xs, k) / std**k

# skewness is the 3rd standardized moment
def Skewness(xs):
    return StandardizedMoment(xs, 3)

print('Mean:', RawMoment(sample, 1))
print('Median:', Median(sample))
print('Skewness:', Skewness(sample))
print('Pearson Median Skewness:', PearsonMedianSkewness(sample))



# side note on how to visualize density plot through KDE

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
density = gaussian_kde(log_sample)
xs = np.linspace(0,10,200) # x-axis
density.set_bandwidth(0.25) # change badnwidth
plt.plot(xs,density(xs))
plt.show()

```
