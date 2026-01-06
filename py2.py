with open("sample.txt", "at") as f:
    
    add1= input("Enter text to write in the file: \n")
    f.write(add1)

    add2= input("Enter additional information to write in the file: \n")
    f.write(add2)

with open("sample.txt", "rt") as fh:
    
    a = fh.read()
    print(a)
