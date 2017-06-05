# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

import datetime
dstart = datetime.datetime.strptime(date_start, '%m-%d-%Y').date()
dstop = datetime.datetime.strptime(date_stop, '%m-%d-%Y').date()
(dstop - dstart).days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

import datetime
date_start = datetime.datetime.strptime('12312013','%m%d%Y').date()
date_stop = datetime.datetime.strptime('05282015','%m%d%Y').date()
(date_stop - date_start).days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

import datetime
date_start = datetime.datetime.strptime('15-Jan-1994','%d-%b-%Y').date()
date_stop = datetime.datetime.strptime('14-Jul-2015','%d-%b-%Y').date()
(date_stop - date_start).days
