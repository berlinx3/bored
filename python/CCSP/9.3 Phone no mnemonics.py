from itertools import product


phone_mapping = { "1": ("1",),
                  "2": ("a","b","c"),
                  "3": ("d","e","f"),
                  "4": ("g","h","i"),
                  "5": ("j","k","l"),
                  "6": ("m","n","o"),
                  "7": ("p","q","r","s"),
                  "8": ("t","u","v"),
                  "9": ("w","x","y","z"),
                  "0": ("0",)}


def possible_mnemonics(phone_number):
    letter_tuples = []

    for digit in phone_number:
        letter_tuples.append(phone_mapping.get(digit, (digit,)))
    
    return product(*letter_tuples)  


if __name__ == "__main__":
    # phone_number = input("Enter a phone number")
    print("Here are the potential mnemonics")

    for mnemonics in possible_mnemonics("234"):
        print("".join(mnemonics))