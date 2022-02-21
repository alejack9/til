# Glass Effect

In order to make a `div` look like made of glass, just apply the `blur` effect in combination with a specific background color.

```css
.content {
  background-color: #ffffff10;
  backdrop-filter: blur(12px);
}
```

`backdrop-filter` has the same effect as the `filter` property, except the filter effects are applied only to the background and instead of to the element's content.

**Going beyond**: `backdrop-filter` has multiple other filters:

* blur
* brightness
* contrast
* drop-shadow
* grayscale
* hue-rotate
* invert
* opacity
* saturate
* sepia
* url – (for applying SVG filters)

[Example](./glass-effect.html)

[Source](https://www.instagram.com/p/CZucmvvPJc3/)
