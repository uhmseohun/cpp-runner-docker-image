import subprocess
import json
import sys
import os

with open("./build-context.json") as build_context_file:
  build_context = json.load(build_context_file)

properties = ["username", "stage_id", "instance_id", "extension"]

for property in properties:
  if property not in build_context:
    print("Check Property")
    sys.exit("Check Property '{}' in Build Context".format(property))

stage_id = build_context["stage_id"]
instance_id = build_context["instance_id"]
extension = build_context["extension"]

code_path = "{}-{}.{}".format(stage_id, instance_id, extension)

if not os.path.exists(code_path):
  sys.exit("Check file '{}'".format(code_path))

os.system("g++ -o ./{} {}".format(instance_id, code_path))

process = subprocess.Popen(["./{}".format(instance_id)],
  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

stdout = stdout.decode('utf8')

print ("[*] Result : {}".format(stdout))
