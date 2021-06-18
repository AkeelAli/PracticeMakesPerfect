

def get_max_element(arr):
	"""
	>>> get_max_element([1, 2, 3, 4, 5])
	5
	>>> get_max_element([-1, 6, -3])
	6
	"""
	max_i = float('-inf')
	for i in arr:
		if i > max_i: 
			max_i = i

	return max_i

	#return max(arr)

def rrc_v1(s):
	new_s = s[0]
	for c in s[1:]:
		if c != new_s[-1]:
			new_s += c
	return new_s

def rrc_v2(s):
	l = list(s)
	shift = 0
	for i in range(1,len(l)):
		if l[i] == l[i-1]:
			shift += 1
		else:
			l[i-shift] = l[i]
	return ''.join(l[:-shift])

def remove_repeated_chars(s):
	"""
	>>> remove_repeated_chars("abcddeefgf")
	'abcdefgf'
	"""
	return rrc_v2(s)
