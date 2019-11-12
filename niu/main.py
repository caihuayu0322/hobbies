import json
import os
import time

from niu.crawler.api import get_data
from niu.report.hu_report import make_hu_report
from niu.report.niu_report import make_niu_report


def writ_to_file(data):
    report = make_niu_report(data)
    report1 = make_hu_report(data)
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
    writ_to_file(get_data(240))
