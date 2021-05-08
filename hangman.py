import random
def hanman():
    a=["apple","color","drown","egg","faith","gun","hungry","kite","point","sheep"]
    t=random.choice(a)
    wrd=[]
    for i in range(len(t)):
        wrd.append('_')
    print(wrd)
    print("Guess the word: ", " ".join(wrd) )
    c=0
    for i in range(10):
        x=input()
        np=-1
        if(x in t):
            p=t.index(x)
            if x in wrd:
                try:
                    if(t.index(x,p+1,len(t))>=0):
                        np=t.index(x,p+1,len(t))
                        if np!=-1:
                            wrd[np]=x
                            print("Guess the word: ", " ".join(wrd))
                            print("correct")
                except Exception as e:
                    check_chances(i)
            else:
                wrd[p]=x
                print("Guess the word: ", " ".join(wrd))
                print("correct")
            if('_' in wrd):
                continue
            else:
                print("YUHU, the force is with you!!")
                break
        else:
            if i==0:
                print("\\")
                print("9 chances left")
            if i==1:
                print("\\0")
                print("8 chances left")
            if i==2:
                print("\\0/")
                print("7 chances left")
            if i==3:
                print("\\0/ \n | ")
                print("6 chances left")
            if i==4:
                print("\\0/ \n | \n/")
                print("5 chances left")
            if i==5:
                print("\\0/ \n | \n/ \\")
                print("4 chances left")
            if i==6:
                print("\\0/- \n | \n/ \\")
                print("3 chances left")
            if i==7:
                print("\\0/-| \n | \n/ \\")
                print("2 chances left")
            if i==8:
                print("\\0/_| \n | \n/ \\")
                print("1 chance left")
            if i==9:
                print(" 0_| \n/|\\ \n/ \\")
                print("Dead bro")
                break

def check_chances(i):
    if i==0:
        print("\\")
        print("9 chances left")
    if i==1:
        print("\\0")
        print("8 chances left")
    if i==2:
        print("\\0/")
        print("7 chances left")
    if i==3:
        print("\\0/ \n | ")
        print("6 chances left")
    if i==4:
        print("\\0/ \n | \n/")
        print("5 chances left")
    if i==5:
        print("\\0/ \n | \n/ \\")
        print("4 chances left")
    if i==6:
        print("\\0/- \n | \n/ \\")
        print("3 chances left")
    if i==7:
        print("\\0/-| \n | \n/ \\")
        print("2 chances left")
    if i==8:
        print("\\0/_| \n | \n/ \\")
        print("1 chance left")
    if i==9:
        print(" 0_| \n/|\\ \n/ \\")
        print("Dead bro")

if __name__ == "__main__":
    hanman()
