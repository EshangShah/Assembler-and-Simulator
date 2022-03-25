
import Dic
from Dic import t_dic
var={}      #empty dic to store variable
def reader(count):
    name = t_dic[count]
    tp_type1 = name[0][0:5]
    type1 = None
    for i in Dic.opc_types.keys():
        if tp_type1 == i:
            type1 = Dic.opc_types[i]
    return type1, name

def bin_dec(binary):
    return int(binary, 2) #gives value of the input in binary


def convert(a,n):           #n is the required number of bits
    bnr = bin(int(a))
     #eliminate the initial "0b"
    bnr = bnr[2:] 
    # this reverses the array         
    x = bnr[::-1]  
    while len(x) < n:
    #add 0's to
        x = x + '0'
    return x[::-1]
def out(type1,count,name):
    address = ""
    j = 0
    fin=[j,address]
    if type1 == " ":
        return()
    #if type is A
    elif type1 == "A":
        #finding the initial opcodes to identify the function
        tp_opc = name[0][0:5]
        #addition function
        if tp_opc == "00000":  
            i = name[0][10:13]   
            j = Dic.Store_resister[i]
            r2 = int(j)
            i = name[0][13:16] 
            k = Dic.Store_resister[i]
            r3 = int(k)
            i = name[0][7:10]
            #performing the task
            r1 = str(r2 + r3)
            Dic.Store_resister[i] = r1
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        #subtract function   
        elif tp_opc=="00001":
            i = name[0][10:13]   
            j = Dic.Store_resister[i]
            r2 = int(j)
            i = name[0][13:16] 
            k = Dic.Store_resister[i]
            r3 = int(k)
            i = name[0][7:10]
            #performing the task
            r1 = str(r2 - r3)
            Dic.Store_resister[i] = r1
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        #multiply function
        elif tp_opc=="00110":
            i = name[0][10:13]   
            j = Dic.Store_resister[i]
            r2 = int(j)
            i = name[0][13:16] 
            k = Dic.Store_resister[i]
            r3 = int(k)
            i = name[0][7:10]
            #performing the task
            r1 = str(r2 * r3)
            Dic.Store_resister[i] = r1
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        #exclusive or function   
        elif tp_opc== "01010":
            i = name[0][10:13]   
            j = Dic.Store_resister[i]
            r2 = int(j)
            i = name[0][13:16] 
            k = Dic.Store_resister[i]
            r3 = int(k)
            i = name[0][7:10]
            #performing the task
            r1 = r2 ^ r3
            Dic.Store_resister[i] = r1
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        #or function
        elif tp_opc== "01011":
            i = name[0][10:13]   
            j = Dic.Store_resister[i]
            r2 = int(j)
            i = name[0][13:16] 
            k = Dic.Store_resister[i]
            r3 = int(k)
            i = name[0][7:10]
            #performing the task
            r1 = r2 | r3
            Dic.Store_resister[i] = r1
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        #and function
        elif tp_opc=="01100":
            i = name[0][10:13]   
            j = Dic.Store_resister[i]
            r2 = int(j)
            i = name[0][13:16] 
            k = Dic.Store_resister[i]
            r3 = int(k)
            i = name[0][7:10]
            #performing the task
            r1 = r2 & r3
            Dic.Store_resister[i] = r1
            Dic.Store_resister["111"] = "0000000000000000"
            return fin    
    #if type is B
    elif type1=="B":
        tp_opc = name[0][0:5]        
        # MoveImmediate function
        if tp_opc == "00010":  
            i = name[0][5:8]
            Dic.Store_resister[i] = bin_dec(str(name[0][8:]))
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        #right shift function
        elif tp_opc=="01000":
            i = name[0][5:8]
            Dic.Store_resister[i] = int(Dic.Store_resister[i] >> (bin_dec(str(name[0][8:]))))
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        #left shift function
        elif tp_opc=="01001":
            i = name[0][5:8]
            Dic.Store_resister[i] = int(Dic.Store_resister[i] << (bin_dec(str(name[0][8:]))))
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        else:
            return()    
    #if type is C
    elif type1 == "C" :
        tp_opc = name[0][0:5]
        # Move reg function
        if (tp_opc == "00011"):  
            i = name[0][13:16]
            k = Dic.Store_resister[i]
            r3 = int(k)
            i = name[0][10:13]
            Dic.Store_resister[i] = str(r3)
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        #divide function
        elif tp_opc=="00111":
            i = name[0][10:13]   
            l = Dic.Store_resister[i]
            r4 = int(l)
            i = name[0][13:16] 
            k = Dic.Store_resister[i]
            r3 = int(k)
            i = name[0][7:10]
            #performing the task
            r1 = str(r3 // r4)
            r2 = str(r3 % r4)
            Dic.Store_resister["000"] = r1  #stores quotient in R0
            Dic.Store_resister["001"] = r2  #stores quotient in R1
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        #invert function
        elif tp_opc=="01101":
            i = name[0][13:16]
            j = Dic.Store_resister[i]
            r2 = int(j)
            i = name[0][10:13]
            r2= ~r2
            Dic.Store_resister[i] = str(r2)
            Dic.Store_resister["111"] = "0000000000000000"
            return fin        
        #compare function
        elif tp_opc=="01110":
            i = name[0][10:13]   
            j = Dic.Store_resister[i]
            r2 = int(j)
            i = name[0][13:16] 
            k = Dic.Store_resister[i]
            r3 = int(k)
            i = name[0][7:10]
            if (r3 > r2):
                Dic.Store_resister["111"] = "0000000000000010"
                return fin
            elif (r3 < r2):
                Dic.Store_resister["111"] = "0000000000000100"
                return fin
            else:
                Dic.Store_resister["111"] = "0000000000000001"
                return fin 
        else:
            return()           
    #if type is D
    elif (type1 == "D"):
        tp_opc = name[0][0:5]
        # store function 
        if (tp_opc == "00101"):    
            i = name[0][5:8]
            j = Dic.Store_resister[i]
            r2 = int(j)
            var[name[0][8:16]] = j
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        # load function
        elif (tp_opc == "00100"):
            i = name[0][5:8]
            Dic.Store_resister[i] = var[name[0][8:16]]
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        else:
            return() 
    #if type is E        
    elif (type1 == "E"):
        tp_opc = name[0][0:5]
         # unconditional jump function
        if tp_opc == "01111": 
            address = name[0][8:16]
            a = convert(address)
            b = len(var)
            fin[1] = a-b
            fin[0] += 1
            return fin
        # jump if less than function
        elif tp_opc == "10000" and Dic.Store_resister["111"] == "0000000000000100":
            address = name[0][8:16]
            a = convert(address)
            b = len(var)
            fin[1] = a-b
            fin[0] += 1
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        # jump if greater than function
        elif tp_opc == "10001" and Dic.Store_resister["111"] == "0000000000000010":  
            address = name[0][8:16]
            a = convert(address)
            b = len(var)
            fin[1] = a-b
            fin[0] += 1
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
        # jump if equal function
        elif tp_opc == "10010" and Dic.Store_resister["111"] == "0000000000000001":
            address = name[0][8:16]
            a = convert(address)
            b = len(var)
            fin[1] = a-b
            fin[0] += 1
            Dic.Store_resister["111"] = "0000000000000000"
            return fin        
        #else flag remains unchanged 
        else :
            Dic.Store_resister["111"] = "0000000000000000"
            return fin
    #if type is F        
    elif (type1 == "F"):
        main.hlt = True
        Dic.Store_resister["111"] = "0000000000000000"
        return fin
    else:
        return()

def overflow():
    for i,j in Dic.Store_resister.items():
        if i !="111":
            if int(j)>65535 or int(j)<0 :
                x = convert(j,16)
                a = len(x)-16
                j = x[a:len(x)] 
                Dic.Store_resister["111"]="0000000000001000"  
            else:
                return()
  
#prints PC count in bits
def pc_counter(count):      
    print(convert(count, 8),convert(Dic.Store_resister["000"], 16), convert(Dic.Store_resister["001"], 16),
        convert(Dic.Store_resister["010"], 16), convert(Dic.Store_resister["011"], 16),
        convert(Dic.Store_resister["100"], 16), convert(Dic.Store_resister["101"], 16),
        convert(Dic.Store_resister["110"], 16), convert(Dic.Store_resister["111"], 16))
#stacking code lines
def memory(pc):
    a = pc
    pc = 0
    main.hlt = False
    while a > pc:
        type , name = reader(pc)
        z = mem_logic(pc, name)
        if z[0] != 0:
            pc = z[0]
        else:
            pc = pc + 1

    # saving variables at end
    if len(var)>0:
        for i , j in var.items():
            print(convert(j, 16))

    # Saving left over lines
    lines_of_code_left = 256-a-len(var)
    for i in range(0, lines_of_code_left):
        print("0000000000000000")

def mem_logic(count , name):
    j = 0
    address = " "
    fin = [j, address]
    #if there is any hlt 
    if name == "1001100000000000":
        main.hlt = True
    print(name[0])
    return fin      

from Dic import my_input
import matplotlib.pyplot as plt
#as given in the pseudo code
def main():
    my_input()
    pc = 0
    Cycle = 0
    x=[]
    y=[]
    main.hlt = False
    while (not main.hlt):
        types , name = reader(pc)
        f = out(types, pc, name)
        x.append(Cycle)
        y.append(pc)
        overflow()
        pc_counter(pc) #update 
        if f[0] != 0:
        #increment the PC
            pc = f[1]

        #else 
        else:
            pc = pc + 1
            Cycle = Cycle+ 1
    memory(pc)
    plt.plot(x,y,marker="D",linestyle="solid",color="m")
    plt.title = ("Memory Access Trace")
    plt.xlabel("Cycle Number")
    plt.ylabel("Memory Address")
    plt.show
    plt.savefig("matplotlib.png") 
if __name__ == "__main__":
    main()
