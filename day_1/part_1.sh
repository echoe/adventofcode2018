mytotal=0; for i in $(cat input.txt); do mytotal=$(( $mytotal + $i )); done; echo $mytotal
