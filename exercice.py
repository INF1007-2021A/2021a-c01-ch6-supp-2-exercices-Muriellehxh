#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_even_keys(dictionary):
	list_yeet = []
	for key in dictionary:
		if key % 2 == 0:
			list_yeet.append(key)

	set_yeet = set(list_yeet)

	return set_yeet

def join_dictionaries(dictionaries):
	full_dict = {}
	for d in dictionaries:
		for key in d:
			full_dict[key] = d[key]

	return full_dict


def dictionary_from_lists(keys, values):
	if len(keys)<len(values):
		n1 = len(keys)
		del values[n1:]
	else:
		n1 = len(values)
		del keys[n1:]

	n = 0
	new_dict = {}
	while n < len(keys):
		new_dict[keys[n]] = values[n]
		n += 1

	return new_dict

def get_greatest_values(dictionnary, num_values):
	list_val = []
	for ind in dictionnary:
		list_val.append(dictionnary[ind])
	list_val = sorted(list_val, reverse=True)
	if num_values == 1:
		n = list_val[0]
		return [list_val[0]]
	return list_val[:num_values]


def get_sum_values_from_key(dictionnaries, key):
	list_sum = []
	for dic in dictionnaries:
		if key in dic:
			n = dic[key]
			list_sum.append(dic[key])


	return sum(list_sum)


if __name__ == "__main__":
	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	print(get_even_keys(yeet))
	print()

	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	doot = {
		0xBEEF: "doot",
		0xDEAD: "DOOT",
		0xBABE: "dOoT"
	}
	print(join_dictionaries([yeet, doot]))
	print()
	
	doh = [
		"D'OH!",
		"d'oh",
		"DOH!"
	]
	nice = [
		"NICE!",
		"nice",
		"nIcE",
		"NAIIIIICE!"
	]
	print(dictionary_from_lists(doh, nice))
	print()
	
	nums = {
		"nice": 69,
		"nice bro": 69420,
		"AGH!": 9000,
		"dude": 420,
		"git gud": 1337
	}
	print(get_greatest_values(nums, 1))
	print(get_greatest_values(nums, 3))
	print()

	bro1 = {
		"money": 12,
		"problems": 14,
		"trivago": 1
	}
	bro2 = {
		"money": 56,
		"problems": 406
	}
	bro3 = {
		"money": 1,
		"chichis": 1,
		"power-level": 9000
	}
	print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
	print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
	print()
