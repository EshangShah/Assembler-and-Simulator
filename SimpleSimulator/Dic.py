opc= \
    {
        "00000": "add","00001": "sub","00010": "mov",
        "00011": "mov","00100": "ld","00101": "st",
        "00110": "mul","00111": "div","01000": "rs",
        "01001": "ls","01010": "xor","01011": "or",
        "01100": "and","01101": "not","01110": "cmp",
        "01111": "jmp","10000": "jlt","10001": "jgt",
        "10010": "je","10011": "hlt",
    }
opc_types=\
    {
        "00000": "A","00001": "A","00010": "B","00011": "C",
        "00100": "D","00101": "D","00110": "A","00111": "C",
        "01000": "B","01001": "B","01010": "A","01011": "A",
        "01100": "A","01101": "C","01110": "C","01111": "E",
        "10000": "E","10001": "E","10010": "E","10011": "F",
    }    
Reg_Type=\
    {
        "000": "R0","001": "R1",
        "010": "R2","011": "R3",
        "100": "R4","101": "R5",
        "110": "R6","111": "FLAGS"
    }

Store_resister = \
    {
        "000": "0","001": "0",
        "010": "0","011": "0",
        "100": "0","101": "0",
        "110": "0","111": "0000000000000000"
    }    
t_dic={}    #temp dictionary to store line
def my_input():
    counter = 0   #counts name
    my_input.t_dic = {}   # makes global func.
    while True:
        try:
            name= input()
            if name != "":
                counter += 1
                t_dic [counter-1] = name.split()
        except EOFError:
            break
        except KeyError:
            break
        except IndexError:
            break
