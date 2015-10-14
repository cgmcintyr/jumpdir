# Jumpdir

A minimal command line utility for quickly jumping to different directories within your home directory.

## Installation

Simply

```bash
pip install jumpdir
```

Then add the following to your .bashrc

```bash
function jd {
  TARGET="$(jumpdir $@)"
  
  if [ $TARGET != "None" ]
    then
      cd $TARGET
    else
      echo "Jumpdir could not find a matching directory :("
  fi
}
```

## Useage

Jumpdir is case insensitive and searches through your home folder for directories whose names directly match the provided search term. It will return the path to the first matching directory, so dealing with duplicate directories can be irksome.

For example, using the following example home directory:

```
.
|-- Devel/
|   |-- python/
|   |   '-- script.py
|   |-- django/
|       '-- somesite/
|           '-- nothinghere.jpg
|-- Downloads/
|   |-- eastclintwood.jpg
|   '-- yup.mp3
|-- Other/
    '-- python/
        '-- duplicate testing
```

Using jumpdir with the jd function works as follows:

```shell
~ $ jd devel
~/Devel $ jd DOWNLOADS
~/Downloads $ jd django
~/Devel/django $ jd othe
Jumpdir could not find a matching directory :(
~/Devel/django $ jd python
~/Devel/python $ # jumpdir will choose the first directory it matches
```
