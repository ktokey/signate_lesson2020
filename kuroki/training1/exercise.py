# coding: utf-8

import pandas as pd
import numpy as np
# import pdb
import matplotlib.pylab as plt


def exercise1():
	name = np.array(['Yamada Taro', 'Yamada Hanako', 'Wakayama Dai'])
	height = np.array([172.5, 160.5, 180.2])
	age = np.array([21, 19, 30])
	labels = ['name', 'height', 'age']

	d_dataframe = pd.concat([
		pd.Series(name, name=labels[0]),
		pd.Series(height, name=labels[1]),
	], axis=1)
	print(d_dataframe)

	d_dataframe = pd.concat([d_dataframe, pd.Series(age, name=labels[2])], axis=1)
	print(d_dataframe)


def exercise2():
	a = np.array([[1, 3, 2], [-1, 0, 1], [2, 3, 0]])
	a_inv = np.linalg.inv(a)
	print(a_inv)
	print(np.matmul(a, a_inv))


def exercise3(values):
	print(values)
	print([1 if i >= 5 else -1 for i in values])


if __name__ == '__main__':
	exercise1()
	exercise2()
	exercise3([10, 3, 1, 5, 8, 6])
