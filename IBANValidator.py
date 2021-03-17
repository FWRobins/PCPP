# IBAN Validator
import random

class IBANValidationException(Exception):
    pass

class IBANDict(dict):
    def __setitem__(self, _key, _val):
        if IbanValidate(_key):
            super().__setitem__(_key, _val)

    def update(self, *args, **kwargs):
        for _key, _val in dict(*args, **kwargs).items():
            self.__setitem__(_key, _val)

def IbanValidate(iban):
    iban = iban.replace(' ','')
    if not iban.isalnum():
        raise IBANValidationException("You have entered invalid characters.")
    elif len(iban) < 15:
        raise IBANValidationException("IBAN entered is too short.")
    elif len(iban) > 31:
        raise IBANValidationException("IBAN entered is too long.")
    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)
        if ibann % 97 == 1:
            print("IBAN entered is valid.")
            return True
        else:
            raise IBANValidationException("IBAN entered is invalid.")

my_dict = IBANDict()
keys = ['GB72 HBZU 7006 7212 1253 01', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108']

for key in keys:
    try:
        my_dict[key] = random.randint(0, 1000)
    except IBANValidationException as e:
        for i in e.args:
            print(f"key {key} error: {i}")


print('The my_dict dictionary contains:')
for key, value in my_dict.items():
    print("\t{} -> {}".format(key, value))

try:
    my_dict.update({'dummy_account': 100})
except IBANValidationException:
    print('IBANDict has protected your dictionary against incorrect data insertion')
