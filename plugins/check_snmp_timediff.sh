#!/usr/bin/env bash
#
# copyright (c) 2015 luffae@gmail.com
#

while getopts ":H:C:t:w:c:" o; do
  case "${o}" in
    H) H=${OPTARG} ;; # host
    C) C=${OPTARG} ;; # community
    t) t=${OPTARG} ;; # timeout
    w) w=${OPTARG} ;; # warning
    c) c=${OPTARG} ;; # critical
    ?) shift
  esac
done

rx="([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
[[ "$H" =~ ^$rx\.$rx\.$rx\.$rx$ ]] || exit 1

C=${C:-public}
t=${t:-2}

w=${w:-30}
c=${c:-60}

walk="/usr/bin/snmpwalk -v2c -c$C -OUvq -t$t -r3"

val=0
str="服务器时间差异"

std_time=$(date +%s)

dt=$($walk $H hrSystemDate.0)
if [[ $? -ne 0 ]]; then
  str+="检测失败"
  val=3

else
  dt=$(date -d"${dt//,/ }" +%s)
  diff=$((dt - std_time))

  [[ $diff -gt -$w && $diff -lt $w ]] || val=1
  [[ $diff -gt -$c && $diff -lt $c ]] || val=2

  str+="[$diff]秒"
fi

echo $str
exit $val

