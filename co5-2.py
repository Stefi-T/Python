fr=open("sample.txt","r")
fw=open("s.txt","w")
x=1
for i in fr:
    if x%2!=0:
        fw.write(i)
    x=x+1
fw.close()
fr.close()
print("Odd lines in new file:")
print(" ")
fw1=open("s.txt","r")
for line in fw1.readlines():
    print(line)
fw1.close()

