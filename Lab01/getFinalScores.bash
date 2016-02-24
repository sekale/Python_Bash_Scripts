#! /bin/bash
#
#$Author: ee364a09 $
#$Date: 2016-01-19 14:26:40 -0500 (Tue, 19 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a09/Lab01/getFinalScores.bash $
#$Revision: 86155 $

NumParams=$#
ParamValues=$@

if ((NumParams != 1))
	then
		echo "Usage: ./getFinalScores.bash <filename>"
		exit 1
	fi

if [[ ! -e $1 ]]
	then
		echo "Error reading input file: $1"
		exit 2
	fi

#echo $1

variable=$(echo "$1" | cut -d '.' -f1)
if [[ ! -e $variable.out ]]
then
touch $variable.out

elif [[ -e $variable.out ]]	
then
	echo "Output file $variable.out already exists."
	exit 3
fi

finalscore=0
while IFS=, read score1 score2 score3 score4 score5
do
	#echo $score2 
	(( finalscore=((score2*15)/100) + ((score3*30)/100) + ((score4*30)/100) + ((score5*25)/100) ))

	echo -n $score1 >> $variable.out
	echo ",$finalscore">> $variable.out
	#echo " $finalscore" > $variable.out
done < "$1"



exit 0
