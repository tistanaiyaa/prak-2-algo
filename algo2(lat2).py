# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:00:17 2024

@author: Lenovo
"""
import math
lintang1 = math.radians (float(input("lintang kota 1: ")))
bujur1 = math.radians (float(input("bujur kota 1: ")))
lintang2 = math.radians (float(input("lintang kota 2: ")))
bujur2 = math.radians (float(input("bujur kota 2: ")))
R = 6371.0
lat = lintang2 - lintang1
long = bujur2 - bujur1
a = math.sin(lat/2)**2 + math.cos(lintang1)*math.cos(lintang2)*math.sin(long/2)**2
C = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
d = R * C
print("jarak antara dua titik tersebut adalah ", d, "kilometer")