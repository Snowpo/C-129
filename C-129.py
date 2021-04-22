import pandas
import csv

file1 = 'bright_stars.csv'
file2 = 'converted_stars.csv'

d1 = []
d2 = []

with open(file1,'r') as f:
    csvfile = csv.reader(f)
    for i in csvfile:
        d1.append(i)

with open(file2,'r') as f:
    csvfile = csv.reader(f)
    for i in csvfile:
        d2.append(i)

h1=d1[0]
h2=d2[0]

p1 = d1[1:]
p2 = d2[1:]

h=h1+h2
p = []

for i in p1:
    p.append(i)

for i in p2:
    p.append(i)

with open('total_stars.csv','w') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p)

df=pandas.read_csv('total_stars.csv')
df.tail()