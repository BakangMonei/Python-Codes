import csv
import os
import time
import string
import random
import turtle

name = (str(input("Please enter your name: ")))
surname = (str(input("Please enter your name: ")))
print("Hello " + name + " " +surname + "! " + "Welcome to Ems Inc.")

estimatedDistance = (float(input("How far is your destination km: ")))
KM = 1000
convertion = estimatedDistance / KM
print("Your estimated distance in KM is %.2f km" %(convertion))

step = 0.7 # 1 step is == 0.7m
