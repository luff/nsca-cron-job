#!/usr/bin/env bash
#
# copyright (c) 2015 luffae@gmail.com
#

while getopts ":I:H:i:f:k:w:c:" o; do
  case "${o}" in
    I) I=${OPTARG} ;; # interval
    H) H=${OPTARG} ;; # host
    i) i=${OPTARG} ;; # es-index
    f) f=${OPTARG} ;; # es-field
    k) k=${OPTARG} ;; # es-keyword
    w) w=${OPTARG} ;; # warning
    c) c=${OPTARG} ;; # critical
    ?) shift
  esac
done

rx="([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
[[ "$H" =~ ^$rx\.$rx\.$rx\.$rx$ ]] || exit 1

w=${w:-1}
c=${c:-1}
I=${I:-30}; I=$((I * 60))

ep=$(date +%s)
te=$((ep / I * I * 1000))
ts=$((te - I * 1000))

[[ -n $k ]] || exit 3

cnt=$(curl -s -XGET 'http://10.0.0.195:9200/*_hy_'$i'/_count' -d \
'{
  "query": {
    "filtered": {
      "query": {
        "query_string": {
          "analyze_wildcard": "true",
          "query": "'$f': \"'$k'\""
        }
      },
      "filter": {
        "and": [{
          "range": { "@timestamp": { "from": '$ts', "to": '$te' } }
        }, {
          "term": { "host": "'$H'" }
        }]
      }
    }
  }
}' | grep -oP '(?<=\"count\":)\d+')

val=0
str="日志分析[$i]字段[$f]关键字[$k]"

if [[ -n $cnt ]]; then
  [[ $cnt -lt $w ]] || val=1
  [[ $cnt -lt $c ]] || val=2
  str+="于最近[$I]秒内出现[$cnt]次"
else
  str+="检测失败"
  val=2
fi

echo $str
exit $val

