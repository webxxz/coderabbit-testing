# backdoor.py

import subprocess
import os

password = "supersecret123"
api_key = "sk-abcdef123456"

def deploy():
    cmd = os.environ.get("DEPLOY_CMD", "ls")
    subprocess.call(cmd, shell=True)  # RCE risk
