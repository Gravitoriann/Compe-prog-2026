## This is the template for TP1, full problem in the rulebook ##

def solve(message: str):
    """
    Decrypt the message

    Parameters:
        message str: The string to decrypt using column cypher
        
    Returns:
        str: The string of the decoded message
    """
    decrypted = ""
    ## YOUR CODE GOES HERE ##
    ## VOTRE CODE VA ICI ##
    sizes = []
    for i in range(1, (len(message)+1)):
        if len(message)% i ==0:
            sizes.append((i, ((len(message))//i)))
    for i in range(1, (len(message)+2)):
        if (len(message)+1)% i ==0:
            sizes.append((i, ((len(message)+1)//i)))
    print(sizes)
    best = 9999
    best_size = (0, 0)
    for i in sizes:
        if abs(i[0] - i[1]) < best:
            best = abs(i[0] - i[1])
            best_size = i
    print(best_size)

    message = list(message)
    message.append(" ")
    lines = []
    for i in range(best_size[1]):
        temp_line = []
        for n in range(best_size[0]):
            temp_line.append(message[((i*best_size[0])+n)])
        lines.append(temp_line)
    print(lines)
    text = []
    for i in range(len(lines[0])):
        for n in lines:
            text.append(n[i])
    decrypted = "".join(text)
    print(decrypted)








    return decrypted
