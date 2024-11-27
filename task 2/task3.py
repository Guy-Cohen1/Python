def question1(num):
    """
    Qs1
    """
    if num == 0:
        return False
    if num == 1:
        return False
    if num == divisors(num, num//2):
        return True
    return False

def divisors(num, counter):
    '''
    :param num:
    :param counter:
    :return: sum of divisors
    '''
    if counter == 1:
        return 1
    if (num % counter) == 0:
        return divisors(num, counter-1) + counter
    return divisors(num, counter-1)
    
def subset(lst, x, sum):
    """
    :param lst: list of integers
    :param x: sum
    :param sum: 0
    :return: number of subsets of lst such that their sum is x
    """
    
    if len(lst) == 0:
        return 0
    if (sum + lst[0]) == x:
        return 1 + subset(lst[1:], x, sum) + subset(lst[1:], x, sum + lst[0])
    return subset(lst[1:], x, sum) + subset(lst[1:], x, sum + lst[0])
    
    
    
def question2(lst, x):
    """
    Qs2
    """
    if x == 0:
        return subset(lst, x, 0) + 1
    return subset(lst, x, 0) 

def epidemic_help(mat, indices, epidemic, cur_row, cur_col):
    """
    :param mat: 
    :param indices: 
    :param epidemic: 
    :param cur_row: 
    :param cur_col: 
    :return: changing the matrix according the epidemic
    """
    if mat[cur_row][cur_col] == 0:
        mat[cur_row][cur_col] = epidemic
        #infected
    else:
        return 1

    # go over all the options
    if cur_row > 0 and cur_col > 0 and cur_row < (len(mat) - 1) and cur_col < (len(mat[0]) - 1):
        return epidemic_help(mat, indices, epidemic, cur_row - 1, cur_col) + epidemic_help(mat, indices, epidemic, cur_row, cur_col - 1) + epidemic_help(mat, indices, epidemic, cur_row + 1, cur_col) + epidemic_help(mat, indices, epidemic, cur_row, cur_col + 1)

    if cur_row > 0 and cur_col > 0 and cur_row < (len(mat) - 1):
        return epidemic_help(mat, indices, epidemic, cur_row - 1, cur_col) + epidemic_help(mat, indices, epidemic, cur_row, cur_col - 1) + epidemic_help(mat, indices, epidemic, cur_row + 1, cur_col)

    if cur_row < (len(mat) - 1) and cur_col < (len(mat[0]) - 1) and cur_row > 0:
            return epidemic_help(mat, indices, epidemic, cur_row + 1, cur_col) + epidemic_help(mat, indices, epidemic, cur_row, cur_col + 1) + epidemic_help(mat, indices, epidemic, cur_row - 1, cur_col)

    if cur_row < (len(mat) - 1) and cur_col < (len(mat[0]) - 1) and cur_col > 0:
            return epidemic_help(mat, indices, epidemic, cur_row + 1, cur_col) + epidemic_help(mat, indices, epidemic, cur_row, cur_col + 1) + epidemic_help(mat, indices, epidemic, cur_row, cur_col - 1)

    if cur_row > 0 and cur_col > 0 and cur_col < (len(mat[0]) - 1):
        return epidemic_help(mat, indices, epidemic, cur_row - 1, cur_col) + epidemic_help(mat, indices, epidemic, cur_row, cur_col - 1) + epidemic_help(mat, indices, epidemic, cur_row, cur_col + 1)

    if cur_row > 0 and cur_col > 0:
        return epidemic_help(mat, indices, epidemic, cur_row - 1, cur_col) + epidemic_help(mat, indices, epidemic, cur_row, cur_col - 1)

    if cur_row > 0 and cur_col < (len(mat[0]) - 1):
        return epidemic_help(mat, indices, epidemic, cur_row - 1, cur_col) + epidemic_help(mat, indices, epidemic, cur_row, cur_col + 1)

    if cur_row > 0 and cur_row < (len(mat) - 1):
        return epidemic_help(mat, indices, epidemic, cur_row - 1, cur_col) + epidemic_help(mat, indices, epidemic, cur_row + 1, cur_col)

    if cur_col > 0 and cur_col < (len(mat[0]) - 1):
        return epidemic_help(mat, indices, epidemic, cur_row, cur_col - 1) + epidemic_help(mat, indices, epidemic, cur_row, cur_col + 1)

    if cur_col > 0 and cur_row < (len(mat) - 1):
        return epidemic_help(mat, indices, epidemic, cur_row, cur_col - 1) + epidemic_help(mat, indices, epidemic, cur_row + 1, cur_col)

    if cur_row < (len(mat) - 1) and cur_col < (len(mat[0]) - 1):
        return epidemic_help(mat, indices, epidemic, cur_row + 1, cur_col) + epidemic_help(mat, indices, epidemic, cur_row, cur_col + 1)

    if cur_col > 0:
        return epidemic_help(mat, indices, epidemic, cur_row, cur_col - 1)

    if cur_row > 0:
        return epidemic_help(mat, indices, epidemic, cur_row - 1, cur_col)

    if cur_col < (len(mat[0]) - 1):
        return epidemic_help(mat, indices, epidemic, cur_row, cur_col + 1)

    if cur_row < (len(mat) - 1):
        return epidemic_help(mat, indices, epidemic, cur_row + 1, cur_col)

def question3_a(mat, indices, epidemic):
    """
    Qs3a
    """
    if mat[indices[0]][indices[1]] != 0:
        mat[indices[0]][indices[1]] = epidemic
    else:
        epidemic_help(mat, indices, epidemic, indices[0], indices[1])

def current_healthy_community(mat,epidemic, cur_row, cur_col):
    """
    :param mat:
    :param cur_row:
    :param cur_col:
    :return: the size of the healthy community in a specific place
    """
    if mat[cur_row][cur_col] == 0:
        mat[cur_row][cur_col] = epidemic
        #infected
        # go over all the options
        if cur_row > 0 and cur_col > 0 and cur_row < (len(mat) - 1) and cur_col < (len(mat[0]) - 1):
            return 1 + current_healthy_community(mat, epidemic, cur_row - 1, cur_col) + current_healthy_community(mat, epidemic,
                                                                                               cur_row,
                                                                                               cur_col - 1) + current_healthy_community(
                mat, epidemic, cur_row + 1, cur_col) + current_healthy_community(mat, epidemic, cur_row,
                                                                              cur_col + 1)

        if cur_row > 0 and cur_col > 0 and cur_row < (len(mat) - 1):
            return 1 + current_healthy_community(mat, epidemic, cur_row - 1, cur_col) + current_healthy_community(mat, epidemic,
                                                                                               cur_row,
                                                                                               cur_col - 1) + current_healthy_community(
                mat, epidemic, cur_row + 1, cur_col)

        if cur_row < (len(mat) - 1) and cur_col < (len(mat[0]) - 1) and cur_row > 0:
            return 1 + current_healthy_community(mat, epidemic, cur_row + 1, cur_col) + current_healthy_community(mat, epidemic,
                                                                                               cur_row,
                                                                                               cur_col + 1) + current_healthy_community(
                mat, epidemic, cur_row - 1, cur_col)

        if cur_row < (len(mat) - 1) and cur_col < (len(mat[0]) - 1) and cur_col > 0:
            return 1 + current_healthy_community(mat, epidemic, cur_row + 1, cur_col) + current_healthy_community(mat, epidemic,
                                                                                               cur_row,
                                                                                               cur_col + 1) + current_healthy_community(
                mat, epidemic, cur_row, cur_col - 1)

        if cur_row > 0 and cur_col > 0 and cur_col < (len(mat[0]) - 1):
            return 1 + current_healthy_community(mat, epidemic, cur_row - 1, cur_col) + current_healthy_community(mat, epidemic,
                                                                                               cur_row,
                                                                                               cur_col - 1) + current_healthy_community(
                mat, epidemic, cur_row, cur_col + 1)

        if cur_row > 0 and cur_col > 0:
            return 1 + current_healthy_community(mat, epidemic, cur_row - 1, cur_col) + current_healthy_community(mat, epidemic,
                                                                                               cur_row, cur_col - 1)

        if cur_row > 0 and cur_col < (len(mat[0]) - 1):
            return 1 + current_healthy_community(mat, epidemic, cur_row - 1, cur_col) + current_healthy_community(mat, epidemic,
                                                                                               cur_row, cur_col + 1)

        if cur_row > 0 and cur_row < (len(mat) - 1):
            return 1 + current_healthy_community(mat, epidemic, cur_row - 1, cur_col) + current_healthy_community(mat, epidemic,
                                                                                               cur_row + 1, cur_col)

        if cur_col > 0 and cur_col < (len(mat[0]) - 1):
            return 1 + current_healthy_community(mat, epidemic, cur_row, cur_col - 1) + current_healthy_community(mat, epidemic,
                                                                                               cur_row, cur_col + 1)

        if cur_col > 0 and cur_row < (len(mat) - 1):
            return 1 + current_healthy_community(mat, epidemic, cur_row, cur_col - 1) + current_healthy_community(mat, epidemic,
                                                                                               cur_row + 1, cur_col)

        if cur_row < (len(mat) - 1) and cur_col < (len(mat[0]) - 1):
            return 1 + current_healthy_community(mat, epidemic, cur_row + 1, cur_col) + current_healthy_community(mat, epidemic,
                                                                                               cur_row, cur_col + 1)

        if cur_col > 0:
            return 1 + current_healthy_community(mat, epidemic, cur_row, cur_col - 1)

        if cur_row > 0:
            return 1 + current_healthy_community(mat, epidemic, cur_row - 1, cur_col)

        if cur_col < (len(mat[0]) - 1):
            return 1 + current_healthy_community(mat, epidemic, cur_row, cur_col + 1)

        if cur_row < (len(mat) - 1):
            return 1 + current_healthy_community(mat, epidemic, cur_row + 1, cur_col)
    else:
        return 0


def traverseMatrix(mat, current_row, current_col, list):
    """
    :param mat:
    :param current_row:
    :param current_col:
    :param list:
    :return: go cell over cell in a recursive way and adding to a list all the sizes off the healthy communities
    """
    M = len(mat)
    N = len(mat[0])
    # If the entire column is traversed
    if (current_col > M):
        return 0

    # If the entire row is traversed
    if (current_row > N):
        return 1

    # cell of the matrix
    if current_col < N and current_row < M:
        list.append(current_healthy_community(mat, 1, current_row, current_col))

    # Recursive call to traverse the matrix
    # in the Horizontal direction
    if (traverseMatrix(mat, current_row, current_col + 1, list) == 1):
        return 1

    # Recursive call for changing the
    # Row of the matrix
    return traverseMatrix(mat, current_row + 1, 0, list)



def question3_b(mat):
    """
    Qs3b
    """
    new_list = []
    traverseMatrix(mat, 0, 0, new_list)
    return max(new_list)


