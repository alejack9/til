# Last Command and Last Argument

Using `!!` and `!$` we can access to the last submitted command and argument, respectively.

```sh
~$ cat test.txt
cat: t: Permission denied
~$ sudo !!
Hello World!
~$ mkdir test
~$ cd !$
~/test$ 
```

[Source (with other cues)](https://code.tutsplus.com/articles/10-terminal-commands-that-will-boost-your-productivity--net-14105)
