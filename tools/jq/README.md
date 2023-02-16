# Launchpad: tools/jq

## Installation

# Examples
  * `alias getjson="curl 'https://api.github.com/repos/stedolan/jq/commits?per_page=5'"`
    * `getjson | jq .`    - pretty print
    * `getjson |.[]`      - print all array elements
    * `getjson |.[0]`     - print first array element
    * `getjson |'.[] | {message: .commit.message, name: .commit.committer.name}` - Print fields, all array elements
    * `getjson |'[.[] | {message: .commit.message, name: .commit.committer.name}]'` - Collect fields for all array elements as an array

# Resources
  * [Cheatsheet](https://gist.github.com/olih/f7437fb6962fb3ee9fe95bda8d2c8fa4)
  * [Manual](https://stedolan.github.io/jq/manual/)
  * [Guide to jq](https://www.baeldung.com/linux/jq-command-json)
  * [Tutorial](https://docs.0install.net/basics/menu/)
  * [Select objects based on value of variable in object using jq](https://stackoverflow.com/questions/18592173/select-objects-based-on-value-of-variable-in-object-using-jq)