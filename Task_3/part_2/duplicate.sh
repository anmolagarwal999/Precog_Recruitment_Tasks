for file in ./*.xml
do
  echo $file
  str2=""
#   for j in $file
#   do
#     echo $j "="
#   done
#   echo "---------"
  a=${file%.*}
  a="${a}2.xml"
  echo $a
  head -200 $file > $a
done