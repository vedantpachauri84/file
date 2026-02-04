w is used for opening a file in write mode
a is used for open a file and add content in it
r is used for reading a file 
2.
try:
    with  open("sample.txt","r") as file:
     for line in file:
       print(line)

except:
    print("Something went wrong/or file do not exist")
    we use try except block for error handling 
first we open  a file in read mode using "r" print its content line by line
and if file does not exist it do not show error it shows what we decide.
