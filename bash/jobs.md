# Jobs

Use `jobs`, `bg` and `fg` to manage jobs. This is usefull to make processes running without blocking the terminal.

## Job suspension

In order to suspend a running process, just use `CTRL+Z` combination on the terminal which is running the process.

```bash command-line
sleep 5m
^Z
[2]  + 8627 suspended  sleep 5m
```

The suspended jobs are listed using `jobs` command.

```bash command-line
jobs
[1]  + suspended  sleep 5m
```

## Resume jobs

Once a job is suspended, we can use `fg` to resume the process in foreground or `bg` to resume it in background, specifying the job number after `%` char.

```bash command-line
fg %1 # resume "sleep" in foreground
# OR
bg %1 # resume "sleep" in background
```

## Running process in background

Any process can be run in background just adding `&` at the end of the line.

```bash command-line
sleep 5m &
[1] 9117
jobs
[1]  + running    sleep 5m
```

### Use case

The best use case that popped out in mind is the `rm -r node_modules` command that can takes minutes to be performed. Just use

```bash
for i in `find . -name "node_modules" -type d -prune`; do rm -r $i &; done
```

to **concurrently** remove all the `node_modules` folders in a folder tree.

[Source](https://www.youtube.com/watch?v=LfC6pv8VISk&t=541s)
