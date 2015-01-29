#
# coding: utf-8
#
# copyright (c) 2015 luffae@gmail.com
#

debug = False
max_parallel_job = 64

plugins_path = '/usr/lib64/nagios/plugins'

nsca_server = '10.0.0.109'
nsca_exec = [ '/usr/sbin/send_nsca', nsca_server, '-to', '60' ]


tree = [
# ----------------------------------------------
{
  'addr': '10.0.0.169',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 200,
    'c': 200,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.151',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 70,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 600,
    'c': 600,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.152',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 1500,
    'c': 1500,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.153',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 600,
    'c': 600,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.154',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 1600,
    'c': 1600,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.155',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 600,
    'c': 1200,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.157',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 400,
    'c': 400,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.158',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 25,
    'c': 50,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 600,
    'c': 600,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.159',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 1500,
    'c': 1500,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.161',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 50,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 800,
    'c': 800,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.162',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 70,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 300,
    'c': 300,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.163',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 80,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 200,
    'c': 200,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.165',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 200,
    'c': 200,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.166',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 1400,
    'c': 1400,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.168',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 100,
    'c': 100,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.146',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 100,
    'c': 100,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.147',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 200,
    'c': 200,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.148',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 200,
    'c': 200,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.149',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 100,
    'c': 100,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '172.16.0.41',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 100,
    'c': 100,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.211',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 75,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 100,
    'c': 100,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.212',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 100,
    'c': 100,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.213',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 100,
    'c': 100,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.214',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 100,
    'c': 100,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.241',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 100,
    'c': 100,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.243',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 50,
    'c': 60,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }, {
    'des': 'IIS-CONNECTIONS',
    'cmd': 'hy/check_snmp_iis_conn.sh',
    'w': 100,
    'c': 100,
    'i': 5
  }, {
    'des': 'HTTPERR-CONNECTION-DROPED',
    'cmd': 'hy/check_httperr_reason.sh',
    'k': 'Connection_Dropped',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-CONNECT-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法连接',
    'w': 1,
    'c': 10,
    'i': 30
  }, {
    'des': 'APPLOG-RESOLVE-FAILED',
    'cmd': 'hy/check_applog_keyword.sh',
    'k': '无法解析',
    'w': 1,
    'c': 10,
    'i': 30
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.22',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.23',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 80,
    'c': 98,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.24',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.25',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.26',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.27',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.112',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.113',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.118',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.120',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.121',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.122',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.123',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.125',
  'snmp': '',
  'jobs': []
},
# ----------------------------------------------
{
  'addr': '10.0.0.130',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.141',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.142',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.144',
  'snmp': 'huiyuan',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.160',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.170',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
},
# ----------------------------------------------
{
  'addr': '10.0.0.180',
  'snmp': 'public',
  'jobs': [{
    'des': 'CPU-USAGE',
    'cmd': 'hy/check_snmp_cpuload.sh',
    'w': 10,
    'c': 30,
    'i': 5
  }, {
    'des': 'MEMORY-USAGE',
    'cmd': 'hy/check_snmp_memory.sh',
    'w': 80,
    'c': 95,
    'i': 5
  }, {
    'des': 'DISK-USAGE',
    'cmd': 'hy/check_snmp_disk.sh',
    'w': 70,
    'c': 80,
    'i': 30
  }, {
    'des': 'TIME-DIFFERENCE',
    'cmd': 'hy/check_snmp_timediff.sh',
    'w': 40,
    'c': 60,
    'i': 60
  }]
}
]
