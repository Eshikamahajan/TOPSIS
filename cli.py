# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 09:43:51 2020

@author: Eshika Mahajan
"""

import argparse
from example import *

def main():
	# create argument parser object 
	parser = argparse.ArgumentParser(description = "Topsis using python") 
  
	parser.add_argument("-n", "--name", type = str, nargs = 1, 
	                    metavar = "name", default = None, help = "Name of csv file with extension") 

	parser.add_argument("-w", "--weight", type = str, nargs = 1, 
	                    metavar = "weight", default = None, help = "Weights of attribute") 

	parser.add_argument("-i", "--impact", type = str, nargs = 1, 
	                    metavar = "impact", default = [1], help = "Impact of attribute") 

	# parse the arguments from standard input 
	args = parser.parse_args()

	filename=args.name
	weight=[int(w) for w in args.weight[0].split(',')]
	impact=[int(im) for im in args.impact[0].split(',')]
	topsis_exp1(filename[0],weight,impact)


if __name__ == "__main__":
	main()