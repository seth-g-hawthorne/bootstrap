# Launchpad: languages/bash
Resources for using bash and creating bash scripts

**Contents**
<!-- vscode-markdown-toc -->
* [Arguments](#Arguments)
* [Keys](#Keys)
* [Multiple commands](#Multiplecommands)
* [Subshell](#Subshell)
* [Redirects](#Redirects)
* [General](#General)
* [Articles](#Articles)
* [Tools](#Tools)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->
**Related**
  * [scripting](./scripting)

</br>

# CLI
## <a name='Arguments'></a>Arguments
  * `!$` - Arguments of previous command line
  * `!!` - Last command (useful if you forgot to prepend sudo: `sudo !!`)

## <a name='Keys'></a>Keys
  * `Tab` - Complete command arguments
  * ctrl-w - Delete last word
  * ctrl-u - Delete from cursor to start
  * alt-b | alt-f - Move word to word

  * ctrl-a - Move to end of line
  * ctrl-b - Move to beginning of line
  * ctrl-k - kill to end of line
  * ctrl-l - Clear screen
  * ctrl-r - Lookup command in history 

## <a name='Multiplecommands'></a>Multiple commands
  * *command-1* `;` *command-2* `;`  *command-3*  - Run commands sequentially
  * *command-1* `&&` *command-2* `&&` *command-3*  - Run commands sequentially; abort on error 

## <a name='Subshell'></a>Subshell
```
  (cd /some/other/dir && other-command)
```

## <a name='Redirects'></a>Redirects
```
  echo "redirect STDOUT" 1> file.txt
  echo "redirect STDERR" 2> file.txt
  echo "redirect both" &> file.txt
```


# Resources
## <a name='General'></a>General
  * [Bash cheatsheet](https://devhints.io/bash)

## <a name='Articles'></a>Articles
  * [Shell Programming Secrets Nobody Talks About](https://www.codeproject.com/Articles/5355689/Shell-Programming-Secrets-Nobody-Talks-About-Part) - Excellent discussion of shell constructs and their underlying implementation and history
  * [7 Tips to Write Better Bash Scripts in 2023](https://geekjob.tech/7-tips-to-write-better-bash-scripts-in-2023-8299f5a59b87)
  * [5 Less Known Bash Concepts To Level Up Your Linux Skills](https://levelup.gitconnected.com/5-less-known-bash-concepts-to-level-up-your-linux-skills-7bcf363804d1)

## <a name='Tools'></a>Tools 
  * [Online Bash Shell](https://www.jdoodle.com/test-bash-shell-script-online/)
  * [Explain shell](https://explainshell.com/) - Explaines contents of a command line
  * ShellCheck
    * [Online](https://www.shellcheck.net/)
    * [github](https://github.com/koalaman/shellcheck.net)
    * [VsCode ShellCheck](https://github.com/vscode-shellcheck/vscode-shellcheck)



