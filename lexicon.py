class lexicon(object):

    def __init__(self):
        self.scan_database={'directions' : ['north', 'south', 'west', 'east', 'down', 'up', 'left', 'right', 'back'],
                            'verbs' : ['go', 'kill', 'eat', 'stop'],
                            'stops' : ['the', 'in', 'of', 'from', 'at', 'it'],
                            'nouns' : ['bear', 'princess', 'door', 'cabinet'],
                            'numbers' : [range(10)]
} # It's the corpus.
        
        self.results = [] # the output of your script.
        self.the_words = the_words

    def scan(self the_words):

        the_words  = the_words.split(" ")
        
        for i in the_words:#the classifier
            if i in self.scan_database['directions']:
                i = ( 'directions', i )

            elif i in self.scan_database['verbs']:
                i = ( 'verbs', i)

            elif i in self.scan_database['stops']:  
                i = ( 'stops', i)

            elif i in self.scan_database['nouns']:  
                i = ( 'nouns', i)

            elif i in self.scan_database['numbers'] or type(i) is int == True:  
                i = ( 'numbers', i)

            else:  
                i = ( 'error', i)
            
            self.results.append(i)
