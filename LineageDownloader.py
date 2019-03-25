import json
import urllib
import urllib.request
import os
import sys
import hashlib
import time
import ssl

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

# Begin SSL Cache Session
context = ssl._create_unverified_context()

file = open("devices.txt", "r")
for i in file:
	devicename = i.split(" ")[0]

	if not os.path.exists("./" + devicename):
		os.makedirs("./" + devicename)

	contents = urllib.request.urlopen("https://download.lineageos.org/api/v1/" + devicename + "/nightly/autodownloader", context=context).read()
	data = json.loads(contents.decode('utf-8'))["response"]
	print("\n=================================")
	print("Number of builds: " + str(len(data)))
	print("Device: " + devicename)
	print("---------------------------------")
	for n in data:
		print("Downloading " + n["filename"] + "...", end=" ", flush=True)
		filedata = urllib.request.urlopen(n["url"], context=context)
		structuredfiledata = filedata.read()

		# Write Files
		with open("./" + devicename + "/" + n["filename"], "wb") as f:
			f.write(structuredfiledata)
		print("Done!", flush=True)

		# Write SHAs
		with open("./" + devicename + "/" + n["filename"] + ".sha256", "wt") as f:
			f.write(n["id"] + " " + n["filename"])

		# Calculate shas
		print("Calculating SHA256... ", end=" ", flush=True)
		sha256 = hashlib.sha256()
		with open("./" + devicename + "/" + n["filename"], 'rb') as f:
			while True:
				BUF = f.read(BUF_SIZE)
				if not BUF:
					break
				sha256.update(BUF)
		if sha256.hexdigest() == n["id"]:
			print("Done!", flush=True)
		else:
			print("DIGEST MISSMATCH!", flush=True)
			sys.exit("DIGEST MISSMATCH " + sha256.hexdigest + " != " + n["id"])

	print("=================================")
time.sleep(10)
