#/bin/bash

files="$(ampy ls)" # это массив, а не строка
files2="${files[0]}"


#echo "${files2[0]}"

IFS=/ read -r -a array <<< "$files2"
for i in "${array[*]}"
do
    echo "$i"
done


