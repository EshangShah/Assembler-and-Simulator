# This is a sample Python script.
import sys
A={"add":"00000","sub":"00001","mul":"00110","xor":"01010","or":"01011","and":"01100"}
B={"mov":"00010","rs":"01000","ls":"01001",}
C={
    "mov":"00011",
    "div":"00111",
    "cmp":"01110",
    "not":"01101",
}
D={"ld":"00100","st":"00101"}
F={"hlt":"10011"}

E={"jmp":"01111","jlt":"10000","jgt":"10001","je":"10010"}
REG={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
dict_u=1  # for part d
pc=0       # for programm counting9
t=[]
u={}
label1={}
name1=[]
fight=[]
bjp=""
fig=0   # for the e part
# list of instructions in chronological order
while(True):
    if(len(fight)==0):
        name = sys.stdin.readline()
    else:
        name=fight[0]
        fight=[]
    z = name.split()
    if(z[0] not in E and z[0] not in D ):
        name1.append(name)                  # append z for error handling
    if "hlt" in z:

        if (z[0][-1:-2:-1] == ":"):
            label1[z[0][0:-1]] = name

        break
    if (z[0] == "var"):
        u[z[1]]=dict_u
        dict_u+=1
        pc+=1
    #try:
    if(z[0] in A):
        #try:


        if(z[1] in REG and z[2] in REG and z[3] in REG):
            opc = A[z[0]]
            reg1 = REG[z[1]]
            reg2 = REG[z[2]]
            reg3 = REG[z[3]]
            out_A = opc + "00" + reg1 + reg2 + reg3
            t.append(out_A)

        pc+=1
    if (z[0] in C and z[2] in REG):
        if(len(z)==3):

            opc = C[z[0]]
            reg1 = REG[z[1]]
            reg2 = REG[z[2]]
            out_c = opc + "00000" + reg1 + reg2
            t.append(out_c)
        pc+=1

    elif(z[0] in B):

        opc=B[z[0]]
        reg1=REG[z[1]]
        imm=bin(int(z[2][1:]))
        imm=imm[2:]
        while(len(imm)<8):
            imm="0"+imm
        out_B=opc+reg1+imm
        t.append(out_B)
        pc+=1
    elif(z[0] in D):     # mp declaration order to be followed and no count for load and store instructions.
        opc=D[z[0]]
        reg1=REG[z[1]]
        char=z[2]
        t.append(opc+reg1+char)
    elif(z[0] in E):
        opc=E[z[0]]
        st=z[1]                   # st is the mem_add
        t.append(opc+st)


    elif(z[0][-1:-2:-1]==":"):
        label1[z[0][0:-1]]=name

        for k in range(1,len(z)):
            bjp=bjp+z[k]+" "
        fight.append(bjp)
dict_var={}
for Var in u:
    dict_var[Var]=pc+u[Var]        # this is the final dictionary

t.append("1001100000000000")
for j in t:
    if(j[0:5]=="00100" or j[0:5]=="00101"):
        mem_addr=dict_var[j[8:]]                # working for printing d

        BIN=bin(mem_addr)

        yes=str(BIN)
        final=yes[2:]
        while(len(final)<8):
            final="0"+final

        print(j[0:8]+final)
    elif(j[0:5]=="01111" or j[0:5]=="10000" or j[0:5]=="10001" or j[0:5]=="10010"):
        my_label=label1[j[5:]]
        fin=name1.index(my_label)
        Binary=bin(fin)
        yes1=str(Binary)
        final1=yes1[2:]
        while(len(final1)<8):
            final1="0"+final1
        print(j[0:5]+"000"+final1)         # jai shree ram
    else:
        print(j)
