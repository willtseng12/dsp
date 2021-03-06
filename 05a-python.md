# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both python lists and tuples can store different data types. However, lists are mutable while tuples are not. Tuples will work as keys and list will not since keys need to be non-mutable, otherwise refering to values within a dictionary can become problematic

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both python lists and sets are iterable and mutable. Sets support mathematical operations such as union and intersection. Main difference is that there are no duplicate items within a set while it can in a list. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is an annoymous function typically used to execute simple task on items. This is used instead of the traditional way to declare a function. For example, `sorted(['ac', 'da', 'bz'], key = lambda   x: x[1]` in python will return: 
   ```python
   ['da', 'ac', 'bz']
   # sorted by the second letter of each string  
   ```
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> list comprehension is a simple and natural way to create lists in python (the same ges with set comprehension, dictionary comprehension).
   ```python
   s = [x**2 for x in range(5) if x < 4]
   print(s)
   ```
   will return  
   ```python
   [0, 1, 4]
   ```
   set comprehension:
   ```python
   t = {x**2 for x in range(5) if x < 4}
   print(t)
   ```
   will	return	
   ```python
   {0,1,4}
   ```
   dictionary comprehension:
   ```python
   u = {x :x**2 for x in range(5) if x < 4 }
   print(u)
   ```
   will return
   ```python
   {0:0, 1:1, 2:4}
   ```
   the same thing can be done with `map`. Here it transforms the original list to another list by calling the lambda function on each item in the list:
   ```python
   list(map(lambda x: x**2, [0,1,2]))
   ```
   this will return:
   ```python
   [0,1,4]
   ```	
   `filter` can do the similar thing as well as list comprehension. Here it filter another list that only contains number less than 4:
   ```python
   list(filter(lambda x: x<4, [0,1,2,3,4,5]))
   ```
   this will return:
   ```python
   [0,1,2,3]
   ```
   The list comprehension is more syntactically friendly since you don't need to input in a lambda function. But depending on the situation a `map` or a `filter` may be more appropriate to the situation.

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.
  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.
  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





