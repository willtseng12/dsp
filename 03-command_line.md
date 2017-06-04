# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd : show current directory  
    mkdir <directory anme> : create new directory  
    rm -r <directory name> : recursively deleting specified directory  
    touch : create a file  
    rm : remove a file  
    mv <original file> <new file name> : rename file  
    ls -a : list hidden files  
    ls -l : list files in long format  
    ls - t : list files ordered by last modified date  
    cp <file to be copied> <destinated directory> : copying a file from one directory to another

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls : refer to question 1  
    ls -a : refer to question 1  
    ls -l : refer to question 1  
    ls -lh : list long format in human readbale format  
    ls -lah : same as ls -lh plus hidden file  
    ls -t : refer to question 1
    ls -Glp : list everything i scurrent directory in long format, appending "directory fomat" as the the last info to the            long format, and specifying inhibitng group information.  
    

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -1  
    ls -r  
    ls -G  
    ls -m  
    ls -q

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs builds and accept command lines from standard input. 
One potentially good use of it is that it break down a potentially long list into sublist that is short enough for a command to operate on. For example, 'rm find /path -type f' may return an error message saying that the list of things returned by find is not executable (removable in this case). However, 'find /path -type f | xargs rm' will break the long list of items into sublists (each individual items) so that 'rm' will be able to execute each individual items accordingly.

 

