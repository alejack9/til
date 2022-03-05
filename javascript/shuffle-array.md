# Shuffle an Array

The faster way to shuffle an array is to randomly sort it.

```javascript
const shuffle = (a, inPlace = true) => (inPlace ? a : [...a]).sort(() => 0.5 - Math.random());
```

However, this approch does not have a uniform distribution since the black-box nature of the `sort` function (take a look at [this](https://javascript.info/array-methods#shuffle-an-array) for more).

[Source](https://dev.to/codebubb/how-to-shuffle-an-array-in-javascript-2ikj)

## Workaround

### Fisher-Yates algorithm

Take each element in reverse order and swap it with a randomly element preceding it.

```javascript
const fisherYates = array => {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]]
  }
}
```
