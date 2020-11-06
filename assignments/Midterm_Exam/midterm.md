The midterm exam is a take-home coding project. Use whatever help you can find from anyone and anything, just like real life. You can even ask Siri or Alexa; they may be telling Apple and Amazon everything you're doing but they won't rat you out to your instructor. However you build this, to get credit you need to be able to explain it in line-by-line detail. And to get full credit it needs to work, it needs to be well commented, and it needs to be fairly well written. (See the rubric below.)

Program requirements:

Start with a map that looks like this:
classHrs = {"class1":0, "class2":0, "class3":0}

Note - It is possible for the tasks described below to be completed with three variables instead of three key:data pairs in a map. But we are using maps in the midterm because they will allow us to store and update a varying amount of data as we start using loops in the second half of the course. Flexible data structures like maps are also necessary when reading data from files or writing output to files, a skill you will practice in future courses.

Ask the user how many hours they should spend on each class. Put each of these answers in the appropriate place in the classHrs map. It could look something like this, but feel free to use your own words:
How many hours should you spend in a week on your first class? (User enters a number)

How many hours should you spend in a week on your second class? (User enters a number)

How many hours should you spend in a week on your third class? (User enters a number)

Ask the user how many days per week they plan to study and put the answer in a variable.
Ask the user how many hours they are actually studying each day and put that answer in a variable.
Add up all the hours in the map and divide the total by the number of days per week that the user plans to study.
Report out your results to one decimal place. It could look something like this:
You should spend an average of 2.7 hours per day studying.

If the number of hours per day actually studying is greater than the number of hours per day you should be studying then say something like this:
You are probably studying enough.

If the number of yours per day actually studying is less than the number of hours per day you should be studying then say something like this:
You should probably study some more each day.



That's it! It sounds a little complicated but if you write your comments out first and fill in the code underneath each comment then it goes together pretty simply. Just use the pieces of the labs you've already done; no need to use FOR loops or anything fancy. It will mostly be several input and print commands that access the classHrs map data and other variables with an IF statement at the end.

-------

A few tips about coding
Good software development follows a cycle
  Research  -> Design  -> Code  -> Test

A lot of the Research and Design can be done up front. You can ask yourself the following questions and think about them to build a plan before you start coding. In fact, many programmers use the answers to these questions as the comments in their code. They start with the comments, and then write the code.:

What is the input?
How will I store the data?
What will the output be?
How do I transform the input into the output? Will I need to make decisions (IF)? Will I need to perform calculations or conversions?
After you have a plan the Code -> Test cycle should be done over and over in little chunks. Don't code it all at once. (Agile development.)

***Start with the most simple code. Get that working. Then add a little more functionality. Get that working. Build your program in simple, easy steps from a simple easy start so you build a strong foundation and know when you hit an error.***

Two analogies are sometimes helpful:
1 - Adding code to a program is like adding salt to food. You want to do it a little at a time so you don't ruin it.

2 - Building a program is like building a house.

Put thought into the design.
Start with a strong and simple foundation.
Build up incrementally.
