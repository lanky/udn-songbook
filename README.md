# udn-songbook
A class-based abstraction of a songbook, using the ukedown rendering engine

# requirements
  * ukedown (markdown extensions)
  * python-fretboard (chord generation)
  * weasyprint (pdf generation)

# basic usage
(it only does basic things at the moment)

```python
from ukebook.song import Song
s = song('/path/to/filename')
```
