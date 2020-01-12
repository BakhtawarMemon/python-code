#!/bin/bash
export LOGFILE=./logfile.log
declare -i label; label=0
running="no"
name=""

track(){
if [[ "$1" == "start" && "$running" == "no" ]]; then
	running="yes"
	((label++))
	if [[ "$2" != "" ]]; then
		name=$2
	else
		name=$label
	fi
	echo "START $(date)" >> $LOGFILE
	echo "LABEL This is task $name" >> $LOGFILE
	start_time=$(date +%T); start_time_secs=$(date +%s -d ${start_time}); printf "$start_time_secs;" >> timestamp.txt
elif [[ "$1" == "start" && "$running" == "yes" ]]; then
	echo "Task is already running. Type track stop to stop the current task and then start new one"
elif [[ "$1" == "stop" && "$running" == "yes" ]]; then
	running="no"
	echo "END $(date)" >> $LOGFILE
	end_time=$(date +%T); end_time_secs=$(date +%s -d ${end_time}); echo $end_time_secs >> timestamp.txt
elif [[ "$1" == "stop" && "$running" == "no" ]]; then
	echo "No task is currently running"
elif [[ "$1" == "status" && "$running" == "yes" ]]; then
	echo "We are currently tracking task $name"
elif [[ "$1" == "status" && "$running" == "no" ]]; then
	echo "We don't have any active tasks"
elif [[ "$1" == "log" ]]; then
	declare -i counter
	counter=1
	input=./timestamp.txt
	while IFS= read -r line
		do
			start_time=$(echo $line | cut -d ";" -f 1)
			end_time=$(echo $line | cut -d ";" -f 2)
			((diff=end_time-start_time))
			result=$(date +%T -ud @${diff})
			echo "Task $counter: $result"
			((counter++))
		done < "$input"
else
	echo "Invalid input. Type track start, stop or status to start a new task, stop a current task or to check the status of current task respectively"
fi
}
