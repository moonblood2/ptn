from crackhead import Methametic as meth


str = "abc (24 314 83 383)(-256)sa 0 (24 314) 1";
inBasket = meth.getMemberinBasket("(",")",str)

print(str);
print(inBasket);

str_cut = str;
for i in inBasket:
    str_cut = str_cut.replace(("("+i+")"), "");

str_cut = str_cut.split();
print(str_cut);

str_dict = {};
for i in inBasket:
    str_dict[i] = str.index(i);
for i in str_cut:
    str_dict[i] = str.index(i)

print(str_dict);
