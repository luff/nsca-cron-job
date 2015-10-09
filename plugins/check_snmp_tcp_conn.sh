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

w=${w:-300}
c=${c:-300}

www="/var/www/html/tcp_conn"

walk="/usr/bin/snmpwalk -v2c -c$C -t$t -r3"

val=0
str="服务器tcp连接数"

$walk $H tcpConnState \
  | awk -F'[. ]' \
   '{ printf("%16s :%-6s%16s :%-6s %16s\n", $2"."$3"."$4"."$5, $6, $7"."$8"."$9"."$10, $11, $14) }' \
  > $www/$H.txt

if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
  str+="检测失败"
  val=3
else
  conn=($(wc -l $www/$H.txt)); conn=${conn[0]}
  str+="[$conn]个"
  str+=" | tcp_connection=$conn;$w;$c;"

  [[ $conn -lt $w ]] || val=1
  [[ $conn -lt $c ]] || val=2
fi

echo $str
exit $val

