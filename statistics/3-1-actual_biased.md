[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python
import thinkstats2
import thinkplot
import nsfg


#Exercise: Something like the class size paradox appears if you survey 
#children and ask how many children are in their family. 
#Families with many children are more likely to appear in your sample, 
#and families with no children have no chance to be in the sample.
#Use the NSFG respondent variable numkdhh to construct the actual 
#distribution for the number of children under 18 in the 
#respondents' households.

#Now compute the biased distribution we would see if we surveyed 
#the children and asked them how many children 
#under 18 (including themselves) are in their household.
#Plot the actual and biased distributions, and compute their means.

#the variable 'numkdhh' is the number of children below 18. It's gonna 
#become the key for the pmfs

resp = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label = 'actual numkdhh')

def BiasPmf(pmf, label):
    '''
    given a pmf, scale (multiply) the probability of each observation
    by the key of that observation.
    '''
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

biased_pmf = BiasPmf(pmf, label = 'observed numkdhh')
thinkplot.PrePlot(1)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='number of children', ylabel='PMF')

print('unbiased_mean', pmf.Mean())
print('biased_mean', biased_pmf.Mean())
```
