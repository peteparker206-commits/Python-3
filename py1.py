try:
    with open("sample.txt", "rt") as file: 
       for i,line in enumerate(file, start=1): 
            print(f"line{i} = {line.strip()}") 

except FileNotFoundError:
    print("The file doesnot exists!")
