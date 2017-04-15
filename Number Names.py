#Number names coding challenge by Dan Jones
import math

#Takes in a number and splits it at every 3 pos just how we write numbers like: 1,000
def splitInto3(number:int) -> []:
	result = []
	number = str(number)
	i = 0
	while i < len(number):
		#This is to get the "1" out of 1,000 as there are not 3 characters before the 1
		if i == 0 and len(number) % 3 != 0:
			result.append(int(number[0: len(number)%3]))
			#Important! Stops it from looping again if the number is less than 3 digits
			if len(number) <= 3:
				i = 3
			i+=1
		else:
			result.append(int(number[i:i+3]))
			i += 3

	return result

#This takes the "one hundred fifty three" and appends on the position it is such as million
def numStringAddDegree(string, degr):
	if degr == 0:
		return string
	
	if string == "zero" and degr == 0:
		return string
	elif string == "zero":
		#This is so we don't have it saying "zero" in random points
		return ""

	if degr > 101: #For numbers wayyy too big...
		return string

	#List of all the big numbers... There seams to be a pattern after writing them all out but I'm not going to re do it all after typing it out.
	degree = {1: "thousand",
		2: "million",
		3: "billion",
		4: "trillion",
		5: "quadrillion",
		6: "quintillion",
		7: "sextillion",
		8: "septillion",
		9: "octillion",
		10: "nonillion",
		11: "decillion",
		12: "undecillion",
		13: "duodecillion",
		14: "tredecillion",
		15: "quattuordecillion",
		16: "quindecillion",
		17: "sexdecillion",
		18: "septendecillion",
		19: "octodecillion",
		20: "novemdecillion",
		21: "vigintillion",
		22: "unvigintillion",
		23: "duovigintillion",
		24: "trevigintillion",
		25: "quattuorvigintillion",
		26: "quinvigintillion",
		27: "sexvigintillion",
		28: "septenvigintillion",
		29: "octovigintillion",
		30: "novemvigintillion",
		31: "trigintillion",
		32: "untrigintillion",		
		33: "duotrigintillion",
		34: "tretrigintillion",
		35: "quattuortrigintillion",
		36: "quintrigintillion",
		37: "sextrigintillion",
		38: "septentrigintillion",
		39: "octotrigintillion",
		40: "novemtrigintillion",		
		41: "quadragintillion",
		42: "unquadragintillion",
		43: "duoquadragintillion",		
		44: "trequadragintillion",
		45: "quatturoquadragintillion",
		46: "quinquadragintillion",
		47: "sexquadragintillion",
		48: "septenquadragintillion",
		49: "octoquadragintillion",
		50: "novemquadragintillion",
		51: "quinquagintillion",
		52: "unquinquagintillion",
		53: "duoquinquagintillion",
		54: "quattuorquinquagintillion",
		55: "quattuorquinquagintillion",
		56: "quinquinquagintillion",
		57: "sexquinquagintillion",
		58: "septenquinquagintillion",
		59: "octoquinquagintillion",
		60: "novemquinquagintillion",
		61: "sexagintillion",
		62: "unsexagintillion",
		63: "duosexagintillion",
		64: "tresexagintillion",
		65: "quattuorsexagintillion",
		66: "quinsexagintillion",
		67: "sexsexagintillion",		
		68: "septensexagintillion",
		69: "octosexagintillion",
		70: "novemsexagintillion",
		71: "septuagintillion",
		72: "unseptuagintillion",
		73: "duoseptuagintillion",
		74: "treseptuagintillion",
		75: "quattuorseptuagintillion",
		76: "quinseptuagintillion",
		77: "sexseptuagintillion",
		78: "septenseptuagintillion",
		79: "octoseptuagintillion",
		80: "novemseptuagintillion",
		81: "octogintillion",
		82: "unoctogintillion",
		83: "duooctogintillion",
		84: "treoctogintillion",
		85: "quattuoroctogintillion",
		86: "quinoctogintillion",
		87: "sexoctogintillion",
		88: "septenoctogintillion",
		89: "octooctogintillion",
		90: "novemoctogintillion",
		91: "nonagintillion",
		92: "unnonagintillion",
		93: "duononagintillion",
		94: "trenonagintillion",
		95: "quattuornonagintillion",
		96: "quinnonagintillion",
		97: "sexnonagintillion",
		98: "septennonagintillion",
		99: "octononagintillion",
		100: "novemnonagintillion",
		101: "centillion"}

	return string + " " + degree[degr]

