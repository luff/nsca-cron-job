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

scripts_base = '/root/scripts/nsca_cron_new'

host_definition = 'windows-server'
service_definition = 'generic-passive-service'

buffer = ''

with open(scripts_base + '/config.yaml') as cfg:
  config = myyaml.ordered_load(cfg)

for h in config.keys():
  buffer += (
    "\n"
    "{0:/<64}\n".format('# ') +
    "# Configuration for " + h + "\n"
    "{0:/<64}\n".format('# ') + "\n"
  )
  buffer += (
    "define host {\n" +
    "    %-24s%s\n" % ('use', host_definition) +
    "    %-24s%s\n" % ('host_name', h) +
    "    %-24s%s\n" % ('alias', h) +
    "    %-24s%s\n" % ('address', h) +
    "}\n\n"
  )
  for j in config[h].keys():
    fresh_second = config[h][j]['params']['I'] * 60 + 300
    buffer += (
      "define service {\n"
      "    %-24s%s\n" % ('use', service_definition) +
      "    %-24s%s\n" % ('host_name', h) +
      "    %-24s%s\n" % ('service_description', j) +
      "    %-24s%d\n" % ('freshness_threshold', fresh_second) +
      "}\n\n"
    )

print buffer

