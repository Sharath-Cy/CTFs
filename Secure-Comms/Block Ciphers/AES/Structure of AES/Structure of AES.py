
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    m2b = []
    for i in range(0,4):
        for j in range(0,4):
            m2b.append(matrix[i][j])
    return m2b
        
def flagex(m2b):
    Flag = ""
    for i in m2b:
        Flag+= chr(i)
    return Flag

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

mat2bytes = matrix2bytes(matrix)
print(flagex(mat2bytes))

