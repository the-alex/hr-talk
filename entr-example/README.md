`entr`
======

Hey, glad you read this.

## Getting started

Install those deps, my friend. If you're not running macOS, then you can
probably figure out how to install `entr` without me.

```bash
$ brew install entr
$ pwd
/Users/ac/development/repositories/hr-talk/entr-example
$ entr ls *.py | entr -c python fizzbuzz.py
```

