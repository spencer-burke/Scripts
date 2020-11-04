#!/bin/bash
# creates the babysuid  problem writeup files

for i in {001..100}
do
    touch babysuid$i.txt
    echo $'Binary: \nSolution: \nFlag: \nExplanation: \n' > babysuid$i.txt

done

