# Single Watchtower run

Instead of keeping a `Watchtower` container, it is possible to run the containers upgrade checks manually using

```bash
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --run-once
```

[Source](https://containrrr.dev/watchtower/arguments/)
