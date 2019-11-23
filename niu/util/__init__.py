def get_niu(data):
    niu = -1
    for k, v in enumerate(data):
        if k < len(data) - 2:
            for i in range(k + 1, len(data) - 1):
                for ii in range(i + 1, len(data)):
                    sum = v + data[i] + data[ii]
                    if not sum % 10:
                        tmp = list(filter(lambda x: False if x in (k, i, ii) else True, list(range(len(data)))))
                        for it in tmp:
                            sum += data[it]
                        niu = sum % 10
                        return niu if niu else 10
    return niu


def format_niu_data(data):
    tmp = list()
    niu = list()
    report = list()
    for i in data:
        time = i[0]
        i = i[1]
        first_zone = get_niu(i[0:5])
        last_zone = get_niu(i[5:10])

        res = 1 if first_zone > last_zone else 0
        tmp.append(res)
        niu.append((first_zone, last_zone))
        report.append((time, res))

    for i in niu:
        print(i)

    return tmp, report


def get_hu(data):
    return list(map(lambda x: 1 if x[0] > x[9] else 0, data))


def format_hu_data(data):
    records = list(map(lambda x: x[1], data))
    time = list(map(lambda x: x[0], data))
    report = list()
    data = get_hu(records)

    # visual data for report
    for k, v in enumerate(data):
        report.append((time[k], v))

    hu = list(map(lambda x: '1    0' if x else '0    1', data))
    for i in hu:
        print(i)

    return data, report


def continue_for_times(times, time_data):
    res = dict()
    # record time duration
    res['duration'] = {
        'start': time_data[-1],
        'end': time_data[0]
    }
    res['record'] = list()

    record = res['record']

    last_turn = None
    now_times = 0
    # [(timestr, record)]
    for k, v in reversed(time_data):
        if last_turn is None:
            last_turn = v
            continue

        if v != last_turn:
            now_times += 1

            if now_times == times:
                last_turn ^= 1
            elif now_times > 2 * times - 1:
                # append to res and reset count, we have find a failure point
                now_times = 0
                last_turn ^= 1
                record.append((k, v))

        else:
            now_times = 0

    return res
