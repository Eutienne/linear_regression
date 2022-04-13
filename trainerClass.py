#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
import numpy as np

class Trainer:
	
	"""
			Constructor
	"""
	def __init__(self, file):
		self.theta0, self.theta1, = 0.0, 0.0
		self.km_norm, self.pr_norm, self.learningRate = 0.0, 0.0, 0.0
		self.mse = []
		with open(file, "r") as f:
			lines = f.readlines()[1:]
		data = []
		for line in lines:
			data.append([int(s) for s in line.rstrip().split(',') if s.isdigit()])
		self.mileage, self.price = zip(*data)

	"""
			Hypothesis
	"""
	def estimatePrice(self, mileage):
		return self.theta0 + (self.theta1 * mileage)
	
	"""
			Give the Average of a list
	"""
	def Average(self, lst):
		return sum(lst) / len(lst)

	"""
			Give the elements to Calculate Pearson's Correlation Coefficient
	"""
	def Relements(self, xAverage, yAverage):
		tmpx, x2, tmpy, y2, sumxy = 0.0, 0.0, 0.0, 0.0, 0.0
		for index in range(len(self.mileage)):
			tmpx = self.mileage[index] - xAverage
			tmpy = self.price[index] - yAverage
			x2 += tmpx * tmpx
			y2 += tmpy * tmpy
			sumxy += tmpx * tmpy
		length = len(self.price)
		return sumxy / length, x2 / length, y2 /length

	"""
			Give back the LearningRate by Pearson's Correlation Coefficient
			############################################# 
			#               _          _                # Pearson's Correlation Coefficient
			#          ∑(Xi−X⎯⎯⎯⎯) • (Yi−Y⎯⎯⎯⎯)             # Pearson's Correlation Coefficient
			#                                           # Pearson's Correlation Coefficient
			#  r =    ----------------------            # Pearson's Correlation Coefficient
			#            _              _               # Pearson's Correlation Coefficient
			#      √∑(Xi−X⎯⎯⎯⎯)² •  √∑(Yi−Y⎯⎯⎯⎯)²           # Pearson's Correlation Coefficient
			#############################################
	"""

	def setLearningRate(self):
		xAverage = self.Average(self.mileage)
		yAverage = self.Average(self.price)
		sumxAverage, x2Average, y2Averege = self.Relements(xAverage, yAverage)
		self.learningRate = sumxAverage / math.sqrt(x2Average * y2Averege) * -1
	
	def denormalize(self):
		xMax = float(max(self.mileage))
		xMin = float(min(self.mileage))
		yMax = float(max(self.price))
		yMin = float(min(self.price))
		self.theta1 *= ((yMax - yMin) / (xMax - xMin))
		self.theta0 = ((yMax - yMin) * self.theta0) + (self.theta1 * (1 - xMin) +yMin)

	def normalize(self, data):
		minVal = float(min(data))
		maxVal = float(max(data))
		newList = []

		for i in data:
			newList.append(float (i - minVal) / (maxVal - minVal))
		return newList

	def train(self):
		tmp0, tmp1, tmp2 = 0.0, 0.0, 0.0
		self.km_norm = self.normalize(self.mileage)
		self.pr_norm = self.normalize(self.price) 
		for i in range(len(self.mileage)):
			tmp0 += self.estimatePrice(self.km_norm[i]) - self.pr_norm[i] 
			tmp1 += (self.estimatePrice(self.km_norm[i]) - self.pr_norm[i]) * self.km_norm[i]
			tmp2 += (self.estimatePrice(self.km_norm[i]) - self.pr_norm[i]) *  (self.estimatePrice(self.km_norm[i]) - self.pr_norm[i])
		self.mse.append(float(tmp2 / len(self.mileage)))
		
		self.theta0 -= self.learningRate * tmp0/len(self.mileage)
		self.theta1 -= self.learningRate * tmp1 / len(self.price)
	
		
		