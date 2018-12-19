import sys
import _thread

def isPrime(sequence=100):
    current_num = 2;
    th = 1;
    while(True):
        isPrime = True;
        for divider in range(2,current_num-1):
            if current_num%divider==0:
                isPrime = False;
                break;
        if isPrime:
            if th == sequence:
                break;
            th += 1;
        current_num +=1;
    print(current_num);

_thread.start_new_thread(isPrime, (1999, ));
_thread.start_new_thread(isPrime, (5, ));

while 1:
        break;
