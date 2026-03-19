def brackets_check(input):
	stack = ""
	for znak in input:
		if znak in ['(', '[', '{']:
			stack += znak
		if znak in [')', ']', '}']:
			if stack[-1] == znak:
			    stack = stack[:-1]
			else:
			    return False
	return True

if __name__ == "__main__":
