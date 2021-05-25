# Document Distance
1. Split each document into words
2. count word frequencies
3. compute dot product and normalize
4. get angle
    - 0 degree: identical
    - 90 degree: no common words

<br/>
<br/>

### difference between original(python2) and python3

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
