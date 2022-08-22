def find_moving_average(data, n):
    moving_average_list = []
    for i in range(len(data) - n+1):
        moving_sum = 0
        moving_average = 0
        for j in range(i, i+n):
            moving_sum += data[j]
        moving_average = moving_sum/n
        moving_average_list.append(moving_average)
    return moving_average_list


def is_peak_at(data, index, w):
    if (index >= w and index < len(data) - w):
        for i in range(1, w+1):
            if (data[index] > data[index-i] and data[index] >= data[index+i]):
                continue
            else:
                return False
        return True
    return False


def get_only_peaks(data, w):
    peaks_list = []
    for i in range(len(data)):
        if is_peak_at(data, i, w):
            peaks_list.append(data[i])
    return peaks_list

def moving_average_of_peaks(data, n, w):
    moving_average_peaks_list = []
    peaks_list = get_only_peaks(data, w)
    moving_average_peaks_list = (find_moving_average(peaks_list, n))
    return moving_average_peaks_list


# some functions to help with testing
def report_test(ans, expected):
    if ans == expected:
        print(" - correct:" + str(ans))
    else:
        print(" **INCORRECT** got " + str(ans) + " but expected " +
              str(expected))
        pass
    pass


def check_ma(data, n, expected):
    print("find_moving_average(" + str(data) + ", " + str(n) + ")")
    report_test(find_moving_average(data, n), expected)
    pass

def check_peaks(data, w, expected):
    print("get_only_peaks(" + str(data) + ", " + str(w) + ")")
    report_test(get_only_peaks(data, w), expected)
    pass


def check_ma_of_peaks(data, n, w, expected):
    print("moving_average_of_peaks(" + str(data) + ", " + str(n) + "," +
          str(w) + ")")
    report_test(moving_average_of_peaks(data, n, w), expected)
    pass


if __name__ == "__main__":
    # test with our basic example data
    data0 = [160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162]
    check_ma(data0, 4, [161, 161, 161, 161, 161.5, 162.5, 163, 163])
    check_peaks(data0, 2, [162, 164])
    check_ma_of_peaks(data0, 2, 2, [163])
    # trying to take the 3 element moving average of a 2 element list
    # gives the empty list
    check_ma_of_peaks(data0, 3, 2, [])
    # the one element moving average is just the data
    check_ma(data0, 1, data0)
    # test with the empty list
    data1 = []
    check_ma(data1, 1, [])
    check_peaks(data1, 1, [])
    check_ma_of_peaks(data1, 1, 1, [])
    # another list to test with
    data2 = [
        100, 105, 110, 115, 120, 115, 110, 120, 125, 120, 125, 120, 130, 135,
        140, 135, 130
    ]
    check_ma(data2, 5,
             [110, 113, 114, 116, 118, 118, 120, 122, 124, 126, 130, 132, 134])
    check_ma(data2, 10, [114, 116.5, 118, 120, 122, 124, 126, 128])
    check_peaks(data2, 1, [120, 125, 125, 140])
    check_peaks(data2, 2, [120, 125, 140])
    check_peaks(data2, 8, [])
    check_ma_of_peaks(data2, 2, 1, [122.5, 125, 132.5])
    check_ma_of_peaks(data2, 2, 2, [122.5, 132.5])
    pass
