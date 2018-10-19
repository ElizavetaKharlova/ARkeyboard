from datetime import datetime

class Timer:
    
    '''
        This class starts the timer and returns the remaining time.
        '''
    
    def __init__(self):
        self.nSecond = 0
        self.totalSec = 30
        self.startTime = datetime.now()
        self.timeElapsed = 0.0

    def getRemainingTime(self):
        timeElapsed = (datetime.now()-self.startTime).total_seconds()
        timeElapsed = int(timeElapsed)

        timeRemaining = self.totalSec - timeElapsed
        
        return timeRemaining
