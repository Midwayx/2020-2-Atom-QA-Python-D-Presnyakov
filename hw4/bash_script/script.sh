#!/bin/bash


function statistics {

FILE=$1
echo -e "\\n#### task 1 #### \\n" >> answer.txt
grep -E "HTTP/[0-2\.]{3}" $FILE -c >> answer.txt && echo "done" || echo "failure"
echo -e "\\n#### task 2 #### \\n" >> answer.txt

awk '$6 ~ /"(POST|GET|PUT|DELETE|HEAD|OPTIONS|PATCH|TRACE|CONNECT)/{print $6}' $FILE |sort|uniq -c >> answer.txt

echo -e "\\n#### task 3 #### \\n" >> answer.txt
cat $FILE | sort -rnk10|awk '{print $7 " " $9 " " $10}'|head >> answer.txt
echo -e "\\n#### task 4 #### \\n" >> answer.txt
awk '$9 ~ /40[0-9]/ {print $0}' $FILE |uniq -c|sort -rnk1|head|awk '{print $8 " " $10 " " $2}' >> answer.txt
echo -e "\\n#### task 5 #### \\n" >> answer.txt
awk ' $9 ~ /50[0-9]/{print $0}' $FILE |sort -rnk10|head|awk '{print $7 " " $9 " " $1}' >> answer.txt
}

ARG=$1
echo "run $0" > answer.txt
if [ -n "$ARG" ]
then
if [ -f "$ARG" ]
then
statistics $ARG
elif [ -d "$ARG" ]
then
for file in $ARG/*
do
if [ -f "$file" ]
then
echo $file >> answer.txt
statistics $file
fi
done
fi
else
echo "Incorrect input: missed path to log files"
fi

