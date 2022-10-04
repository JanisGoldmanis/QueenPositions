def convert_to_xy(list):
    result = []
    for value in list:
        column = ord(value[0])-65
        row = int(value[1])-1
        result.append([column,row])
    return result
