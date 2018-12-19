import queue
import threading

def isPrime(q, sequence):
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

    q.put(print(sequence,"th :",current_num));

q = queue.Queue();

input_list = [1999, 5, 1998, 2, 4557, 3, 199];
for i in input_list:
    t = threading.Thread(target=isPrime, args = (q,i));
    t.daemon = True;
    t.start();

threadInfo_total = threading.active_count();
threadInfo_list = threading.enumerate();

for i in range(len(input_list)):
    q.get();

print("Number of thread(not stable) :", threadInfo_total);
for counter, thread_name in enumerate(threadInfo_list):
    print("Thread ",counter,": ", thread_name);
