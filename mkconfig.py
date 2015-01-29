#!/usr/bin/env python
# coding: utf-8
#
# copyright (c) 2015 luffae@gmail.com
#

import config

host_definition = 'windows-server'
service_definition = 'generic-passive-service'

buffer = ''

for h in config.tree:
  buffer += (
    "\n"
    "{0:/<64}\n".format('#') +
    "# Configuration for " + h['addr'] + "\n"
    "{0:/<64}\n".format('#') + "\n"
  )
  buffer += (
    "define host {\n" +
    "    %-24s%s\n" % ('use', host_definition) +
    "    %-24s%s\n" % ('host_name', h['addr']) +
    "    %-24s%s\n" % ('alias', h['addr']) +
    "    %-24s%s\n" % ('address', h['addr']) +
    "}\n\n"
  )
  for j in h['jobs']:
    buffer += (
      "define service {\n"
      "    %-24s%s\n" % ('use', service_definition) +
      "    %-24s%s\n" % ('host_name', h['addr']) +
      "    %-24s%s\n" % ('service_description', j['des']) +
      "    %-24s%d\n" % ('freshness_threshold', j['i'] * 60 + 300) +
      "}\n\n"
    )

print buffer

