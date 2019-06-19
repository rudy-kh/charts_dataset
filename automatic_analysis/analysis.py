
import json
import numpy as np
import argparse
from itertools import combinations

parser = argparse.ArgumentParser()
parser.add_argument("-data", required=True)

args = vars(parser.parse_args())


def get_x_y(filename):
	"""
	Function for extracting only the information needed to analyze the data, return a dict for every plot,
	including the values of x axis, y axis, plot type, plot title

	:param filename: name of annotations.json file, which follows a certain format
	:type filename: str
	"""
	with open(filename) as f:
		data = json.load(f)

	xy = {}
	
	for i,k in enumerate(data):
		x = k["models"][0]["x"]
		y = k["models"][0]["y"]
		title = k["general_figure_info"]["title"]["text"]
		x_order_info = k["models"][0]["x_order_info"]
		plot_type = k["type"] # "vbar_categorical"
		xy[i+1] = {"x":x, "y":y, "title":title,"type":plot_type, "x_order_info": x_order_info}

	return xy


data_ext = get_x_y(args["data"])

# <x_axis_label_highest_value>, <x_axis_label_Scnd_highest_value>, <x_axis_label_3rd_highest_value>, <x_axis_label_least_value>, 

# <y_axis_highest_value_val>, <y_axis_Scnd_highest_val>, <y_axis_3rd_highest_val>, <y_axis_least_value_val>

def get_stat_info(data):
	"""
	Calculate simple statistical information about the data for each plot
	Return keys and values to be added to the according dictionary belonging of each plot

	:param data: information about each plot individually
	:type data: dict
	"""
	
	# what labels in the annotated descriptions can be mapped to directly from the calculations?
	x, y = data["x"], data["y"]
	# min/max
	# <x_axis_label_highest_value>, x_axis_label_3rd_highest_value
	# <y_axis_highest_value_val>
	y_max_idx = np.argmax(y)
	x_max, y_max = x[y_max_idx], y[y_max_idx]

	y_min_idx = np.argmin(y)
	x_min, y_min = x[y_min_idx], y[y_min_idx]
	
	# mean
	mean = np.mean(data["y"])

	# sorted axes, according to descending y values
	y_sorted, x_sorted = (list(t) for t in zip(*sorted(zip(y,x),reverse=True)))
	#print(x_sorted,"\n",y_sorted)
	labels = {}
	# labels for ordered x and y
	anno_size_x = ["<x_axis_label_highest_value>", "<x_axis_label_Scnd_highest_value>", "<x_axis_label_3rd_highest_value>", "<x_axis_label_4th_highest_value>","<x_axis_label_5th_highest_value>","<x_axis_label_least_value>"]

	anno_size_y = ["<y_axis_highest_value_val>", "<y_axis_Scnd_highest_val>", "<y_axis_3rd_highest_val>", "<y_axis_label_4th_highest_value>","<y_axis_label_5th_highest_value>", "<y_axis_least_value_val>"]

	n = len(x) - 2 # -1 for max, -1 for min
	anno_size_x2 = anno_size_x[:n+1]
	anno_size_x2.append(anno_size_x[-1])
	anno_size_y2 = anno_size_y[:n+1]
	anno_size_y2.append(anno_size_y[-1])

	label_name_pairs_x = {e[0]:e[1] for e in zip(anno_size_x2,x_sorted)}
	label_value_pairs_y = {e[0]:e[1] for e in zip(anno_size_y2,y_sorted)}

	# label <x_axis_label_count> is the number of categories on the x axis
	label_count = len(x)
	misc = {"<x_axis_label_count>":label_count}
	
	# pairwise differences
	# Are categories more often compared to the extrema? 

	times = {"label": "<y_axis_inferred_value>","pairs":{}}
	# To interpret this dict: (c1, c2): 5 -> c1 has a value about 5 times larger than c2
	# OR: c2 has a value 5 times smaller than c1
	
	plus = {"label": "<y_axis_inferred_value>","pairs":{}}
	# To interpret this dict: (c1, c2): 13 -> c1 has a value that is 13 [unit] larger than c2
	# OR: c2 has a value 13 [unit] smaller than c1
	x_combin, y_combin = list(combinations(x_sorted,2)), list(combinations(y_sorted,2))
	for i,pair in enumerate(x_combin):
		k = y_combin[i][0] // y_combin[i][1] # floor division, result rounded down int
		times["pairs"][pair] = k
		
		d = y_combin[i][0] - y_combin[i][1] # difference
		plus["pairs"][pair] = d
	
	differences = {"plus":plus, "times":times}

	return data["title"], data["x_order_info"],differences, label_name_pairs_x,label_value_pairs_y, misc

d1 = data_ext[1]
print("BASIC INFORMATION")
for i in range(1,len(data_ext)+1):
	print(data_ext[i])
	print("\n")


print("---- INFORMATION FROM EXTRA PREPROCESSING -- EXAMPLE")

title,order_info, differences, label_name_pairs_x, label_value_pairs_y, misc = get_stat_info(d1)
print("TITLE",title)
print("X axis order info",order_info)
for e,v in differences.items():
	print(e)
	for n,m in v.items():
		print(n,m)
	print("\n")

for e,v in label_name_pairs_x.items():
	print(e,v)
print("\n")
for e,v in label_value_pairs_y.items():
	print(e,v)
print("\n")
for e,v in misc.items():
	print(e,v)



