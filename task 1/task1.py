def q1(input_file_name):
    """
    Read values from input file
    :param input_file_name: An input file name
    :return: The result of the division of the first number by the others
    """
    try:
        with open(input_file_name, 'r') as file:
            f = file.readlines()
    except:
        return -1
    try:
        index = 0
        current_val = 0
        for line in range(len(f)):
            #going through line by line
            for i in range(len(f[line].split())):
                # going through word by word
                if index == 0:
                    #first number in the file
                    current_val = float(f[line].split()[i])
                else:
                    current_val = float(current_val) / float(f[line].split()[i])
                index += 1
        return current_val

    except ZeroDivisionError:
        return -2
    except ValueError:
        return -3

 

def q2(input_file_name):
    """
      a. Read words from input file
      b. Classify the words by length
      c. Write each word and its length to output file.
    """
    try:
        with open(input_file_name, 'r') as file:
            f = file.readlines()
    except:
        print ("problem with the file")
    word_list = []
    max_word = 0
    sorted_list = []
    for line in range(len(f)):
        # going through line by line
        for i in range(len(f[line].split())):
            # going through word by word
            word_list.append(f[line].split()[i])

    while len(word_list) != 0:
        for words in range(len(word_list)):
            #searching fot the biggest word in the file
            if len(word_list[words]) >= max_word:
                max_word = len(word_list[words])
        changed_list = word_list[::-1]
        #taking revrsed list
        for elements in range(len(word_list)):
            #put the longest word in a new list
            if len(changed_list[elements]) == max_word:
                max_word = 0
                sorted_list.append((changed_list[elements], len(changed_list[elements])))
                word_list.remove(changed_list[elements])
                break
    sorted_list = sorted_list[::-1]
    #taking a reversed list because we want shorter words first
    with open('output_' + str(input_file_name), 'w') as l:
        l.write(str(sorted_list))
    
    

def isPrime(N):
    #check if a given number is a prime number
    for number in range(2, N):
        if N % number == 0:
            return False
    return True
    
def q3_a(n: int):
    """
    :param n: An integer number
    :return: All prime numbers up to n
    """
    if n < 2:
        return []
    factors = []
    for i in range(2 , n+1):
        #check numbers till n and add the prime one's into a list
        if isPrime(i):
            factors.append(i)
    return factors
    

def q3_b(n: int):
    """
    uses the function q3_a
    :param n: An integer number
    :return: A list that contains all the three prime numbers combinations whose product is less than or equal to n.
    """
    all_factorials = q3_a(n)
    #a list of prime numbers till n
    main_factors = []
    for i in range(len(all_factorials)):
        #first number
        for j in range(len(all_factorials)):
            #second number
            for r in range(len(all_factorials)):
                #third number
                if all_factorials[i] * all_factorials[j] * all_factorials[r] <= n and all_factorials[i] <= all_factorials[j] <= all_factorials[r]:
                    main_factors.append([all_factorials[i] , all_factorials[j] , all_factorials[r]])
                    #if the three numbers are by the rules, add them to a list
    return main_factors
    

def q4(n: int):
    """
    :param n: A positive number
    :return: The n-th line in the Pascal triangle
    """
    try:
        pascal_line = []
        for i in range(n+1):
            #creates a list of lists line by line
            pascal_line.append([])
            pascal_line[i].append(1)
            for j in range(1, i):
                #every number in pascal triangle is the sum of the two numbers from the upper line
                pascal_line[i].append(pascal_line[i - 1][j - 1] + pascal_line[i - 1][j])
            if i != 0:
                pascal_line[i].append(1)
        return pascal_line[n]
    except:
        return -1


    
def q5_a(z, a, b, n):
    """
     The function returns the approximation of the root of 𝑧(𝑥) (𝑧(𝑥)=0) according to the bisection method.
    """
    iterations = 0
    if a > b:
        return False
    if z(a)*z(b) > 0:
        #no solution
        return False
    while (b-a) >= 0.01:
        x_current = (a+b)/2
        if z(a)*z(b) > 0:
            return False
        if z(x_current) == 0:
            # this is a root
            return round(x_current, 2)
        if z(x_current) * z(a) < 0:
            #go to the right side
            b = x_current
        else:
            #go to the left side
            a = x_current
        if iterations == n+1:
            return False
        iterations += 1
    return round(x_current, 2)

def h(x, f, g):
    return f(x)-g(x)


def q5_b(f, g, a, b, n):
    """
    The function returns the approximation of a solution 𝑓(𝑥)=𝑔(𝑥) (using the bisection method)
    """
    #same function like g5_a, but z(x)=f(x)-g(x)
    iterations = 0
    if a > b:
        return False
    if (f(a) - g(a)) * (f(b) - g(b)) > 0:
        return False
    while (b - a) >= 0.01:
        x_current = (a + b) / 2
        if (f(a) - g(a)) * (f(b) - g(b)) > 0:
            return False
        if (f(x_current)-g(x_current)) == 0:
            # this is a root
            return round(x_current, 2)
        if (f(x_current)-g(x_current)) * (f(a) - g(a)) < 0:
            b = x_current
        else:
            a = x_current
        if iterations == n + 1:
            return False
        iterations += 1
    return round(x_current, 2)

# ########### TESTING FUNCTIONS, DO NOT CHANGE THESE FUNCTIONS ################


def f(x):
    return 3*x+9


def g(x):
    return x**2-5

# ###############################################################################


