DIM=$1
WIN=$2
FILENAME=w2v-$DIM-1b-win-$WIN
nohup time ./convertvec bin2txt ../$FILENAME.bin ../$FILENAME.txt > /dev/null 2>&1 &
