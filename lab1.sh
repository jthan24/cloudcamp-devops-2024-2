
#!/bin/bash


if [ -d "$dir1" ]; then
    rm -rf dir1
fi
    mkdir dir1
    cd dir1

now=$(date +"%m_%d_%Y")

x=1
while [ $x -le 10 ]
do
  #echo fname(++x).txt
  #echo touch file x
  echo "${now}" > Test"$x".txt

x=$(( $x + 1 ))
done

