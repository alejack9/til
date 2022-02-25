# Head and Tail

Using `[head, ...tail]` we can split an array keeping the first element in `head` and the rest of the elements in tail.

```javascript
const str = "this is a test";
const [head, tail] = str.split(' ');
console.log(head); // "this"
console.log(tail); // [ "is", "a", "test" ]
```
