from crackhead import Methametic as meth
import math

public_key, private_key = meth.RSA_createKey(51);

msg = "Hello world!";
print(msg);
encrypted = meth.RSA_encryptText(public_key, msg);
# send encrypted_text to your friend

print(encrypted);# man in the middle receive encrypted_text

# friend receive encrypted_text
msg_text = meth.RSA_decryptText(private_key, encrypted);
print(msg_text);
