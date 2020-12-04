# The final exam is a take-home coding project. Use whatever help you can find from anyone and anything. However you build this, to get credit you need to be able to explain it in line-by-line detail. And to get full credit it needs to work, it needs to be well commented, and it needs to be fairly well written. (See the rubric below.)

## It should look something like this when you run it:
https://btc.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9e72717c-a1d5-444e-a357-abdc01022b8a&start=undefined

### Program requirements:

    > - Print "Reading file into list..."
    > - Read the file stockIndex.csvPreview the document into a list in your program. (See the File I/O examples.)
    > - Print "The data in the list..."
    > - Print the list that contains the data.
    > - Print "Drawing the data..."
    > - Draw the data. The first field of each row is the day, the second field is the index amount. If the index amount went up, draw the line green. If the index amount went down, draw the line red. (I would use a FOR loop to get x and y coordinates from the list and use turtle or tkiner to draw the line to those coordinates.)
    > - Print "Drawing the graph..."
    > - Draw the x and y axis lines, unit markings, and labels. (Just turtle or tkinter drawing.)

## To build this, I would start by using these bullet points as the comments for your code. Then I would work from top to bottom to get each section working. I laid out the print statements in that order to make the programming easier, but if you would rather draw the graph lines and labels first and then write the data that works, too. You can earn partial credit for each section: reading the data into a list, drawing the data, and drawing the graph lines and labels. Drawing the graph is tedious can take a while to get it looking good so I would save drawing the graph lines and labels for last.

# File I/O Code Examples
```python
import csv

## Reading a csv file
with open("captains.csv", "r") as csvfile:
# creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        print(row[1],row[0])

## Reading a csv file into a list
shipCap=[]
with open("captains.csv", "r") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        shipCap.append(row)

## Print the shipsCaps list
for row in shipCap:
    print(row)

# Print the captain of the 3rd ship (multidimensional array, a list of lists)
print(shipCap[2][1])

# Add a ship,captain pair to the list

inShip=input("Ship? ")
inCap=input("Captain? ")
shipCap.append([inShip,inCap])
# Re-Print the shipsCaps list
for row in shipCap:
    print(row)

# Writing the revised csv file
with open("captains.csv", 'w',newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the rows
    csvwriter.writerows(shipCap)
```
