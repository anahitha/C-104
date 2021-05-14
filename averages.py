import csv
from collections import Counter

#getting data
with open('SOCR-HeightWeight.csv', newline='') as f: #newline = '' means \n doesn't come
    data = csv.reader(f)
    fdata = list(data)
fdata.pop(0)
ndata = []
for i in range(len(fdata)):
    num = fdata[i][2]
    ndata.append(float(num))

#mean    
length = len(ndata)
count = 0
for i in ndata:
    count = count+i
mean = count/length
print(mean)

#median
ndata.sort()
if length%2 == 0:
    num1 = float(ndata[length//2])
    num2 = float(ndata[length//2-1])
    median = (num1+num2)/2
else:
    median = ndata[length/2]
print(median)

#mode
d = Counter(ndata)
ranges = {"100-110": 0,"110-120": 0, "120-130": 0, "130-140": 0, "140-150": 0}
for height, occurence in d.items():
    if 100 < float(height) < 110:
        ranges["100-110"] += occurence
    elif 110 < float(height) < 120:
        ranges["110-120"] += occurence
    elif 120 < float(height) < 130:
        ranges["120-130"] += occurence
    elif 130 < float(height) < 140:
        ranges["130-140"] += occurence
    elif 140 < float(height) < 150:
        ranges["140-150"] += occurence

mrange, moccurence = 0, 0
for range, occurence in ranges.items():
    if occurence > moccurence:
        mrange = [int(range.split("-")[0]), int(range.split("-")[1])]
        moccurence = occurence
mode = float((mrange[0] + mrange[1]) / 2)
print(mode)