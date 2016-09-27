# JSON Generator
A simple python script that generates a json model template. Does not generate dummy data

# Usage

To use this tool, simply clone the repository and then run `pip install .` in the json-generator directory.

## Included commands
* `--help` lists the commands in the command line
* `--obj` or `-o` names the JSON object
* `--element` or `-e` names the objects elements
* `--key` or `-k` names the keys inside of the element 
* `--repeat` or `-r` the amount of elements repeated
* `--id` or `-id` specifices whether or not IDs are keys, this is set True by default

### Example Command

`jg -o people -e person -k name -k surname -k number -r 3` will give [this output](https://gist.github.com/AwolDes/7a95d06623d4cbe6d5fc)

