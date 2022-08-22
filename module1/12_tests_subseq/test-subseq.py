from subseq import maxSeq
import sys


def check(input_list, expected_answer):
    print("Testing maxSeq(" + str(input_list) + ")")
    ans = maxSeq(input_list)
    if (ans == expected_answer):
        print(" -> maxSeq passed this test case")
    else:
        print(" -> maxSeq failed this test case: got " + str(ans) + " but expected " +
              str(expected_answer))
        sys.exit(1)
        pass
    pass


# write your test cases like this
check([1, 2, 3], 3)
check([], 0)
check([1, 2, 2, 3], 2)
check([1, 2, 3, 3, 3, 3, 4, 4, 4], 3)
check([1, 1, 2, 2, 2, 3], 2)
check([1, 3, 5, 7, 7, 8, 9, 10, 11, 12], 6)
check([2, 2, 2, 3, 3, 5], 2)