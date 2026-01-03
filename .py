try:
    with  open("sample.txt","r") as file:
     for line in file:
       print(line)

except:
    print("Something went wrong/or file do not exist")