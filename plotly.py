#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt, mpld3
import statistics as stat
import math

with open('140621_0_distiled.txt') as f:
    lines = [int(line.strip()) for line in f]

if lines:
   lines.pop(0)


def Average(lst):
    return int(reduce(lambda a, b: a + b, lst)) / len(lst)

def valueTransformS(num):
   return int(pow(10,6)*(1/((pow(num,2)*0.00001)-(num*0.23)+(4950000/num)+940)))

def valueTransformO(num):
   return int((pow(num,2)*0.00001)-(num*0.23)+(4950000/num)+940)

def result():
   string = """<!DOCTYPE html>
             <html>
	        <head>
		   <title>CondStat 1.0</title>
                   <meta charset="UTF-8">
	        </head>
	        <body>
	 	   <h2>Calculated mediane: {}uS/cm</h2>
		   <h2>Average: {}uS/cm</h2>
                   <a href="figure1.html">Graph</a>
	        </body>
             </html>""".format(median,avg)

   file = open("/var/www/html/140621_0_distiled.html","w")
   file.write(string)
   file.close()

median = valueTransformO(int(stat.median(lines)))
avg = valueTransformO(Average(lines))

result()

print("Median:" + str(median) + " Avg:" + str(avg))

print(' '.join(map(str, lines)))

fig = plt.figure()
obj, = plt.plot(lines,'-', lw=2)
mpld3.save_html(fig,"/var/www/html/140621_0_distiled_fig.html")

