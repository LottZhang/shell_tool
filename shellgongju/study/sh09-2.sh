#!/bin/bash
function printit(){
	echo "you choice is $1"
}
case $1 in
  "one")
    printit 1
    ;;
  "two")
    printit 2
    ;;
  *)
    echo "usage hello limited"
    ;;
esac
