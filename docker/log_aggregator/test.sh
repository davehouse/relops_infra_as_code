#!/usr/bin/env bash

function assert() {
    $1 || (
      echo "Assert failed: \"$1\""
      exit 1
    )
}
levels="DEBUG INFO NOTICE WARN ERR CRIT ALERT EMERG"

docker-compose up -d --remove-orphans --force-recreate
#sleep 5

while [[ $(docker-compose ps | wc -l) -lt 3 ]]; do
    sleep 1
    printf "."
done

docker-compose exec rsyslog-client sh -c 'logger "client hostname:$(hostname)"'
docker-compose exec rsyslog-client sh -c 'for level in '"$levels"'; do sleep 1; logger -p $level test_${level}_message; done'
sleep 5

messages=$(docker-compose logs log-aggregator | grep '"message":"client hostname:\|test_[^_]*_message')
declare -l match_levels
match_levels=${levels// /\\|}
found_messages=$(echo "$messages" | grep "rsyslog\.user\.\(${match_levels}\)")

client_hostname=$(echo "$found_messages" | grep -o 'client hostname:[^ \"]*' | cut -d':' -f2)
echo $client_hostname
echo "$found_messages" | grep -o 'test_[^_]*_message' | sort | uniq -c

remote_logs=""
while ! $(echo "$remote_logs" | grep "$client_hostname"); do
    remote_logs=$(docker-compose run read-logs)
    printf "."
done
remote_logs=$(docker-compose run read-logs)
echo "$remote_logs"

docker-compose down -q
#messages_on_stackdriver=$(docker-compose logs --tail=10 read-logs)
#echo "$messages_on_stackdriver" | grep
#docker-compose down
