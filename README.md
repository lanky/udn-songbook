<!-- markdownlint-disable MD013 MD033-->
<!-- vim: set tw=100 -->

# udn-songbook
A class-based abstraction of a songbook, using the [ukedown](https://pypi.org/project/ukedown/) rendering engine

## requirements
* ukedown (markdown extensions)

## development requirements - for future project enhancements

* python-fretboard (chord generation)
* weasyprint (pdf generation)

## basic usage

(it only does basic things at the moment)

```python
from udn_songbook.song import Song
s = song('/path/to/filename')
```

And to generate a songbook, use the SongBook class, with a directory of UDN-format songsheets

```python
from udn_songbook.book import SongBook
mybook = SongBook(inputs=['directory1', 'directory2', 'someotherfile.udn'])
```

A Songbook in this context is a collection of song objects with additional metadata, such as an index.

## what you need to use this:

* a directory full of UDN-format files.
* templates:
  * index.html.j2
  * song.html.j2
* stylesheets (up to you, you can pass their names and location to the methods)
  * pdf.css
  * ukedown.css
