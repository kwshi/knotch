#!/usr/bin/env python3

# Basic language components
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
hundred = 'hundred'
_and = 'and'
zero = 'zero'
negative = 'negative'

def kilo(n):
	# Chunks of three
	text = str(n)
	kilos = len(text)//3 + 1 # Powers of thousand (of power of thousand, heh)
	zfill = text.zfill(len(text)//3*3 + 3)
	chunks = [zfill[i:i+3] for i in range(0, len(zfill), 3)]
	del text, zfill

	groups = [] # Word groups

	# Per chunk
	for chunk in chunks: # Per 3-digit chunk
		group = [] # Initiate current segment group
		queue = '' # Conjunctive letter queue (mn, sx)

		# Ones place
		if chunk[:2] == '00': # Under 10
			if chunk[2] == '1': group.append('mi')
			elif chunk[2] == '2': group.append('bi')
			elif chunk[2] == '3': group.append('tri')
			elif chunk[2] == '4': group.append('quadri')
			elif chunk[2] == '5': group.append('quinti')
			elif chunk[2] == '6': group.append('sexti')
			elif chunk[2] == '7': group.append('septi')
			elif chunk[2] == '8': group.append('octi')
			elif chunk[2] == '9': group.append('noni')
		else: # Regular Conway Wechsler
			if chunk[2] == '1': group.append('un')
			elif chunk[2] == '2': group.append('duo')
			elif chunk[2] == '3':
				group.append('tre')
				queue += 'sx'
			elif chunk[2] == '4': group.append('quattuor')
			elif chunk[2] == '5': group.append('quin')
			elif chunk[2] == '6':
				group.append('se')
				queue += 'sx'
			elif chunk[2] == '7':
				group.append('septe')
				queue += 'mn'
			elif chunk[2] == '8': group.append('octo')
			elif chunk[2] == '9':
				group.append('nove')
				queue += 'mn'

			def conjunction(chars): # Test & add conjunctive characters
				nonlocal queue, group
				for c in chars:
					if c in queue:
						group += c
				queue = ''

			# Tens
			if chunk[1] == '1':
				conjunction('n')
				group.append('deci')
			if chunk[1] == '2':
				conjunction('ms')
				group.append('viginti')
			elif chunk[1] == '3':
				conjunction('ns')
				group.append('triginta')
			elif chunk[1] == '4':
				conjunction('ns')
				group.append('quadraginta')
			elif chunk[1] == '5':
				conjunction('ns')
				group.append('quinquaginta')
			elif chunk[1] == '6':
				conjunction('n')
				group.append('sexaginta')
			elif chunk[1] == '7':
				conjunction('n')
				group.append('septuaginta')
			elif chunk[1] == '8':
				if group and group[-1] == 'tre': # Special case
					group += 's'
					queue = ''
				else: conjunction('mx')
				group.append('octoginta')
			elif chunk[1] == '9': group.append('nonaginta')

			# Hundreds place
			if chunk[0] != '0':
				if chunk[0] == '1':
					if group and group[-1] == 'tre': group += 's' # Special case
					else: conjunction('nx')
					group.append('centi')
				elif chunk[0] == '2':
					conjunction('n')
					group.append('ducenti')
				elif chunk[0] == '3':
					conjunction('ns')
					group.append('trecenti')
				elif chunk[0] == '4':
					conjunction('ns')
					group.append('quadringenti')
				elif chunk[0] == '5':
					conjunction('ns')
					group.append('quingenti')
				elif chunk[0] == '6':
					conjunction('n')
					group.append('sescenti')
				elif chunk[0] == '7':
					conjunction('n')
					group.append('septingenti')
				elif chunk[0] == '8':
					if group and group[-1] == 'tre': # Special case
						group += 's'
						queue = ''
					else: conjunction('mx')
					group.append('octingenti')
				elif chunk[0] == '9': group.append('nongenti')

		if groups and not group: # "ni"llion
			group.append('ni')
		if group: # Make sure group has something
			if group[-1][-1] == 'a': group[-1] = group[-1][:-1] + 'i' # Prevent "-allion"
			group.append('lli')
			groups.append(''.join(group)) # Append group to groups

	if groups: return ''.join(groups) + 'on'
	else: return 'thousand' # Zero-index!