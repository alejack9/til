# Registers

Vim provides a set of registers where you can store data "copying" it for later usage. This allows you to store different pieces of text in different places and use them whenever necessary.

Every register is accessed using a double quote before its name. Each registry name is composed by a single character. For example, we can access the content that is in the register `r` with `"r`. In order to copy the selected text into the register `r`, we can type `"ry`. To paste the content of this register, the logic is the same: `"rp`.

We can also copy the content of a registry in insert mode by using `Ctrl+r + registry_name`. This will paste content into the current buffer.

But that's only scratching the surface! [Learn More!](https://www.brianstorti.com/vim-registers/)
