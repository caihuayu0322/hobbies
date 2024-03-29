from util import format_niu_data


def get_max_same_num(data):
    tmp_last_data = 0
    old_max = 1
    new_max = 1
    distri = dict()

    for k, v in enumerate(data):
        if k == 0:
            tmp_last_data = v
            continue

        if v != 0 and v == tmp_last_data:
            new_max += 1
        else:
            old_max = max(new_max, old_max)
            if new_max != 1:
                distri[new_max] = distri.get(new_max, 0) + 1
            new_max = 1

        tmp_last_data = v
    else:
        old_max = max(new_max, old_max)
        if new_max > 1:
            distri[new_max] = distri.get(new_max, 0) + 1

    total = 0
    for (k, v) in distri.items():
        total += v

    res = dict()
    for k in sorted(distri.keys(), key=lambda x: int(x)):
        res[k] = (distri[k], '{:.2f}%'.format(100 * distri[k] / total))
    return old_max, res


def get_max_not_same_num(data):
    tmp_last_data = 0
    old_max = 1
    new_max = 1
    distri = dict()

    for k, v in enumerate(data):
        if k == 0:
            tmp_last_data = v
            continue

        if v != tmp_last_data:
            new_max += 1
        else:
            old_max = max(new_max, old_max)
            if new_max != 1:
                distri[new_max] = distri.get(new_max, 0) + 1
            new_max = 1

        tmp_last_data = v
    else:
        old_max = max(old_max, new_max)
        if new_max > 1:
            distri[new_max] = distri.get(new_max, 0) + 1

    total = 0
    for (k, v) in distri.items():
        total += v

    res = dict()
    for k in sorted(distri.keys(), key=lambda x: int(x)):
        res[k] = (distri[k], '{:.2f}%'.format(100 * distri[k] / total))

    return old_max, res


def make_niu_report(data):
    data, report = format_niu_data(data)

    total = len(data)
    first_zone = 0
    for i in data:
        first_zone += i

    first = data
    last = list(map(lambda x: 0 if x else 1, data))

    max_first_zone_same, max_first_zone_same_dist = get_max_same_num(first)
    max_last_zone_same, max_last_zone_same_dist = get_max_same_num(last)
    max_first_zone_not_same, max_first_zone_not_same_dist = get_max_not_same_num(first)
    max_last_zone_not_same, max_last_zone_not_same_dist = get_max_not_same_num(last)

    return {
        'total': total,
        'first_zone': first_zone,
        'last_zone': total - first_zone,
        'max_first_zone_same': max_first_zone_same,
        'max_last_zone_same': max_last_zone_same,
        'max_first_zone_not_same': max_first_zone_not_same,
        'max_last_zone_not_same': max_last_zone_not_same,
        'max_first_zone_same_dist': max_first_zone_same_dist,
        'max_last_zone_same_dist': max_last_zone_same_dist,
        'max_first_zone_not_same_dist': max_first_zone_not_same_dist,
        'max_last_zone_not_same_dist': max_last_zone_not_same_dist,
        'report': report
    }
