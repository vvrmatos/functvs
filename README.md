# Functvs
This is an open-source advanced mathematics library

**Source Code**: <a href="https://github.com/shimon-d/functvs" target="_blank">https://github.com/shimon-d/functvs</a>

## How to contribute

1. Fork the dir 
2. Create a branch in the like fashion: pl-2023-user.name-playbook.number (regex: ^pl-2023-[a-zA-Z0-9]+\.[a-zA-Z0-9]+-playbook\.[0-9]+$)
3. Do the appropriate changes according to the Playbook
4. Run the black configuration set on the pyproject.toml
5. PR and wait for the review and comment
6. If any fixes are required fix them, go back to step 2. Otherwise, move onto the next contrib quest

## Installation
```shell
$ pip install Functvs
---> 100%
```

## Dependencies


## Code example
```python
from functvs import Subfactorial

print(Subfactorial.euler(5))


>>> 44
``` 
