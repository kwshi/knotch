#!/usr/bin/env python3
from . import language as lang

def split(n): # Split into chunks of three
	# Negative numbers
	negative = False
	if n < 0:
		negative = True
		n *= -1

	text = str(int(n))
	kilos = len(text)//3 + 1 # Powers of thousand
	zfill = text.zfill(kilos * 3)
	chunks = [zfill[i:i+3] for i in range(0, len(zfill), 3)]

	if chunks and chunks[0] == '000': # Remedy custom zerofill
		del chunks[0]
		kilos -= 1

	return kilos, chunks, negative

def knot(n):
	kilos, chunks, negative = split(n)
	groups = [] # Word groups

	# Per chunk
	for chunk in chunks: # Per 3-digit chunk
		group = [] # Initiate current word group

		# Hundreds place
		if chunk[0] != '0':
			group.append(lang.ones[int(chunk[0]) - 1])
			group.append(lang.hundred)

		# And
		if chunk[1:3] != '00' and (group or groups): # Something after 'and' (in this group) & something before 'and'
			group.append(lang._and)

		# Tens & teens
		if chunk[1] == '1': # Teens
			group.append(lang.teens[int(chunk[2])])
		else: # Regular tens
			if chunk[1] != '0': group.append(lang.tens[int(chunk[1]) - 2])

			# Ones place
			if chunk[1] != '0' and chunk[2] != '0': # Case for hyphens
				group[-1] += '-'
				group[-1] += lang.ones[int(chunk[2]) - 1]
			elif chunk[2] != '0': # No hyphens
				group.append(lang.ones[int(chunk[2]) - 1])

		# Power of thousands suffix
		if chunk != '000':
			if kilos > 1: group.append(lang.kilo(kilos - 2))

		kilos -= 1 # Decrement thousands
		if group: groups.append(' '.join(group)) # Append group to groups

	if groups:
		y = ', '.join(groups)
		if negative: y = lang.negative + ' ' + y

		return y
	else: return lang.zero # Zero!
