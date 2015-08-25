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

w=${w:-10}
c=${c:-30}

walk="/usr/bin/snmpwalk -v2c -c$C -OUvq -t$t -r3"

val=0
str="服务器cpu使用率"

load_list=($($walk $H hrProcessorLoad))

if [[ $? -ne 0 ]]; then
  str+="检测失败"
  val=2
else
  for l in ${load_list[@]}; do
    total=$((total + l))
    count=$((count + 1))
  done

  p=$((total / count))
  str+="[$p%]"

  [[ $p -lt $w ]] || val=1
  [[ $p -lt $c ]] || val=2
fi

echo $str
exit $val

