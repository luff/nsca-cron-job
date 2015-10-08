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

script_dir = sys.path[0]

service_definition = 'generic-passive-service'

buffer = ''

with open(script_dir + '/config.yaml') as cfg:
  config = myyaml.ordered_load(cfg)

for h, hv in config.iteritems():
  buffer += (
    "\n"
    "{0:/<64}\n".format('# ') +
    "# Configuration for " + h + "\n"
    "{0:/<64}\n".format('# ') + "\n"
  )
  buffer += (
    "define host {\n" +
    "    %-24s%s\n" % ('use', hv['template']) +
    "    %-24s%s\n" % ('host_name', hv['alias']) +
    "    %-24s%s\n" % ('alias', h) +
    "    %-24s%s\n" % ('address', hv['address']) +
    "}\n\n"
  )
  for j, jv in hv['jobs'].iteritems():
    fresh_second = jv['params']['I'] * 60 + 300
    buffer += (
      "define service {\n"
      "    %-24s%s\n" % ('use', service_definition) +
      "    %-24s%s\n" % ('host_name', hv['alias']) +
      "    %-24s%s\n" % ('service_description', j) +
      "    %-24s%d\n" % ('freshness_threshold', fresh_second) +
      "}\n\n"
    )

print buffer

