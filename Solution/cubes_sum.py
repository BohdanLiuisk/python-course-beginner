from math import floor


def get_coubes_sum(number, result_array=None, starting_point=0):
    if result_array is None:
        result_array = []
    number_index = number
    point_index = starting_point
    while number_index > 0:
        if point_index > 0:
            x = floor(float('{0:.11f}'.format((number_index ** (1 / 3))))) - 1
            point_index -= 1
        else:
            x = floor(float('{0:.11f}'.format((number_index ** (1 / 3)))))
        if x <= 1:
            x = floor(float('{0:.11f}'.format((number_index ** (1 / 3)))))
        if point_index > x:
            print(0)
            exit(0)
        result_array.append(x ** 3)
        number_index -= x ** 3
        if len(result_array) > 7:
            result_array.clear()
            get_coubes_sum(number, result_array, starting_point + 1)
    print(*result_array)
    exit(0)

while True:
    get_coubes_sum(int(input()))
