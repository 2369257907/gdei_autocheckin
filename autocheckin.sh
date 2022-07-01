#!/bin/bash


#填写账号和加密后的密码
username="替换为账号名"
password="xx替换为加密后的密码xx"

#登陆并获取cookie
cookie=$(curl -D - 'https://tb.gdei.edu.cn/login' -H 'Connection: keep-alive' -H 'sec-ch-ua: "Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"' -H 'Accept: */*' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'sec-ch-ua-mobile: ?0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31' -H 'sec-ch-ua-platform: "Windows"' -H 'Origin: https://tb.gdei.edu.cn' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Referer: https://tb.gdei.edu.cn/login' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' --data "username=$username&password=$password&rdf=on" -X POST -sSL -o /dev/null --compressed | grep JSESSIONID= | awk -F= '{print $2}' | awk -F\; '{print $1}')

echo $cookie
#获取当前时间
time=$(date +%s)

#一键打卡
resp1=$(
curl "https://tb.gdei.edu.cn/system/yqdc/yjtb?_=$time" \
-X 'GET' \
-H 'Accept: */*' \
-H "Cookie: JSESSIONID=$cookie" \
-H 'Accept-Language: zh-CN,zh-Hans;q=0.9' \
-H 'Host: tb.gdei.edu.cn' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15' \
-H 'Referer: https://tb.gdei.edu.cn/system/main' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Connection: keep-alive' \
-H 'X-Requested-With: XMLHttpRequest'
  )

#一键晨午检
resp2=$(
  curl -s "https://tb.gdei.edu.cn/system/mrcj/yjcwj?_=$time" \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: "Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"' \
  -H 'Accept: */*' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://tb.gdei.edu.cn/system/main' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H "Cookie: JSESSIONID=$cookie" \
  --compressed
)
echo "-----------------------------------"
echo $resp1

case $resp1 in
    "1")  echo '一键打卡成功'
    ;;
    "2")  echo '您还没有健康填报，不能一键打卡'
    ;;
    "3")  echo '你今天打过卡了'
    ;;
    "4")  echo '问卷有更新，请重新填报'
    ;;
    *)  echo '打卡失败'
    ;;
esac

echo "-----------------------------------"
echo $resp2

case $resp2 in
    "1")  echo '您今天已经晨午检'
    ;;
    "succC")  echo '一键晨午检成功'
    ;;
    "5")  echo '非晨午检时间'
    ;;
    *)  echo '晨午检失败'
    ;;
esac

