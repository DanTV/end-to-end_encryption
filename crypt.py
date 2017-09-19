from tkinter import filedialog, Tk
class Crypting():
    def crypt(self,task="f"):
        import abc_creator
        if task =='e':
            alphabet = abc_creator.create_abc()
            text = input("Enter text: ")
            print("\n"*100)
            abc_old = 'q w e r t y u i o p a s d f g h j k l z x c v b n m + '.split()

            alphabet_2 = {}
            for v in range(0, 27):
                alphabet_2[abc_old[v]] = alphabet[v]

            output_text=""
            for i in text:
                if i ==" ": i="+"
                letter = alphabet_2[i]
                if letter == "+": letter=" "
                output_text += letter
            print("Your encrypted text:\n"+output_text)
            print("\n\nAlphabet for decrypting is near to this crypting machine")
        elif task == "d":
            main = Tk()
            filed = filedialog.askopenfilename(master=main)
            if str(filed).endswith(".txt"): pass
            else:
                print("File with alphabet must be text file (.txt)")
                input("Press Any Key On Keyboard")
                self.crypt(task)
            print(filed)

            print("Input text for decrypt")
            text_decrypt = input("Input: ")

            file = open(filed, "r")
            alphabet_d = file.read()
            file.close()

            alphabet_d = alphabet_d.split()
            abc_decrypt = {}

            abc_old = 'q w e r t y u i o p a s d f g h j k l z x c v b n m + '.split()
            for c in range(0,27):
                abc_decrypt[alphabet_d[c]]= abc_old[c]
            print(abc_decrypt)

            output_text_decrypt = ""
            for s in text_decrypt:
                letter_decrypt = abc_decrypt[s]
                if letter_decrypt == "+": letter_decrypt = " "
                output_text_decrypt += letter_decrypt
            print("Your decrypted text:\n"+output_text_decrypt)
            input("\nPress Any Key On Keyboard")


        elif task == "f":
            print("You need to input only D(decrypt) or E(encrypt).\n"
                  "But your choice is going to be choiced by our programm:\n"
                  "It's: Ecnrypt")
            input("Press Any Key On Keyboard")
            self.crypt(task="e")



    def main(self):
        print("Hello! This is a crypting machine. You can crypt and encrypt anything you like.\n")
        task = input("Encrypt(e)/Decrypt(d): ")
        if str(task).lower() == "e" or str(task).lower() == "encrypt":
            task = "e"
        elif str(task).lower() == "d" or str(task).lower() == "decrypt":
            task = 'd'
        else: task = 'b'
        self.crypt(task)
Crypting().main()
