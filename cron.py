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

script_dir = sys.path[0]
plugin_dir = script_dir +'/plugins'

nsca_server = '192.168.181.100'
nsca_exec = [ '/usr/sbin/send_nsca', nsca_server, '-to', '60' ]


def parallel_execute(jobs):
  if not jobs: return

  output = ''
  processes = []
  while True:
    while jobs and len(processes) < max_parallel_job:
      job = jobs.pop()
      if debug:
        print subprocess.list2cmdline(job['exec'])

      processes.append({
        'host': job['host'],
        'desc': job['desc'],
        'proc': subprocess.Popen(job['exec'], stdout=subprocess.PIPE)
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

with open(script_dir + '/config.yaml') as cfg:
  config = myyaml.ordered_load(cfg)

for h, hv in config.iteritems():
  for j, jv in hv['jobs'].iteritems():
    if not debug and (epoch_minute % jv['params']['I'] != 0):
      continue

    cmd = [ plugin_dir + '/' + jv['cmd'], '-H', hv['address'] ]
    if jv['snmp']:
      cmd.extend([ '-C', str(hv['community']) ])
    for p, pv in jv['params'].iteritems():
      cmd.extend([ '-' + p, str(pv) ])

    job_list.append({
      'host': hv['alias'],
      'desc': j,
      'exec': cmd
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

