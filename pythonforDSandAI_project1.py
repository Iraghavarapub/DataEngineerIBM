#Press Shift+Enter to run the code
class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('!', '').replace(',','').replace('.','').replace('?','')
        # make text lowercase
        formattedText= formattedText.lower()
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split()
        
        # Create dictionary
        freqMap={}
        for word in set(wordList):
            freqMap[word] = wordList.count(word)
        return freqMap
           
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
       
         
givenstring="lorem is my friend"       
analyzed = TextAnalyzer(givenstring)
print("Formatted Text:", analyzed.fmtText)
word= 'lorem'
freqWord = analyzed.freqOf(word)
print("the Word",word,"appears",freqWord,"Times")