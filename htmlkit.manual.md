<<<<<<< HEAD
# htmlkit2 Python Module - User Guide

`htmlkit2` is a Python toolkit for generating valid HTML and CSS programmatically. It offers classes and functions for building complete web pages, tables, lists, and style declarations directly from your Python scripts.
=======
# htmlkit Python Module - User Guide

`htmlkit` is a Python toolkit for generating valid HTML and CSS programmatically. It offers classes and functions for building complete web pages, tables, lists, and style declarations directly from your Python scripts.
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e

---

## Getting Started

Import the module at the top of your script:
```python
<<<<<<< HEAD
import htmlkit2
=======
import htmlkit
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e
```

---

## Class Reference

### 1. HtmlPage

Create and manage the structure and contents of a full HTML page.

#### Initialization
```python
<<<<<<< HEAD
page = htmlkit2.HtmlPage(title="My Page")
=======
page = htmlkit.HtmlPage(title="My Page")
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e
# The title argument is optional. Default is "title"
```

#### Core Methods

- **page.page()**  
  Returns the fully composed HTML page as a string.
  ```python
  html_str = page.page()
  ```

- **page.save(filename)**  
  Writes the HTML page to a file.
  ```python
  page.save("index.html")
  ```

- **page.set_title(title)**  
  Sets or replaces the `<title>` of the page.
  ```python
  page.set_title("Welcome!")
  ```

- **page.set_style(css, mode='internal')**  
  Adds a CSS file to the `<head>` section.
    - `mode="external"`: Links the file with `<link>`
    - `mode="internal"`: Embeds contents in a `<style>` element

  ```python
  page.set_style("mystyle.css", "external")
  page.set_style("inline.css")  # embedded by default
  ```

- **page.add_style(css_text)**  
  Adds the given CSS as an internal `<style>` block.
  ```python
  page.add_style("body { background: lightblue; }")
  ```

- **page.append_body(html)**  
  Appends HTML content to the end of `<body>`.
  ```python
  page.append_body("<h1>Hello</h1>")
  ```

- **page.set_body(html_list)**  
  Replaces all `<body>` content with `html_list` (a list of HTML/text).
  ```python
  page.set_body(["<h2>Start Here</h2>", "<p>Welcome!</p>"])
  ```

---

### 2. ItemList

Create HTML ordered (`<ol>`) or unordered (`<ul>`) lists.

#### Initialization
```python
<<<<<<< HEAD
mylist = htmlkit2.ItemList()
# For unordered lists (default).

mylist = htmlkit2.ItemList(startno=1)
=======
mylist = htmlkit.ItemList()
# For unordered lists (default).

mylist = htmlkit.ItemList(startno=1)
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e
# For ordered lists.
```

#### Methods

- **mylist.add_item(item)**  
  Adds an item to the end of the list.

- **mylist.add_list(list_of_items)**  
  Adds multiple items to the list from a Python list.

- **mylist.get_list()**  
  Returns the complete HTML `<ul>` or `<ol>` as a string.

- **mylist.get_body()**  
  Returns the list of items (not formatted as HTML).

#### Example
```python
<<<<<<< HEAD
shopping = htmlkit2.ItemList()
=======
shopping = htmlkit.ItemList()
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e
shopping.add_item("Milk")
shopping.add_item("Eggs")
print(shopping.get_list())
```

---

### 3. Table

Programmatically build HTML tables.

#### Initialization
```python
<<<<<<< HEAD
t = htmlkit2.Table()
=======
t = htmlkit.Table()
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e
```

#### Methods

- **t.add_head(header)**  
  Adds a column header.

- **t.add_row(list_of_cells)**  
  Adds a row (give a list for each row).

- **t.new_row(), t.add_cell(cell), t.end_row()**  
  Step-by-step row construction.

- **t.get_table()**  
  Returns the complete `<table>` HTML string.

- **t.set_class(classname)**  
  Set a CSS class for the table.

- **t.set_id(id_str)**  
  Set the HTML id for the table.

- **t.set_caption(caption)**  
  Add a caption to the table.

- **t.borderon() / t.borderoff()**  
  Show or hide table borders.

#### Example
```python
<<<<<<< HEAD
t = htmlkit2.Table()
=======
t = htmlkit.Table()
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e
t.add_head("Name")
t.add_head("Score")
t.add_row(["Alice", "90"])
t.add_row(["Bob", "85"])
print(t.get_table())
```

---

### 4. Element

Create arbitrary HTML tags, optionally with a class attribute.

#### Usage
```python
<<<<<<< HEAD
el = htmlkit2.Element("span", "highlight")
=======
el = htmlkit.Element("span", "highlight")
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e
print(el.tag("Important text"))
# <span class="highlight">Important text</span>
```

---

### 5. AutoID

Generate unique sequential IDs or class names for HTML elements.

#### Usage
```python
<<<<<<< HEAD
auto = htmlkit2.AutoID(prefix="item", startvalue=1)
=======
auto = htmlkit.AutoID(prefix="item", startvalue=1)
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e
print(auto.auto())  # item1
print(auto.auto())  # item2
auto.reset()        # back to item1
```

---

## HTML Helper Functions

