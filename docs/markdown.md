# Markdown examples
Markdown is a loose collection of plain text standards, and there are many dialects of markdown. This is helpful for at the very least giving your code a useable `README.md` (e.g. the landing page for github repositories).

For help, see [https://www.markdownguide.org/](https://www.markdownguide.org/) and [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/).

Here we just demonstrate some of the most common features. Mkdocs uses the `pymdown` dialect for more advanced features.

## Note you can have sub-headings!
### And sub-sub-headings!
#### And sub-sub-subheadings!


## Other features
You can do lists:

1. Lorem
2. Ipsum
3. Lalala

---

(^note the line above^)

And code blocks with python highlighting!

```python
def f(x):
    return x**2
```

---

And format text:

1. *italicize*
2. **bold**
3. ***itali-bold***

---

Include and embed links: [github](www.github.com)

---

> A block quote! Lorem Ipsum
> > That even nests!

--- 

Lastly, latex is possible!

$$\int \Omega_i^5 d\Omega$$
