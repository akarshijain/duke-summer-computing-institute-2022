def calculateBalance(age, current_balance, info_tuple):
    months = info_tuple[0]
    while months > 0:
        print('Age {:3d} month {:2d} you have ${:.2f}'.format(age//12, age%12, current_balance))
        age += 1
        increase = current_balance * info_tuple[2]
        current_balance += increase + info_tuple[1]
        months -= 1
    return age, current_balance


def calculateRetirement(start_age, initial, working, retired):
    retirement_start_age, current_balance = calculateBalance(start_age, initial, working)
    calculateBalance(retirement_start_age, current_balance, retired)


def set_info_tuple(months, contribution, rate_of_return):
    info_tuple = (months, contribution, rate_of_return)
    return info_tuple


if __name__ == "__main__":
    working = set_info_tuple(489, 1000, 0.045/12)
    retired = set_info_tuple(384, -4000, 0.01/12)
    calculateRetirement(327, 21345, working, retired)