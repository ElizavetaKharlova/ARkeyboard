import numpy as np

class leaderboard:
    
    '''
        This class creates a leaderboard.
        '''

    results = []
    resultsN = []
    
    def __init__(self):
#        self.name = name
#        self.score = str(score)
        self.names = open("names.txt", "w+")
        self.names.close()
        self.scores = open("scores.txt", "w+")
        self.scores.close()

    def getRank(self, name, score):
        '''
            This function sorts the names and scores in order.
            '''
        names = open("names.txt", "a+")
        names.write(name + "\n")
        names.close()
        scores = open("scores.txt", "a+")
        scores.write(str(score) + "\n")
        scores.close()
        namesRead = open("names.txt", "r")
        resultsN = namesRead.readlines()
        scoresRead = open("scores.txt", "r")
        resultsScores = scoresRead.readlines()
        ind = np.argsort(resultsScores)[::-1]
        resultsScores.sort(reverse=True)
        resultsNames = []
        for i in range(len(resultsN)):
            resultsNames.append(resultsN[ind[i]])

        return resultsNames, resultsScores


