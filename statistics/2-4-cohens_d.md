[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```python
import nsfg
import math

#Using the variable 'totalwgt_lb', investigate whether first babies are 
#lighter or heavier than others.
#Compute Cohen’s effect size to quantify the difference 
#between the groups. How does it compare to the difference 
#in pregnancy length?

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1] #live births
firsts = live[live.birthord == 1] #first live births
others = live[live.birthord != 1] #non first live births

def Cohen_Effect_Size(group1, group2):
    """Computes Cohen's effect size for two groups.
    
    group1: Series or DataFrame
    group2: Series or DataFrame
    
    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()
    var1, var2 = group1.var(), group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1*var1 + n2*var2)/ (n1 + n2)
    return diff / math.sqrt(pooled_var)

print(Cohen_Effect_Size(firsts.totalwgt_lb, others.totalwgt_lb))
print(Cohen_Effect_Size(firsts.prglngth, others.prglngth))

# One discovers that the Cohen effect size is positive for pregnancy length
# but negative for total weight. The magnitude of the two values are both 
# relatively small: perhaps too small for us to say there is a consistent
# difference in these varaibles between the two groups

```
