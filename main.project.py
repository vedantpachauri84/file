

with open("sample.txt","w") as file:
     content=input("Enter the content")
     file.write(content)
     print("content written sucessfully")


with open("sample.txt","a") as file:
    print("enter data to append in file")
    content2=input("Enter the content")
    print("enter data to append in file")
    file.write(content2)


with open("sample.txt","r") as file:
 print(file.read())

