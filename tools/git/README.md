# Launchpad: tools/git

# Configuration
### Setup
Run `git-config.sh` or issue the following commands:
```
git config --global color.ui true
git config --global user.name "First Last"
git config --global user.email "emai@example.com"
git config --global push.default current
git config -l
```

## Ssh keys 
  * `ssh-keygen -t rsa -b 4096 -C "user@gmail.com”`
  * `cat ~/.ssh/id_rsa.pub1
  * `ssh -vT git@github.com`



## Pretty logging
```
.gitconfig
[aliases]
lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --branches
```

## Envrionment variables
```
export GIT_SSL_NO_VERIFY=1
```

# Commands
  * `git init`                           - Initialize current directory as a repo
  * `git add .`                          - Stage new files
  * `git add -A .`                       - Stage files such that the index matches the working tree 
  * `git add -u .`                       - Stage updated files
  * `git add -e .`                       - Edit differences between index and tree and apply result
  * `git branch` *new-branch*            - Create *new-branch* from current point in history  
  * `git branch` *new-branch* *tag-orid* - Create *new-branch* from specified point in history 
  * `git branch -a`                      - List all branches 
  * `git branch -r`                      - List remote branches 
  * `git branch --sort=-committerdate`   - List branches sorted by commit date 
  * `git checkout` *branch*              - Switch to branch *branch*
  * `git checkout -b` *branch*           - Create and switch to branch *branch*
  * `git checkout --` *files*            - Undo uncommited changes to *files*
  * `git clone` [-depth n] *repo*        - Clone a repo
  * `git commit -m` *message*            - Commit the staged files
  * `git commit -m` *message* -a         - Stage and commit modified files
  * `git log --pretty=oneline --graph --decorate --all`
  * `git mv` *old-loc* *new-loc*         - Stage file or directory move
  * `git pull origin`                    - Fetch and merge changes from `origin` into current branch
  * `git pull` *remote*                  - Fetch and merge changes from *remote* brnach into current branch
  * `git push` *remote* *branch*         - Push changes to remote repository
  * `git status`                         - Display status of local changes 
  * `git reset --head`                                  - Revert to last commit
  * `git reset HEAD --` *files*          - Unstage change to *files*  
  * `git rm --` *file*                   - Stage file deletion 
  * `git rm -r --` *dir*                 - Stage directory deletion (recursive)


# Use Cases

## Creating a new repo
Replace project and user with appropriate values.
```
export GIT_USER=user
export GIT_PROJECT=project
echo "# ${GIT_PROJECT}" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:${GIT_USER}${GIT_PROJECT}.git
git push -u origin master
```

## Create Pull request
```
git clone https://github.com/user/sapientia-api.git
git checkout -b feature-branch
```
make changes to files 
```
git add .
git commit -m "change message"
git remote add origin
git push -u origin master
```
From the Git UI create a new pull request for the newly created branch


## Update dev branch with changes from master
  * `git pull`
  * Merge changes either by
    * `git merge master` - creates a new commit
    * `git rebase` 

## Fixing Problems 
See: [Oh Shit, Git!?!](https://ohshitgit.com/)

## Accidentally committed changes on master
  * Create a dev branch: `git checkout -b` *dev-branch*
  * Find the ID of the change on master:`git log` 
  * Revert the change on master: `git reset` *id*
  * Commit the changes on the dev branch

## Change message or add files to last commit
  * `git --amend`

## Undo commit from local branch
  * `git reset --hard` *id*

## Undo commit pushed to remote repo
  * `git revert` *id*


# Related Information
## General
  * [cheatsheet](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)
  * [git-scm Command Reference](https://git-scm.com/docs)
  * [GitHub Docs](https://docs.github.com/en)
  * [Oh Shit, Git!?!](https://ohshitgit.com/)
  * [Learn git branching](https://learngitbranching.js.org/)
  * [Atlasian git tutorials](https://www.atlassian.com/git/tutorials)
  * [Git the simple guide](http://up1.github.io/git-guide/index.html)
  * [Git Immersion](https://gitimmersion.com/index.html)
  * [On Git and Cognitive Load](https://dzone.com/articles/on-git-and-cognitive-load)

## Configuration
  * [Generating an ssh key and adding it to github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
  * [.gitignore files](https://github.com/github/gitignore)

## Use cases 
  * [Git forking](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
  * [Commands to keep a fork up-to-date](https://dzone.com/articles/git-commands-to-keep-a-fork-up-to-date)
  * [Standard workflow for pull requests](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
  * [How to push an existing project to github](https://www.digitalocean.com/community/tutorials/how-to-push-an-existing-project-to-github)

## Tools
  * [Github Desktop](https://desktop.github.com/)
