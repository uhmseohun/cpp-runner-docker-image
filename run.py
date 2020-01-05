import subprocess
import json
import sys
import os

with open('./build-context.json') as build_context_file:
  build_context = json.load(build_context_file)

fields = ['username', 'stage_id', 'instance_id', 'extension']

for field in fields:
  if field not in build_context:
    print('Check Property')
    sys.exit(f"Check Property '{field}' not in Build Context")

stage_id = build_context['stage_id']
instance_id = build_context['instance_id']
extension = build_context['extension']

code_path = f'{stage_id}-{instance_id}.{extension}'

if not os.path.exists(code_path):
  sys.exit(f"Check file '{code_path}'")

os.system(f'g++ -o ./{instance_id} {code_path}')

process = subprocess.Popen([f'./{instance_id}'],
  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

stdout = stdout.decode('utf8')

print (f'[*] Result : {stdout}')
