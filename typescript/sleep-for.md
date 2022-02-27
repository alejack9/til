# Sleep-for

In order to make program wait (or sleep) for a certain amount of time we can use a one-liner that returns a `Promise` after a certain amount of time.

```typescript
const sleepFor = (ms: number): Promise<void> => new Promise((resolve) => setTimeout(resolve, ms));
```

[Source](https://expertcodeblog.wordpress.com/2018/07/05/typescript-sleep-a-thread/)
