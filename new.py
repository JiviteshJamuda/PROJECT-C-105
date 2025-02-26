import csv
import pandas as pd
import plotly.express as px
import math

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data :
        total += int(x)
    
    mean = total/n
    return mean

# squareing and getting the values
squared_list = []
for num in data :
    a = int(num)-mean(data)
    a = a**2
    squared_list.append(a)

# getting sum
sum = 0
for i in squared_list :
    sum = sum + i

# divide sum by total values
result = sum/(len(data)-1)

deviation = math.sqrt(result)
print(deviation)