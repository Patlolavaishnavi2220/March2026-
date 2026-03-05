print("enter the name of first file:",end=" ")
fileOne=input()
print("enter the name of second file:",end=" ")
fileTwo=input()
print("enter the name of third file:",end=" ")
fileThree=input()

content=" "
fh=open(fileOne,"r")
for line in fh:
    content =content+line+'\n'
fh.close()
fh=open(fileTwo,"r")
for line in fh:
    content=content+line+'\n'
fh.close()
fh=open(fileThree,"w")
fh.write(content)
print("\n file merged successfully")
