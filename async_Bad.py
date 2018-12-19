import asyncio
import time

def isPrime(sequence):
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

    # return current_num;
    print(current_num);

async def isPrime_Async(sequence):
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

    return current_num;

async def isPrime_Async_caller(l):
    input_list = l;

    coroutines = [isPrime_Async(sequence) for sequence in input_list];
    completed, pending = await asyncio.wait(coroutines);
    for i in completed:
        print(i.result());

if __name__ == '__main__':
    input_list = [199, 5, 190, 2, 450, 3, 190];

    tic = time.process_time() #strat timer
    event_loop = asyncio.get_event_loop();
    try:
        event_loop.run_until_complete(isPrime_Async_caller(input_list));
    finally:
        event_loop.close();
    toc = time.process_time() #stop Timer
    print("Async method processtime: ",toc-tic);

    tic = time.process_time() #strat timer
    for i in input_list:
        isPrime(i);
    toc = time.process_time() #stop Timer
    print("Async method processtime: ",toc-tic);
