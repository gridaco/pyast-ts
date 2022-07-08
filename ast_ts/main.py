from base64 import decode
import json
import os
import subprocess
from subprocess import Popen

_DIR = os.path.dirname(os.path.abspath(__file__))
cwd = os.path.join(_DIR, 'ts-parser')


def parse(file):
    p = subprocess.run(["node", "index.js",
                        f"--f={file}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
    return json.loads(p.stdout.decode('utf-8'))
