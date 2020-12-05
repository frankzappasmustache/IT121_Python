"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: final.py
    Author: Dustin McClure
    Lab: Final Exam
    Modified Date: 12/03/2020

    Python Final Exam
"""
import csv
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

print("\tReading file into list...\n")
stockindex = []
with open("stockIndex.csv", "r") as csvfile:
    csvread = csv.reader(csvfile)

    for row in csvread:
        print(row[0], row[1])
        stockindex.append(row)

print("\tThe data in the list...\n")
print(stockindex)

print("\tDrawing the data...\n")
x1 = int(0)
y1 = int(0)
plt.figure(figsize=(30, 30), dpi=80, facecolor='w', edgecolor='k')
for row in stockindex:
    x = int(row[0])
    y = int(row[1])
    if y < y1:
        #plt.scatter(x,y, color='blue')
        plt.plot([x, y], color='red', linestyle='dashed', label='Indexlow')
    elif y > y1:
        #plt.scatter(x,y, color='blue')
        plt.plot([x, y], color='green', linestyle='solid', label='Indexhigh')
    #plt.subplots_adjust(top=0.972, bottom=0.096, left=0.031, right=0.992, hspace=0.25, wspace=0.25)
    x1 = int(x)
    y1 = int(y)
print("\tDrawing the graph...\n")
plt.title('Stock Index Plot')
plt.xlabel('Days')
plt.ylabel('Stock Index')
plt.show()
