from crackhead import Methametic as meth

eq = "100x+50=3+x";

op_list = "+-*/=";
var_list = "x";
num_list = "0123456789";

eq_list = [];
prev_chr = "";
fullNum = [];

for c, i in enumerate(eq):
    if i in op_list:
        if len(fullNum) != 0:
            eq_list.append("".join(fullNum));
        eq_list.append(i);
        fullNum = [];

    if i in var_list:
        if len(fullNum) != 0:
            eq_list.append("".join(fullNum));
            if prev_chr in num_list:
                eq_list.append("*");
        eq_list.append(i);
        fullNum = [];

    if i in num_list:
        fullNum.append(i);
        if c == len(eq)-1:
            eq_list.append(fullNum);
    prev_chr = i;

print(eq_list);
