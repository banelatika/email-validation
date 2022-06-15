

email = input("enter your email : ")
k = 0
j = 0
d = 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == "."):
                for x in email:
                    if x == x.isspace():
                        k = 1
                    elif x.isalpha():
                        if x == x.upper():
                            j = 1
                    elif x.isdigit():
                        continue
                    elif x == " _" or x == "." or x == "@":
                        continue
                    else:
                        d == 1

                if k == 1 or j == 1 or d == 1 :
                        print("wrong email 5")
                else : 
                    print("right Email")
            else:
                print("wrong Email 4")
        else:
            print("wrong email3")
    else:
        print("wrong email 2")
else:
    print("wrong emali 1")
