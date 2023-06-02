import termcolor as tc


def pair(num_list: list[int], num: int = 0) -> list[int]:
    """
    input: [0, 1, 7, 0, 2, 2, 0, 0, 1, 0]
    output:"^--------^        ^--^      "
    output:[0, 1, 7,    2, 2, 0,    1, 0]
    output:"^                 ^        ^"
    """
    num_pos: list[bool] = [n == num for n in num_list]

    pre_output1 = " " + "".join(["^  " if n else "   " for n in num_pos])
    pre_output1 = pre_output1.split("^")
    for i in range(1, len(pre_output1)-1, 2):
        pre_output1[i]=pre_output1[i].replace(" ", "-")

    if len(pre_output1)%2 == 0:
        output1 = "^".join(pre_output1[:-1]) + " " + pre_output1[-1]
    else:
        output1 = "^".join(pre_output1)
    

    yes: bool = True
    pre_output3 = []
    for num_b in num_pos:
        if num_b:
            if yes:
                pre_output3.append(True)
            else:
                pre_output3.append(False)
            yes = not yes
        else:
            pre_output3.append(False)
    
    output2: list[int] = []
    for num_p, num_l in zip(pre_output3, num_list):
        if num_l == num:
            if num_p:
                output2.append(num_l)
        else:
            output2.append(num_l)
    


    i_output2: int = 0
    pp_output2: str = " "
    for num_l in num_list:
        if pp_output2[-1] == " ":
            pp_output2 += "  "
        else:
            pp_output2 += ", "

        if num_l == output2[i_output2]:
            pp_output2 += str(num_l)
            i_output2 += 1
        else:
            pp_output2 += " " * len(str(num_l))

    pp_output2 = "[" + pp_output2[3:] + "]"

    output3 = "".join(["^" if p == str(num) else " " for p in pp_output2])

    print(tc.colored(num_list.__str__(), "magenta"))
    print(tc.colored(output1, "green"))
    print(tc.colored(pp_output2, "magenta"))
    print(tc.colored(output3, "yellow"))

        

    return output2

    




pair([0, 1, 7, 0, 2, 2, 0, 0, 1, 0])
