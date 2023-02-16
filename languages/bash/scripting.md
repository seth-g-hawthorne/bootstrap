# Jumpstart: linux/bash/scripting

**Contents**
  * Constructs
    * [Arguments](#Arguments)
    * [Arrays](#Arrays)
    * [Functions](#Functions)
    * [Heredoc](#Heredoc)
    * [Loops](#Loops)
  * [Resources](#Resources)

<br/>

# Constructs
## Arguments
  * `$#` - Number of arguments
  * `$*` - All arguments 
  * `$`_n_ - Argument _n_


```
  if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
  fi

  if [ -z "$1" ]
  then
    echo "No argument supplied"
  fi
```

## Arrays
```
   sizes=(1 2 4 8 16 32 64 128)
   echo ${sizes[@]}
   for s in ${sizes[@]}; do
     echo $s
   done
```

## Functions
### Declaration
```
  foo () {
    echo "Function foo called"
  }

  foo
```
### Arguments
```
  #!/bin/bash

  answer () {
    while read response; do
      echo
        case $response in
          [yY][eE][sS]|[yY])
            printf "$1\n"
            return 0
            break
            ;;
          [nN][oO]|[nN])
            printf "$2\n"
            return 1
            break
            ;;
          *)
            printf "Please, enter Y(yes) or N(no)! "
        esac
    done
  }

  echo -e "\nRun application? (Yes/No) "
  answer "Run" "Will not run" && echo "I'm script" || echo "Doing nothing"
```

### Local variables
```
inc () {
  lvar=1
  (( lvar++ ))
  echo $lvar
}

inc
```

### Recursion
```
  count=0
  level=4

  recurse () {
    count=$(( $count + 1 ))
    echo $count

    while [ $count -le $level ]; do
      recurse
    done
  }

  recurse
```

### Export for use by other scripts
```
  hello () {
    echo "hello"
  }

  export -f hello
```

### Existence
```
  exists() {
    declare -f "$@" > /dev/null && echo "$@ exists" || echo  "$@ does not exist"
  }
```

### Return value
```
  function myfunc()   {
      echo "result
  }

  echo $(myfunc)   
  ```

## Heredoc
```
  cat << END
  Heredoc text line 1
  Heredoc text line 2
  END 

```

## Loops
```
   until [ -f /tmp/examplefile.txt ]
   do
     sleep 5
   done
```



# Resources
## General
  * [Bash cheatsheet](https://devhints.io/bash)

## Scripting
  * [Linux Bash scripting blog series](https://faun.pub/linux-bash-scripting-part1-4bc70d4942c6)
  * [The art of the command line](https://github.com/jlevy/the-art-of-command-line)
  * [Ultimate guide to modernizing bash script code](https://medium.com/mkdir-awesome/the-ultimate-guide-to-modularizing-bash-script-code-f4a4d53000c2) - Multi-file script with colorization

### Constructs
  * [Heardoc tutorial](https://linuxhint.com/bash-heredoc-tutorial/)
  * [Function return values](https://www.linuxjournal.com/content/return-values-bash-functions)
  * [Avoid eval in bash](https://stackoverflow.com/questions/17529220/why-should-eval-be-avoided-in-bash-and-what-should-i-use-instead/17529221#17529221)

