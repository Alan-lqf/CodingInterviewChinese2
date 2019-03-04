def moving_count(rows, cols, k):
    if rows == 0 or cols == 0:
        return False

    visited = [[False] * cols for _ in range(rows)]
    count = count_recursively(rows, cols, k, (0,0), visited)
    return count


def count_recursively(rows, cols, k, matrix_indices, visited):
    count = 0
    m_i, m_j = matrix_indices

    if check(rows, cols, k, matrix_indices, visited):
        visited[m_i][m_j] = True
        count = 1 + count_recursively(rows, cols, k, (m_i+1, m_j), visited) + count_recursively(rows, cols, k, (m_i-1, m_j), visited) + count_recursively(rows, cols, k, (m_i, m_j+1), visited) + count_recursively(rows, cols, k, (m_i, m_j-1), visited)
    return count


def check(rows, cols, k, matrix_indices, visited):
    m_i, m_j = matrix_indices
    if not (0 <= m_i < rows) or not (0 <= m_j < cols) or (sum_digit(m_i) + sum_digit(m_j) > k) or visited[m_i][m_j]:
        return False
    return True


def sum_digit(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


# ===============测试代码================

def test(rows, cols, k, expected):
    if moving_count(rows, cols, k) == expected:
        print("Passed. \n")
    else:
        print("Faild. \n")

# 多行多列
def test1():
    test(10, 10, 5, 21)

# 一行部分
def test2():
    test(1, 100, 10, 29)


# 一列部分
def test3():
    test(100, 1, 15, 79)


# 不能进入任意一格
def test4():
    test(10, 10, -5, 0)




if __name__ == '__main__':

    test1()
    test2()
    test3()
    test4()
