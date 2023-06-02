import random as rn
from ordbok import * 

print("Hei, jeg heter Marvin og jeg kan hjelpe deg med enkle spørsmål")
bruker = input("bruker: ")
if "vetle" in bruker:
    svar = rn.choice(vetle)
    print(svar)

if "billån" in bruker:
    svar = rn.choice(billån)
    print(svar)

else:
    svar = rn.choice(no_answer)
    print(svar)
while True:
        bruker=input("Bruker: ")

        if "bye" in bruker:
            break
        else: 
            if "billån" in bruker:
                svar = rn.choice(billån)
                print(svar)

            else:
                svar = rn.choice(no_answer)
            print(svar)