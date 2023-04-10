# python3

B=13 #prime
Q=256 #alphabet

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    switch = input()
    if "F" in switch:
        # input from file
        filename = input()
        if filename != "a":
            f = open("./tests/"+filename, "r")
            P = f.readline()
            T = f.readline()
            f.close()
    elif "I" in switch:
        # input from keyboard
        P = input()
        T = input()
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (P.rstrip(), T.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern: str, text: str):
    # this function should find the occurances using Rabin Karp alghoritm 
    global B, Q
    p_len = len(pattern)
    t_len = len(text)

    multiplier = 1
    for i in range(1, p_len):
        multiplier = (multiplier * Q) % B

    p_hash = 0
    t_hash = 0
    for i in range(p_len):
        p_hash = (Q * p_hash + ord(pattern[i])) % B
        t_hash = (Q * t_hash + ord(text[i])) % B

    output = []
    for i in range(t_len-p_len+1):
        if p_hash == t_hash:
            for j in range(p_len):
                if text[i+j] != pattern[j]:
                    break
                else:
                    j += 1

            if j == p_len:
                output.append(i)
        
        if i < t_len-p_len:
            t_hash = (Q * (t_hash - ord(text[i]) * multiplier) + ord(text[i+p_len])) % B

            if t_hash < 0:
                t_hash = t_hash + B

    # and return an iterable variable
    return output

#not used!
def get_hash(pattern: str) -> int:
    global B, Q
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (B * result + ord(pattern[i])) % Q
    return result

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

