import random

TheDict = {};

command_list = "showlist";

inp = input();
while(inp != "exit"):

    if inp == "random":
        print("random mode:");
        rag = int(input());
        for i in range(rag):
            inp = str(random.randint(0,100));
            if inp not in TheDict:
                TheDict[inp] = 1;
            else:
                TheDict[inp] += 1;

    if inp not in command_list:
        if inp not in TheDict:
            TheDict[inp] = 1;
        else:
            TheDict[inp] += 1;

    if inp == "showlist":
        print(TheDict);

    if inp == "dupCount":
        dupCount = 0;
        for i in TheDict:
            if TheDict[i] > 1:
                dupCount+=1;
        print(dupCount);

    inp = input();