#This function takes a digit ant turns it into text version
#This is to prevent code repetition for handaling decimals
def digitToString(num : int) -> str:
	if len(str(num)) > 1:
		return "Error"
	
	#Store the word equivilant
	units = {"0": "zero",
		"1": "one",
		"2": "two",
		"3": "three",
		"4": "four",
		"5": "five",
		"6": "six",
		"7": "seven",
		"8": "eight",
		"9": "nine"}
	
	return units[num]

#This takes a 3 digit integer in and turns it into the word quivilant
def numToString(num : int):
	#Ensure only 3 letters
	if len(str(num)) > 3:
		return "Error"

	#Don't need to do any other code if zero
	if num == 0:
		return "zero"

	#Store the word equivilant
	teens = {"11": "eleven",
		"12": "twelve",
		"13": "thirteen",
		"14": "fourteen",
		"15": "fitheen",
		"16": "sixteen",
		"17": "seventeen",
		"18": "eighteen",
		"19": "nineteen"}

	tens = {"1": "ten",
		"2": "twenty",
		"3": "thirty",
		"4": "fourty",
		"5": "fifty",
		"6": "sixty",
		"7": "seventy",
		"8": "eighty",
		"9": "nighty"}

	hundred = "hundred"

	num = str(num)
	result = ""

	#Deal with the hundreds first
	if len(num) == 3:
		if int(num[0]) > 0:
			result += digitToString(num[0]) + " " + hundred + " "

	#used so we don't and five at the end of fithteen
	doUnits = True
	#Deal with the tens
	if len(num) >= 2:
		i = 0
		if len(num) == 3:
			i = 1

		#Sort out if we are dealing with a teen here
		if int(num[i]) == 1 and int(num[i]) > 0 and int(num[i+1]) > 0:
			result += teens[num[i] + num[i+1]]
			doUnits = False
		elif int(num[i]) > 0:
			result += tens[num[i]] + " "

	#Appending units if necesarry
	if doUnits and int(num[len(num) - 1]) > 0:
		result += digitToString(num[len(num) - 1])

	return result

#This function takes in a number and returns the word equivilant of it
def toNumName(num : int) -> str:
	result = ""

	if str(num)[0] == "-":
		num *= -1
		result += "minus "

	#Splits num into blocks of 3 digits
	num = splitInto3(num)
	
	#Go through each of blocks minus the last one
	for i in range(0, len(num) - 1, 1):
		#Add the string equivilant of that number to the result
		result += numStringAddDegree(numToString(num[i]), len(num) -1 -i) + " "

	#This is so that if the last block is zero the zero is removed unless the number is not bigger than zero
	if num[len(num) - 1] != 0:
		result += numToString(num[len(num) -1])
	elif len(num) == 1:
		result += numToString(num[len(num) -1])

	return result

#This splits up a number and returns it as an array of the integer part and the decimal part
def getIntAndDecParts(num) -> []:
	return [int(i) for i in str(num).split(".")]

#This is to handel floats
def toNumNameWithDecimals(num: str):
	result = ""
	#Get the integer and decimal part of float
	num = getIntAndDecParts(num)
	intPart = num[0]
	decPart = 0
	#If no decimal part len(num) == 1
	if len(num) > 1:
		decPart = num[1]

	#Convert integer part
	result += toNumName(intPart)

	#Convert decimal part if necisary
	if decPart > 0:
		result += " point"
		
		for i in str(decPart):
			result += " " + digitToString(i)

	return result

print(toNumNameWithDecimals(input("Number: ")))
