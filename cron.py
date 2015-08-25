#!/usr/bin/env python
# coding: utf-8
#
# copyright (c) 2015 luffae@gmail.com
#

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.dont_write_bytecode = True

import myyaml
import time
import subprocess

debug = False

max_parallel_job = 64
scripts_base = '/root/scripts/nsca_cron_new'
plugins_path = '/root/scripts/nsca_cron_new/plugins'

nsca_server = '10.0.0.109'
nsca_exec = [ '/usr/sbin/send_nsca', nsca_server, '-to', '60' ]


def parallel_execute(jobs):
  if not jobs: return

  output = ''
  processes = []
  while True:
    while jobs and len(processes) < max_parallel_job:
      job = jobs.pop()
      if debug:
        print subprocess.list2cmdline(job['cmd'])

      processes.append({
        'host': job['host'],
        'desc': job['desc'],
        'proc': subprocess.Popen(job['cmd'], stdout=subprocess.PIPE)
      })

    for p in processes:
      if p['proc'].poll() is not None:
        processes.remove(p)
        output += (
          str(p['host']) + '\t' +
          str(p['desc']) + '\t' +
          str(p['proc'].returncode) + '\t' +
          str(p['proc'].communicate()[0])
        )

    if not processes and not jobs:
      break
    else:
      time.sleep(0.05)

  return output


#-----------------------------------------------------------------------
# main entrance
#-----------------------------------------------------------------------

epoch_minute = int(round(time.time() / 60))

job_list = []

with open(scripts_base + '/config.yaml') as cfg:
  config = myyaml.ordered_load(cfg)

for h in config.keys():
  for j in config[h].keys():
    job = config[h][j]
    if not debug and (epoch_minute % job['params']['I'] != 0):
      continue
    cmd = [ plugins_path + '/' + job['cmd'] ]
    for p in job['params'].keys():
      cmd.extend([ '-' + p, str(job['params'][p]) ])
    job_list.append({
      'host': h,
      'desc': j,
      'cmd': cmd
    })

result_list = parallel_execute(job_list)

if debug:
  print result_list
  exit(0)

send = subprocess.Popen(
       nsca_exec,
       stdin=subprocess.PIPE,
       stdout=subprocess.PIPE)

out, err = send.communicate(input=result_list)
