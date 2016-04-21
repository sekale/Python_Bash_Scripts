#! /bin/bash

Params=$@
NumParams=$#

if (( NumParams != 1 ))
then
	echo "No. of parameters must be 1"
	exit 1
fi

if [[ ! -e $1 ]]
then
    echo "Error: $1 doesn't exist"
    exit 2
fi


if [[ ! -e schedule.out ]]
then
	echo "We can continue"
	touch schedule.out
	chmod +x schedule.out
else
	echo "Error: schedule.out does exist"
	#exit 3
fi
n=1

while read line
	do
	#			while read line
	#			do
	#					if (( $count_val1 < 3))
	#					then
	#						variable2=$(echo $line | cut -d ' ' -f1)
	#						variable3=$(echo $line | cut -d ' ' -f12)
	#						echo "PID: $variable2, cmd: $variable3"
	#					else
	#					break
	#					fi
	#					((count_val1=$count_val1 + 1))

#				done < logfile4.txt			
#


#					if [[ ! -e outfile4.txt ]]
#					then
#					touch outfile4.txt
#					chmod +x outfile4.txt
#					fi
#				echo "Please enter a username: "
#				read name
#				cat outfile.txt | grep "$name" >outfile4.txt



	chmod +x schedule.out
	chmod +x schedule.out.gold
	cp schedule.out.gold schedule.out

	echo $line
	#outfile = schedule.out
	done < $1


exit 0



