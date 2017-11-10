# https://docs.python.org/3/library/xml.html
# https://docs.python.org/3/library/xml.etree.elementtree.html
TESTDECK = 'xmlTestFile.xml'

# GENERIC METHODS THAT MIGHT BE USEFUL LATER

def openTag(tagName):
    return '<' + tagName + '>'

def closeTag(tagName):
    return '</' + tagName + '>'

def countTags(tagName):
    f = open(TESTDECK)
    c = 0
    for line in f:
        if openTag(tagName) in line:
            c = c + 1
    f.close()
    return c

# JUST SOME JUNK FOR PRACTICE

def getDeckName():
    # location of deckName in xml file: deck/name

    inDeck = False
    inName = False
    
    f = open(TESTDECK)
    for line in f:
        if inDeck == False:
            if openTag('deck') in line:
                print('deck')
                #stoppedhere
    f.close()
#    return deckName

def findLocation(location):
    # given a path tag1/tag2/tag3
    # return the line number
    # test with /cards/card[@id='1']/side1

    # parse location into a list
    locationList = []
    currentWord = ''
    for i in range(len(location)):
        print(location[i])
        #stoppedhere
    
    return 12345

# MAIN

print(countTags('card'))
getDeckName()
print(findLocation('/cards/card[@id=''1'']/side1'))
