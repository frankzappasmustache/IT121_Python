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

print("\tReading file into list...\n")
stockindex = []
with open("stockIndex.csv", "r") as csvfile:
    csvread = csv.reader(csvfile)

    for row in csvread:
        stockindex.append(row)

print("\tThe data in the list...\n")
print(stockindex)

print("\tDrawing the data...\n")
x1 = int(0)
y1 = int(0)
for row in stockindex:
    x = int(row[0])
    y = int(row[1])

    if y < x:
        plt.plot(x, y, color='red', linestyle='dashed', linewidth=2, marker='o',
             markerfacecolor='blue', markersize=10, label="Index Amount")
    elif y >= x:
        plt.plot(x, y, color='green', linestyle='solid', linewidth=2, marker='o',
             markerfacecolor='blue', markersize=10, label="Index Amount")

print("\tDrawing the graph...\n")
plt.xlabel('Days')
plt.ylabel('Stock Index')
plt.title('Stock Index Plot')
plt.legend()
plt.show()
