#PA3

import sys
import os

from Crypto.Hash import SHA256

def main():
	block_size = 1024

	file_target = "./1.mp4"
	hash_target = ""

	h0_target = calculate_hash(file_target, block_size)
	h0_target_hex = h0_target.encode('hex')
	print "h0(",file_target,"):",h0_target_hex

	
def calculate_hash(file_path, block_size):
	file_size = os.path.getsize(file_path)
	last_block_size = file_size % block_size

	print "size(",file_path, "):",file_size,"bytes"
	fp = open(file_path, 'rb')
	last_hash = ''
	
	for chunk in read_reversed_chunks(fp, file_size, last_block_size, block_size):
		sha256 = SHA256.new()
		sha256.update(chunk)
		if(last_hash):
			sha256.update(last_hash)
		last_hash = sha256.digest()
	fp.close()

	return last_hash


def read_reversed_chunks(file_object, file_size, last_chuck_size, chunk_size):
	iter = 0
	last_pos = file_size
	while last_pos>0:
		size = chunk_size
		if(iter == 0):
			size = last_chuck_size

		file_object.seek(last_pos - size)
		data = file_object.read(chunk_size)
		if not data:
			break

		iter = iter + 1
		last_pos -= size
		yield data

main()