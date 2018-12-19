from multiprocessing.dummy import Pool as ThreadPool

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

    return [sequence, current_num];

input_list = [1990, 5, 1980, 2, 4570, 3, 1990];

pool = ThreadPool(4);
results = pool.map(isPrime, input_list);

pool.close();
pool.join();

results_dict = {};
for i in results:
    results_dict[i[0]] = i[1];

print(results_dict);
