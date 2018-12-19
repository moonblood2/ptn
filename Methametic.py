class Methametic:
    def __init__(self, deep_mode_on = False):
        self.deep_mode_on = deep_mode_on;

    def isPrime(self, CheckNumber):
        if CheckNumber <2:
            return False;
        for divider in range(2,CheckNumber-1):
            if(CheckNumber%divider == 0):
                return False;
        return True;
