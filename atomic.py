#!/usr/bin/env python

import json
import sys
import os
from subprocess import Popen


def main():
    stdin = sys.stdin.read()
    j = json.loads(stdin)
    service_name = j['service_name']
    deployment_name = j['deployment_name']

    # eg
    # web/vc-master/upstream = vc-master-123adb
    p = Popen(['/usr/bin/env', 'etcdctl', 'set', '/web/%s/upstream' % service_name, deployment_name], env=os.environ.copy())
    p.wait()

if __name__ == '__main__':
    main()