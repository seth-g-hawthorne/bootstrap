# Launchpad: tools/parallel
GNU tool that executes commands in parallel

## Installation
### Linux
```
sudo apt install parallel
```

## Example
```
parallel wget -q {} :::: download_links.txt
```

## Resources
  * [Manual](https://www.gnu.org/software/parallel/man.html)
  * [Tutorial](https://www.gnu.org/software/parallel/parallel_tutorial.html)

