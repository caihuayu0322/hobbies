import json
import os
import time

import sys

from crawler.api import get_data
from report.hu_report import make_hu_report
from report.niu_report import make_niu_report
from report.three_times_turn import make_x_turn


def writ_to_file(data):
    report = make_niu_report(data)
    report1 = make_hu_report(data)
    hu, niu = make_x_turn(data, 3)

    with open("/tmp/caicai/private/res_%s" % time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time())),
              'w+') as f:
        f.write('niu')
        f.write('\n')
        f.write('total: %s' % report['total'])
        f.write('\n')
        f.write('first zone: %s' % report['first_zone'])
        f.write('\n')
        f.write('last_zone: %s' % report['last_zone'])
        f.write('\n')
        f.write('max_first_zone_same: %s' % report['max_first_zone_same'])
        f.write('\n')
        f.write('max_last_zone_same: %s' % report['max_last_zone_same'])
        f.write('\n')
        f.write('max_first_zone_not_same: %s' % report['max_first_zone_not_same'])
        f.write('\n')
        f.write('max_last_zone_not_same: %s' % report['max_last_zone_not_same'])
        f.write('\n')
        f.write('max_first_zone_same_dist: %s' % json.dumps(report['max_first_zone_same_dist']))
        f.write('\n')
        f.write('max_last_zone_same_dist: %s' % json.dumps(report['max_last_zone_same_dist']))
        f.write('\n')
        f.write('max_first_zone_not_same_dist: %s' % json.dumps(report['max_first_zone_not_same_dist']))
        f.write('\n')
        f.write('max_last_zone_not_same_dist: %s' % json.dumps(report['max_last_zone_not_same_dist']))
        f.write('\n')

        f.write('-----------------------------------------')
        f.write('\n')

        f.write('hu')
        f.write('\n')
        f.write('total: %s' % report1['total'])
        f.write('\n')
        f.write('first zone: %s' % report1['first_zone'])
        f.write('\n')
        f.write('last_zone: %s' % report1['last_zone'])
        f.write('\n')
        f.write('max_first_zone_same: %s' % report1['max_first_zone_same'])
        f.write('\n')
        f.write('max_last_zone_same: %s' % report1['max_last_zone_same'])
        f.write('\n')
        f.write('max_first_zone_not_same: %s' % report1['max_first_zone_not_same'])
        f.write('\n')
        f.write('max_last_zone_not_same: %s' % report1['max_last_zone_not_same'])
        f.write('\n')
        f.write('max_first_zone_same_dist: %s' % json.dumps(report1['max_first_zone_same_dist']))
        f.write('\n')
        f.write('max_last_zone_same_dist: %s' % json.dumps(report1['max_last_zone_same_dist']))
        f.write('\n')
        f.write('max_first_zone_not_same_dist: %s' % json.dumps(report1['max_first_zone_not_same_dist']))
        f.write('\n')
        f.write('max_last_zone_not_same_dist: %s' % json.dumps(report1['max_last_zone_not_same_dist']))
        f.write('\n')

    niu_path = '/tmp/caicai/private/niu/data/niu_data'
    if not os.path.exists(niu_path):
        os.makedirs('/'.join(niu_path.split('/')[:-1]), exist_ok=True)

    hu_path = '/tmp/caicai/private/niu/data/hu_data'
    if not os.path.exists(hu_path):
        os.makedirs('/'.join(hu_path.split('/')[:-1]), exist_ok=True)

    with open(niu_path, 'w+') as f:
        f.write(json.dumps(report['report']))

    with open(hu_path, 'w+') as f:
        f.write(json.dumps(report1['report']))


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(__file__))

    # with open('/tmp/caicai.log', 'w+') as fp:
    #     fp.write(json.dumps(get_data(28800)))
    writ_to_file(get_data(num=480))
