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
t=${t:-15}

w=${w:-60}
c=${c:-80}

walk="/usr/bin/snmpwalk -v2c -c$C -OUvq -t$t -r3"

val=0
str="服务器磁盘使用率"

mapfile -t desc < <($walk $H hrStorageDescr)
mapfile -t size < <($walk $H hrStorageSize)
mapfile -t used < <($walk $H hrStorageUsed)
#mapfile -t sau < <($walk $H hrStorageAllocationUnits)

for ((i=0; i<${#desc[@]}; i++)); do
  n=${desc[$i]}

  if [[ $n =~ "Serial Number" ]]; then
    u=$((${used[$i]} * 100 / ${size[$i]}))

    str+="'${n%% *}' [$u%]; "
    if [[ $u -ge $c ]]; then
      val=2
    elif [[ $u -ge $w ]]; then
      val=1
    fi
  fi
done

echo $str
exit $val

