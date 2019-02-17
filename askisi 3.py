ask3 = open('ask3.txt','r')

lines = ask3.readlines()
program =[]
for line in lines:
    grammi = []
    for letter in line:
        if letter!="#":
            grammi.append(letter)
        else :
            break
    program.append(grammi)
ask3.close()
ask3 = open('ask3.txt','w')
for i in range(len(program)):
    ask3.write (str((program[i])))
ask3.close()