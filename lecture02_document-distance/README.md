## difference between original(python2) and python3

### python2
```python
translation_table = string.maketrans(string.punctuation + string.uppercase,
                                     " "*len(string.punctuation) + string.lowercase)
```
### python3
```python
translation_table = str.maketrans(string.punctuation + string.ascii_uppercase,
                                  " " * len(string.punctuation) + string.ascii_lowercase)
```
