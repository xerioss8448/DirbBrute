#!/usr/bin/python3
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url", help="Specify url")
parser.add_argument("-w","--wordlist", help="Specify a wordlist")
args = parser.parse_args()

w = open(args.wordlist, "r")


if args.url and args.wordlist:
	url = args.url

	wordlist = (w.readlines())
	wLen = (len(wordlist))

	for i in range(wLen):
		t = wordlist[i].replace("\n", "")
		response = requests.get(url + t)
		r = str(response)

		if "2" in r:
			print("/" + t, "-->", url + t)
else:
	print('Missing arguments, syntax : python3 DirBrut.py -u <url> -w <wordlist>')
