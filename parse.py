#!/usr/bin/scl enable rh-python36 -- python
def open_file(file_path):
	out_data=""
	with open(str(file_path)) as f:
		out_data=f.read()
	return out_data
print(open_file("parse.py"))
