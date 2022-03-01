# Range

The faster way to make a `range` function similar to Python is

```javascript
const range = (f) => [...Array(f).keys()];

console.log(range(3));  // [ 0, 1, 2 ]
```

[Source](https://stackoverflow.com/questions/3895478/does-javascript-have-a-method-like-range-to-generate-a-range-within-the-supp)
