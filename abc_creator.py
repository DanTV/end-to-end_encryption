


def create_abc():
    import random
    new_abc = "q w e r t y u i o p a s d f g h j k l z x c v b n m +".split()
    old_abc = ""

    dict_abc = {}

    used = []
    for c in range(0, 10000):
        if len(old_abc) == len(new_abc):
            break
        letter = random.randrange(0, len(new_abc))
        if letter in used:
            pass
        else:
            old_abc += new_abc[letter]
            used.append(letter)
    old_abc = (" ".join(old_abc)).split()
    for f in range(0, 27):
        dict_abc[new_abc[f]] = old_abc[f]
    dict_abc_write = ""
    for s in dict_abc.values():
        dict_abc_write = dict_abc_write + s + " "
    password = open("alphabet.txt", "w")
    password.write(dict_abc_write)
    password.close()

    print("New crypted alphabet has created. It's in alphabet.txt near the abc creator.\n"
          "Now you should go to crypt machine and crypt your text with this alphabet\n")
    input("Press Any Key On Keyboard")
    return dict_abc_write.split()





if __name__ == '__main__':
    create_abc()