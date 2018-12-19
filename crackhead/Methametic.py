import math
import random

def isPrime(CheckNumber):
    if CheckNumber <2:
        return False;
    for divider in range(2,CheckNumber-1):
        if CheckNumber%divider == 0:
            return False;
    return True;


def primeAt(at):
    if at <1 or type(2)!=type(at):
        raise Exception('Ensure your input');

    th = 0;
    num2check = 2;

    while at != th:
        if isPrime(num2check):
            th +=1;
        if at == th:
            return num2check;
        num2check +=1;


def factor(theNumber):
    def factor_process(theNumber):
        factor_list = [];
        for divider in range(2, theNumber-1):
            if theNumber%divider == 0:

                num1 = divider;
                num1_pCheck = isPrime(num1);
                if num1_pCheck:
                    factor_list.append(num1);
                else:
                    pass

                num2 = int(theNumber/divider);
                num2_pCheck = isPrime(num2);
                if num2_pCheck:
                    factor_list.append(num2);
                else:
                    factor_list.append(factor_process(num2));

                if num1_pCheck and num2_pCheck:
                    return factor_list;

        return factor_list[:2];

    def flatMultiDimensionList(string_list, list2enum, count):
        for i in list2enum:
            if type(i) != list:
                count+=1;
                string_list += str(i)+",";
            else:
                string_temp, list2enum, c_temp = flatMultiDimensionList(string_list, i, count);
                string_list += string_temp+",";
                count+=c_temp;
        return string_list, list2enum, count;

    factor_list = factor_process(theNumber);
    factor_list, _, count = flatMultiDimensionList("", factor_list, 0);
    list_lenght = len(factor_list);
    factor_list = factor_list.split(',')[:count];
    factor_list = factor_list[-int(math.sqrt(list_lenght)):]
    factor_list = [int(i) for i in factor_list];
    return factor_list;


def lcm(inputList):
    """
    lcm(x)
    x: List of Number
    return LCM
    """
    def memberCount(factorList):
        memberFrequency = {};
        for i in factorList:
            if i not in memberFrequency:
                memberFrequency[i] = 1
            else:
                memberFrequency[i] += 1

        return memberFrequency;

    numCount = [];
    for input in inputList:
        if not isPrime(input):
            factorOfnum = factor(input);
            numCount.append(memberCount(factorOfnum));
        else:
            numCount.append({input:1});

    lcm_list = {};
    for nc in numCount:
        for i in nc:
            if i not in lcm_list:
                lcm_list[i] = nc[i];
            elif nc[i] > lcm_list[i]:
                lcm_list[i] = nc[i];

    result = [];
    for i in lcm_list:
        for _ in range(lcm_list[i]):
            result.append(i);

    final_result = 1;
    for i in result:
        final_result*=int(i);

    return final_result;

def isCoprime(number, basenumber):
    if number > 1 and number < basenumber:
        if number not in factor(basenumber):
            return True;
    return False;

def RSA_createKey(level):
    p = primeAt(random.randint(level-50,level+100));
    q = primeAt(random.randint(level-50,level+100));
    n = p*q;

    l = lcm([p-1,q-1]);

    e = random.randint(2,l)
    while not isCoprime(e,l) or not isPrime(e):    # e and l has gcd == 1
        e = random.randint(2,l-1);

    d = 1;
    while (e*d)%l != 1:
        d+=1

    public_key = [n, e];
    private_key = [n, d];
    return public_key, private_key;

def RSA_DeEncrypt(key, msg):
    return (msg**key[1])%key[0];

def text2hex(text):
    hex_l = [];
    for c in text:
        hex_l.append(ord(c));
    return hex_l;

def hex2text(hex):
    text_l = [];
    for h in hex:
        text_l.append(chr(h));
    text_l = "".join(text_l);
    return text_l;

def RSA_encryptText(public_key, msg):
    msg_hex = text2hex(msg);
    print(msg_hex);
    merge_range = 2;
    loop_num = math.floor(len(msg_hex)/merge_range);
    if len(msg_hex)%merge_range:
        loop_num+=1;

    encrypted_l = [];
    for i in range(loop_num):
        bundle = msg_hex[i*merge_range:i*merge_range+merge_range];

        bundle_str = [];
        for h in bundle:
            str_h = str(h);
            if len(str_h)<3:
                str_h = "0"+str_h;
            bundle_str.append(str_h);
        bundle_str = "".join(bundle_str);
        encrypted = RSA_DeEncrypt(public_key, int(bundle_str));
        encrypted_l.append(encrypted);

    return encrypted_l;

def RSA_decryptText(private_key, encrypted):
    decrypted_l = [];
    for e in encrypted:
        decrypted_l.append(RSA_DeEncrypt(private_key, e));
    print("decrypted_l = ", decrypted_l);
    decrypted = [];
    for m in decrypted_l:
        num2str = str(m);
        decrypted.append(int(num2str[:-3]));
        decrypted.append(int(num2str[-3:]));
        # decrypted.append(num2str);
    decrypted = hex2text(decrypted);
    return decrypted

def getMemberinBasket(startChr, endChr, msg):
    str_list = [];
    s = 0;
    e = 0;
    s_p = 0;
    e_p = 0;
    for c, i in enumerate(msg):
        if i == startChr:
            s = c;
        if i == endChr:
            e = c;
        if e > s and not(s_p == s or e_p == e):
            str_list.append(msg[s+1:e]);
            s_p = s;
            e_p = e;
    return str_list;
