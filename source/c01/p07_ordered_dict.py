#

'''
Topic:排序字典
'''
from collections import OrderedDict
import json

def ordered_dict():
	d = OrderedDict()
	d['foo'] = 1
	d['bar'] = 2
	d['spam'] = 3
	d['grok'] = 4
	for key in d:
		print(key, d[key])
	return d

if __name__ == '__main__':
	d = ordered_dict()
	print(json.dumps(d))

