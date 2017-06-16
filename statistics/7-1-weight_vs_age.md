[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

```python
import thinkstats2
import first
import thinkplot
import numpy as np

#Using data from the NSFG, make a scatter plot of birth weight versus 
#mother’s age.

live, firsts, others = first.MakeFrames()
live = live.dropna(subset = ['agepreg', 'totalwgt_lb']) #drop NA values

thinkplot.Scatter(live.agepreg, live.totalwgt_lb, alpha=0.2)
thinkplot.Show(xlabel = 'mother age (years)', 
               ylabel = 'birth weight (lb)', 
               legend ='')

#Plot percentiles of birth weight versus mother’s age. 

def Binned_Percentile(df):
    
    bins = np.arange(10, 48, 3) # create a range object [10, 48) increments of 3
    indices = np.digitize(df.agepreg, bins) # categorize each obs into bin index
    groups = live.groupby(indices) #groupby object that contains len(groups) dataframes
    
    momAge = [group.agepreg.mean() for i, group in groups] #avg. mom age for each dataframe
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups] #cdf for each
    
    for degree in [75,50,25]:
        weights = [cdf.Percentile(degree) for cdf in cdfs]
        label = '%dth' % degree
        thinkplot.Plot(momAge, weights, label = label)
    thinkplot.Show(xlabel = 'mother age (years)',
                   ylabel = 'birth weight (lb)',
                   legend = True)
        
Binned_Percentile(live)


#Compute Pearson’s and Spearman’s correlations. How would you character-ize 
#the relationship between these variables?

print(thinkstats2.Corr(live.agepreg, live.totalwgt_lb))
print(thinkstats2.SpearmanCorr(live.agepreg, live.totalwgt_lb))

# The two variables are likely to be non linearly correlated as the Pearson
# Correlation coefficient and Spearman coefficient are both low

```
