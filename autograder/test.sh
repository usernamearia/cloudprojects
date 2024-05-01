#!/bin/bash
tmpoutput=$(echo -e "freddy\nsusan" | ./uploads/a.out)
echo "Program output: $tmpoutput"
CORRECT=0

if echo "$tmpoutput" | grep -q 'freddy'; then
  let CORRECT=CORRECT+1
  echo "Found 'freddy'"
fi

if echo "$tmpoutput" | grep -q 'susan'; then
  let CORRECT=CORRECT+1
  echo "Found 'susan'"
fi

echo "Score: $CORRECT"
exit $CORRECT

