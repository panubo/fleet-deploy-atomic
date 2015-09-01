#!/usr/bin/env python

import json
import sys
import os
import subprocess
from subprocess import STDOUT

# TODO: look at using https://github.com/jplana/python-etcd


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
    try:
        output = subprocess.check_output(['/usr/bin/env', 'etcdctl', 'get', '/vulcand/frontends/%s/frontend' % service_name], env=os.environ.copy(), stderr=STDOUT)
    except subprocess.CalledProcessError as e:
        if e.returncode == 4:
            # Make backend directory if required
            subprocess.call(['/usr/bin/env', 'etcdctl', 'mkdir', '/vulcand/frontends/%s' % service_name], env=os.environ.copy(), stderr=STDOUT)
            subprocess.call(['/usr/bin/env', 'etcdctl', 'set', '/vulcand/frontends/%s/frontend' % service_name, '{}'], env=os.environ.copy(), stderr=STDOUT)
            output = '{}'
        else:
            raise  # /vulcand/frontends/wordpress-test-master

    subprocess.check_call(['/usr/bin/env', 'etcdctl', 'set', '/vulcand/frontends/%s/frontend' % service_name, vulcan_frontend(output, deployment_name)], env=os.environ.copy(), stderr=STDOUT)

if __name__ == '__main__':
    main()
