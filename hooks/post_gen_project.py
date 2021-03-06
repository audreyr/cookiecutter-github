#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import getpass
import json
import os
import sys

import requests


print('post generation hook')
f = open('python_post.txt', 'w')
f.close()

print('Enter the following info to authenticate with GitHub and create a repo.')

# TODO: use cookiecutter['github_username'] instead
sys.stdout.write('GitHub username? ')
user = input()

password = getpass.getpass()

payload = {'name': 'test-repo'}

r = requests.post(
        url='https://api.github.com/user/repos',
        data=json.dumps(payload),
        auth=(user, password)
    )

print(r.status_code)
print(r.content)
