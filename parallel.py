#!/usr/bin/env python
# coding: utf-8
#
# copyright (c) 2015 luffae@gmail.com
#

import config
import time
import subprocess


def parallel_execute(jobs):
  if not jobs: return

  output = ''
  processes = []
  while True:
    while jobs and len(processes) < config.max_parallel_job:
      job = jobs.pop()
      if config.debug:
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

epoch_minute = int(time.time() / 60)

job_list = []

for host in config.tree:
  for job in host['jobs']:
    j = dict()
    j['host'] = host['addr']
    j['desc'] = job['des']

    if (epoch_minute % job['i'] != 0):
      continue
    cmd = [ config.plugins_path + '/' + job['cmd'] ]

    cmd.extend([ '-H', str(host['addr']), '-s', str(host['snmp']) ])

    if 'w' in job:
      cmd.extend([ '-w', str(job['w']) ])
    if 'c' in job:
      cmd.extend([ '-c', str(job['c']) ])
    if 'k' in job:
      cmd.extend([ '-k', str(job['k']) ])

    j['cmd'] = cmd
    job_list.append(j)


result_list = parallel_execute(job_list)

if config.debug:
  print result_list
  exit(0)

send = subprocess.Popen(
       config.nsca_exec,
       stdin=subprocess.PIPE,
       stdout=subprocess.PIPE)

out, err = send.communicate(input=result_list)