| Function | Example | Output |
|----------|---------|--------|
<<<<<<< HEAD
| **tag(tagname, text)** | `htmlkit2.tag("p", "Hello")` | `<p>Hello</p>` |
| **heading(level, text, idno="")** | `htmlkit2.heading(2, "Subtitle")` | `<h2>Subtitle</h2>` |
| **link(url, text)** | `htmlkit2.link("https://python.org", "Python")` | `<a href="https://python.org">Python</a>` |
| **image(src, alt="")** | `htmlkit2.image("cat.jpg", "A cat")` | `<img src="cat.jpg" alt="A cat">` |
| **comment(text)** | `htmlkit2.comment("note")` | `<!-- note -->` |
| **commentblock(text)** | `htmlkit2.commentblock("line 1\nline 2")` | <!-- <br>line 1<br>line 2<br>--> |
| **hr()** | `htmlkit2.hr()` | `<hr>` |
| **safetext(text)** | `htmlkit2.safetext("a < b & c > d")` | `a &lt; b &amp; c &gt; d` |
=======
| **tag(tagname, text)** | `htmlkit.tag("p", "Hello")` | `<p>Hello</p>` |
| **heading(level, text, idno="")** | `htmlkit.heading(2, "Subtitle")` | `<h2>Subtitle</h2>` |
| **link(url, text)** | `htmlkit.link("https://python.org", "Python")` | `<a href="https://python.org">Python</a>` |
| **image(src, alt="")** | `htmlkit.image("cat.jpg", "A cat")` | `<img src="cat.jpg" alt="A cat">` |
| **comment(text)** | `htmlkit.comment("note")` | `<!-- note -->` |
| **commentblock(text)** | `htmlkit.commentblock("line 1\nline 2")` | <!-- <br>line 1<br>line 2<br>--> |
| **hr()** | `htmlkit.hr()` | `<hr>` |
| **safetext(text)** | `htmlkit.safetext("a < b & c > d")` | `a &lt; b &amp; c &gt; d` |
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e

---

## CSS Helper Functions

| Function | Example | Output |
|----------|---------|--------|
<<<<<<< HEAD
| **style(selector, *props)** | `htmlkit2.style("p", "font-size:16px", "color:blue")` | `p{font-size:16px; color:blue;}` |
| **ink(color)** | `htmlkit2.ink("red")` | `color:red;` |
| **paper(color)** | `htmlkit2.paper("white")` | `background-color:white;` |
| **italic()** | `htmlkit2.italic()` | `font-style: italic;` |
| **bold()** | `htmlkit2.bold()` | `font-weight: bold;` |
| **smallcaps()** | `htmlkit2.smallcaps()` | `font-variant: small-caps;` |
=======
| **style(selector, *props)** | `htmlkit.style("p", "font-size:16px", "color:blue")` | `p{font-size:16px; color:blue;}` |
| **ink(color)** | `htmlkit.ink("red")` | `color:red;` |
| **paper(color)** | `htmlkit.paper("white")` | `background-color:white;` |
| **italic()** | `htmlkit.italic()` | `font-style: italic;` |
| **bold()** | `htmlkit.bold()` | `font-weight: bold;` |
| **smallcaps()** | `htmlkit.smallcaps()` | `font-variant: small-caps;` |
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e

---

## Complete Example

```python
<<<<<<< HEAD
import htmlkit2

# Create a web page
page = htmlkit2.HtmlPage("Sample Page")
=======
import htmlkit

# Create a web page
page = htmlkit.HtmlPage("Sample Page")
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e
page.add_style("body { font-family: sans-serif; }")
page.append_body(htmlkit.heading(1, "Welcome!"))

fruits = htmlkit.ItemList()
fruits.add_list(["Apple", "Banana", "Cherry"])
page.append_body(fruits.get_list())

table = htmlkit.Table()
table.add_head("Name")
table.add_head("Score")
table.add_row(["Alice", "92"])
table.add_row(["Bob", "88"])
page.append_body(table.get_table())

page.save("sample.html")
```

---

## Summary
<<<<<<< HEAD
=======

- **HtmlPage:** Generate and output entire HTML documents.
- **ItemList:** Easily build `<ul>` and `<ol>` lists.
- **Table:** Programmatically build tables.
- **Element:** Custom tag or span/div element creator.
- **AutoID:** Automatic numbering for element IDs/classes.
- **Helper functions:** Tags, links, headings, comments, images, safe text, and CSS.
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e

- **HtmlPage:** Generate and output entire HTML documents.
- **ItemList:** Easily build `<ul>` and `<ol>` lists.
- **Table:** Programmatically build tables.
- **Element:** Custom tag or span/div element creator.
- **AutoID:** Automatic numbering for element IDs/classes.
- **Helper functions:** Tags, links, headings, comments, images, safe text, and CSS.

<<<<<<< HEAD
htmlkit2 lets you automate and script the authoring of HTML/CSS for web pages, reports, and custom output—entirely from Python!

=======
>>>>>>> 20b7df9ada3078f6ee1d412a561f86c1994fba2e
---

For more details, examples, or troubleshooting, consult the in-code comments or contact the project maintainer.
