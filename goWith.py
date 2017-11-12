# CONSTANTS
RECIPEDATABASE = 'recipe-database.xml'
RECIPENAME = 'recipe-name'

# METHODS
def getRecipeList():
	recipeList = []
	startRecipeName = False
	endRecipeName = False
	with open(RECIPEDATABASE) as f:
		for line in f:
			if startRecipeName == False:
				if ('<' + RECIPENAME + '>') in line:
					startRecipeName = True
					recipeName = ''
				if startRecipeName == True and endRecipeName == False:
					# get text after <recipe-name> tag
					# TBD: just add line for now, but parse out text later
					recipeList.append(line)
					
				if ('</' + RECIPENAME + '>') in line:
					startRecipeName = False
					endRecipeName = True
					recipeName = ''
	
	return recipeList
	

def turnStringIntoList(inputString):
	 # DESCRIPTION: 
	 # INPUT: Comma-separated string of ingredients
	 # OUTPUT: List of ingredients
	 # DEPENDENCIES: none
	 
	 # TODO: make appending to list a separate function, protect against adding
	 #	extra spaces, comma at end, blank entries, etc.
	
	inputList = []
	i = 0
	entry = ''
	for c in range(0, len(inputString)):
		if inputString[c] == ',':
			inputList.append(entry)
			entry = ''
		else:
			entry = entry + inputString[c]
		i = i + 1
		
		# last character in string: add the entry
		if i == len(inputString):
			inputList.append(entry)
	return inputList

def findCandidates(inputList):
	# Get list of recipes (full recipes, template recipes)
	# Search through ingredient list
	# Return a list of candidates for user to choose
	
	candidateList = []
	with open(RECIPEDATABASE) as f:
		for line in f:
			#TBD: this is totally not doing anything useful at the moment
			candidateList.append(line)
	
	f.close()
	return candidateList

# MAIN

# Get list of ingredients to search in database
inputList = []
inputString = input("Enter comma-separated list of ingredients: ")
inputList = turnStringIntoList(inputString)

# Get a list of things from "the database" that match the ingredients
candidateList = []
candidateList = findCandidates(inputList)


# Show five to the user, ask for 1-5 input or more

# TESTING - show list of recipes
recipeList = []
recipeList = getRecipeList()
print(recipeList)
