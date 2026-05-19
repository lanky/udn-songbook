<!-- markdownlint-disable MD013 MD033-->
<!-- vim: set tw=100 -->

# udn-songbook

## What'cha talkin' about, Willis?

`udn-songbook` is a class-based abstraction of a songbook, using the [ukedown](https://pypi.org/project/ukedown/) rendering engine.
Long-term it is intended to replace most of the code from the [`ukebook-md`](https://github.com/lanky/ukebook-md) tools.

It supports a number of different profiles (combinations of on/off flags really) and can produce
indexed PDF songbooks from a colleciton of files in ukedown format.

## Requirements

Python packages
* ukedown (markdown extensions)
* weasyprint (PDF generation)
* pychord (chord management)

## development requirements - for future project enhancements
* python-fretboard (chord generation)

## The TL;DR

How to use the current functionality

### Load a single songsheet and inspect it

```python
from udn_songbook import Song
s = song('/path/to/filename')

# list the unique chords in the song
s.chords

# save it to disk
s.save(outputfile)

# transpose by an arbitrary number of semitones
s.transpose(semitones)

# generate a PDF from the current song, using built-in templates
s.pdf()
```

### Build a book from a directory (or multiple directories) of UDN-format songsheets


```python
from udn_songbook import SongBook
mybook = SongBook(inputs=['directory1', 'directory2', 'someotherfile.udn'])
```

Songbooks have an index auto-generated, and do not support mutiple songs with the same ID (which is
essentially "Title - Artist").

If your inputs include multiple songs in this way, the last one imported will be used. So name them
carefully.

A Songbook in this context is a collection of song objects with additional metadata, such as an
index.

## Tools

The pip package also installs some commandline tools, aimed at managing individual songsheets:

`udn_transpose`, which allows in-place (or optionally to a new file) transposing of an existing
songsheet by an arbitrary number of semitones. The transposition is added to metadata

`udn_songsheet`, which renders a UDN songsheet to a file in either PDF (default) or HTML format. it
also supports in-place transposition, without affecting the original input file.

`udn_pdfbook` - build a songbook and render it as a PDF file.

## Profile and custom chord support

Profiles control the optional elements in song templates (chords, band notes, chord diagrams etc.)

A default set is defined in the `defaults.toml` file contained in this package. You can also pass
additional configuration files in `dynaconf` TOML format, or define/update your settings in your
`~/.config/udn_songbook/settings.toml` file


### Available profile settings

the "default" profile has all of these defined with comments:

```toml
[profile.default]
# show chord diagrams
diagrams = false
# show performance notes
notes = true
# show inline chords
chords = true
# show singer notes
singer_notes = true
# add writer credits to footer
credits = true
# show capo position to play in original key
capo = false
# which stylesheet applies
stylesheet = "portrait"
```

## Chord names and pychord

pychord is quite opinionated about its chord names (or "qualities") and will reject some fairly
common chord variations/voicings. You can define your own in your configuration file, also.

Here are the custom definitions in the default settings:

```toml
[chordtypes]
# define custom chord "types" here. A custom chord "quality" (as pychord calls them)
# is a list of numbered scale tones from a chromatic scale, starting at 0 for the root.
# these are semitones from root(0) upwards
# A standard major scale consits of these intervals: 0,2,4,5,7,9,11
# so 0, 4, 7, 8 is actually 1, 3, 5, b6 in scale tones.
# mapping the C major scale as an example:
# semitones: 0 1  2 3  4 5 6  7 8  9 10 11 12
# note:      C C# D Eb E F F# G G# A Bb B  C
# scale:     1    2    3 4    5    6    7  8
# A major chord (1, 3, 5 in scale tones) -> (0, 4, 7) in semitones
# and minor (1, b3, 5) -> (0, 3, 7) etc.
addb6 = [0, 4, 7, 8]
6sus2 = [0, 2, 7, 9]
7sus2 = [0, 2, 7, 10]
"add#11" = [0, 4, 7, 18]
```


## what you need to use this:

* a directory full of UDN-format files.
* templates:
  * index.html.j2
  * song.html.j2
* stylesheets (up to you, you can pass their names and location to the methods)
  * pdf.css
  * ukedown.css

The package has built-in templates, which use the MS Verdana font by default, so you'll want that,
or of course you can change the stylesheets accordingly.
