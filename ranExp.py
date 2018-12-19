import random

# loop = int(input());
# rag = int(input());
#
# avg = [];
#
# l = 1000;
# for i in range(l):
#     TheDict = {};
#     for i in range(loop):
#         inp = str(random.randint(0,rag));
#         if inp not in TheDict:
#             TheDict[inp] = 1;
#         else:
#             TheDict[inp] += 1;
#
#     dupCount = 0;
#     for i in TheDict:
#         if TheDict[i] > 1:
#             dupCount+=1;
#     avg.append(dupCount);
#
# sum = 0;
# for i in avg:
#     sum+=i;
#
# print((sum/l)/loop);

win = 666666;
many = 10000000;
mylotto = [];
while len(mylotto) < many:
    lotto = random.randint(0,win);
    mylotto.append(lotto);

c = 0;
for i in mylotto:
    if i == win:
        c+=1;

print("Winning Number: ", win)
print("yout lotto:", mylotto);
if c > 0:
    print("!!!YOU WON!!!! ", c, "of lotto.");
else:
    print("!!!EAT shit!!!!");
