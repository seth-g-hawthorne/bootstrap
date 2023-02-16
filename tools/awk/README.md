# Launchpad: tools/awk

## Phases
  1. Execute commands from BEGIN block
  2. Read line from input stream
  3. Execute awk commands on line
  4. Goto 2 if not EOF
  5. Executed commands from END block


## Examples
```
awk 'BEGIN{printf "Sr No\tName\tSub\tMarks\n"} {print}' marks.txt
awk 'BEGIN{printf "Sr No\tName\tSub\tMarks\n"} {print}' marks.txt
awk -f command.awk marks.txt
awk -v name=Jerry 'BEGIN{printf "Name = %s\n", name}'
awk --dump-variables ''
cat awkvars.out
awk '{print $3 "\t" $4}' marks.txt

```

```
# awk: the same than cut, but more flexible with delimiters, with more filters, and more computacionally complex
awk '{print $3}' sales.txt # print only the 3rd column
awk '{print $2 ", " $3}' sales.txt # print the 2nd and 3rd columns, separated with a comma
awk '{print $2 + $3}' sales.txt # print the sum of the 2nd and 3rd columns
awk 'length($0) > 20' sales.txt # print those lines whose length is longer than 20 characters
awk '$2 > 100' sales.txt # print those lines where the value of the second column is greater than 100
```

## Related Information
  * [Tutorial](https://www.tutorialspoint.com/awk/index.htm)
  * [Cheatsheet](https://www.shortcutfoo.com/app/dojos/awk/cheatsheet)
  * [Intro to awk](https://www.grymoire.com/Unix/Awk.html)
  * [Arithmetic ops](https://www.gnu.org/software/gawk/manual/html_node/Arithmetic-Ops.html )


