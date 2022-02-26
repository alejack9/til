# Default Values

Using `:-` operator we can give a default value if the variable is not set.

```bash
name="Good morning!"
echo ${name}                # Good morning!
echo ${name1:-Hello World!} # Hello World!
```

It is usefull in facing optional input arguments.

```bash
echo "Hello ${1:-user}!"
```

[Source](https://stackoverflow.com/a/9333006)
