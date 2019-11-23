from util import format_hu_data, format_niu_data, continue_for_times


def make_x_turn(data, x=3):
    hu_data = format_hu_data(data)
    niu_data = format_niu_data(data)

    hu = three_turn_hu(hu_data, x)
    niu = three_turn_niu(niu_data, x)

    return hu, niu


def three_turn_hu(data, x):
    res, time_data = data

    return continue_for_times(x, time_data)


def three_turn_niu(data, x):
    res, time_data = data

    return continue_for_times(x, time_data)
