# rpn calculator v2, rebuilt for Oython 3 removing dependency on deanishe's alfred workflow library

import re
import sys
import json

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def calc(ops):
	stack = []
	for i in range(len(ops)):
		if is_number(ops[i]):
			stack.append(float(ops[i]))
		elif ops[i]=='+':
			stack.append(stack.pop()+stack.pop())
		elif ops[i]=='-':
			n = stack.pop()
			stack.append(stack.pop()-n)
		elif ops[i]=='*':
			stack.append(stack.pop()*stack.pop())
		elif ops[i]=='/':
			n = stack.pop()
			stack.append(stack.pop()/n)
		elif ops[i]=='':
			pass 
	return stack

def produceOutput(theString): 
	result = {"items": []}
	# Add items to Alfred feedback with uids so Alfred will track frequency of use
	
	ops = [y.replace(' ','') for y in re.split('\s|(?<!\d)[,.]|[,.](?!\d)',theString)]
	resultString = str(calc(ops)[0])	
	result["items"].append({
		"title": resultString,
		"subtitle": "",
		"valid": True,
		"uid": "rpn-result",
		"icon": {
			"path": "icon.png"
		},
		"arg": resultString
			})
	return result
	
def main():
	if len(sys.argv) > 0:
		theString = sys.argv[1]
		myReplacementString = json.dumps(produceOutput(theString))	
		
		sys.stdout.write(myReplacementString)
		sys.stdout.flush()
		
	else:
		theString = sys.argv[1] 
		produceOutput (theString)
		
if __name__ == '__main__':
	main()


				