[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```python
import brfss
import scipy.stats

#In the BRFSS (see Section 5.4), the distribution of heights is roughly 
#normal with parameters μ = 178 cm and σ = 7.7 cm for men, 
#and μ = 163 cm and σ = 7.3 cm for women.

#In order to join Blue Man Group, you have to be male 
#between 5’10” (≈177.8cm) and 6’1” (≈185.4cm)(see http://bluemancasting.com). 
#What percentage of the U.S. male population is in this range? 
#Hint: use scipy.stats.norm.cdf.

brfss = brfss.ReadBrfss()

maleHeight = brfss[brfss.sex == 1].htm3
                    
maleHeightAvg = maleHeight.mean()
maleHeightStd = maleHeight.std()


probLB = scipy.stats.norm.cdf(177.8, 
                              loc = maleHeightAvg, 
                              scale = maleHeightStd)
probUP = scipy.stats.norm.cdf(185.4, 
                              loc = maleHeightAvg, 
                              scale = maleHeightStd)

print(probUP - probLB)
```
