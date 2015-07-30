#!/usr/bin/env python

import json
import sys
import os
import subprocess


def vulcan_frontend(key, backend):
    j = json.loads(key)
    j['BackendId'] = backend
    return json.dumps(j)


def main():
    stdin = sys.stdin.read()
    j = json.loads(stdin)
    service_name = j['service_name']
    deployment_name = j['deployment_name']

    # Update Vulcan Backend
    output = subprocess.check_output(['/usr/bin/env', 'etcdctl', 'get', '/vulcand/frontends/%s/frontend' % service_name], env=os.environ.copy())
    subprocess.check_call(['/usr/bin/env', 'etcdctl', 'set', '/vulcand/frontends/%s/frontend' % service_name, vulcan_frontend(output, deployment_name)], env=os.environ.copy())


if __name__ == '__main__':
    main()
