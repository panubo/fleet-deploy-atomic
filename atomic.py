#!/usr/bin/env python

import json
import sys
import os
from subprocess import Popen


def main():
    stdin = sys.stdin.read()
    j = json.loads(stdin)
    service_name = j['service_name']
    p = Popen(['/usr/bin/env', 'etcdctl', 'set', '/web/docs/upstream', service_name], env=os.environ.copy())
    p.wait()

if __name__ == '__main__':
    main()
