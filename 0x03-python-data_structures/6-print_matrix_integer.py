#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        m_len = len(matrix[i])
        for j in range(m_len):
            if j != m_len - 1:
                end_c = ' '
            else:
                end_c = ''
                print("{:d}".format(matrix[i][j]), end=end_c)
        print("")
