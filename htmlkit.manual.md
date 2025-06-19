htmlkit2 Python Module - User Guide
==================================

htmlkit2 is a Python toolkit for generating valid HTML and CSS programmatically. It offers classes and functions for building complete web pages, tables, lists, and style declarations directly from your Python scripts.

--------------------------------------------------------------------------------
Getting Started

Import the module at the top of your script:
    import htmlkit2

--------------------------------------------------------------------------------
Class Reference

1. HtmlPage
-----------
Create and manage the structure and contents of a full HTML page.

Initialization:
    page = htmlkit2.HtmlPage(title="My Page")
    # The title argument is optional. Default is "title".

Core Methods:
  - page.page()
      Returns the fully composed HTML page as a string.

  - page.save(filename)
      Writes the HTML page to a file.

  - page.set_title(title)
      Sets or replaces the <title> of the page.

  - page.set_style(css, mode='internal')
      Adds a CSS file to the <head> section.
      mode="external": Links the file with <link>.
      mode="internal": Embeds contents in a <style> element.

  - page.add_style(css_text)
      Adds the given CSS as an internal <style> block.

  - page.append_body(html)
      Appends HTML or text to the end of <body>.

  - page.set_body(html_list)
      Replaces all <body> content with html_list (a list of HTML/text).

--------------------------------------------------------------------------------

2. ItemList
-----------
Create HTML ordered (<ol>) or unordered (<ul>) lists.

Initialization:
    mylist = htmlkit2.ItemList()
    # For unordered lists (default).

    mylist = htmlkit2.ItemList(startno=1)
    # For ordered lists.

Methods:
  - mylist.add_item(item)
      Adds an item to the end of the list.

  - mylist.add_list(list_of_items)
      Adds multiple items to the list from a Python list.

  - mylist.get_list()
      Returns the complete HTML <ul> or <ol> as a string.

  - mylist.get_body()
      Returns the list of items (not formatted as HTML).

Example:
    shopping = htmlkit2.ItemList()
    shopping.add_item("Milk")
    shopping.add_item("Eggs")
    print(shopping.get_list())

--------------------------------------------------------------------------------

3. Table
--------
Programmatically build HTML tables.

Initialization:
    t = htmlkit2.Table()

Methods:
  - t.add_head(header)
      Adds a column header.

  - t.add_row(list_of_cells)
      Adds a row (give a list of cells).

  - t.new_row(); t.add_cell(cell); t.end_row()
      Step-by-step row construction.

  - t.get_table()
      Returns the complete <table> HTML string.

  - t.set_class(classname)
      Set a CSS class for the table.

  - t.set_id(id_str)
      Set the HTML id for the table.

  - t.set_caption(caption)
      Add a caption to the table.

  - t.borderon() / t.borderoff()
      Show or hide table borders.

Example:
    t = htmlkit2.Table()
    t.add_head("Name")
    t.add_head("Score")
    t.add_row(["Alice", "90"])
    t.add_row(["Bob", "85"])
    print(t.get_table())

--------------------------------------------------------------------------------

4. Element
----------
Create custom HTML tags, optionally with a class.

Usage:
    el = htmlkit2.Element("span", "highlight")
    print(el.tag("Important text"))
    # Result: <span class="highlight">Important text</span>

--------------------------------------------------------------------------------

5. AutoID
---------
Generate unique sequential IDs or class names for HTML elements.

Usage:
    auto = htmlkit2.AutoID(prefix="item", startvalue=1)
    print(auto.auto())  # item1
    print(auto.auto())  # item2
    auto.reset()        # back to item1

--------------------------------------------------------------------------------
HTML Helper Functions

- tag(tagname, text)
    Create an element: htmlkit2.tag("p", "Hello") → <p>Hello</p>

- heading(level, text, idno="")
    Create a header: htmlkit2.heading(2, "Subtitle") → <h2>Subtitle</h2>

- link(url, text)
    Create a link: htmlkit2.link("https://python.org", "Python") → <a href="https://python.org">Python</a>

- image(src, alt="")
    Image tag: htmlkit2.image("cat.jpg", "A cat") → <img src="cat.jpg" alt="A cat">

- comment(text)
    Single-line HTML comment: htmlkit2.comment("note") → <!-- note -->

- commentblock(text)
    Multi-line HTML comment: htmlkit2.commentblock("line 1\nline 2")

- hr()
    Horizontal rule: htmlkit2.hr() → <hr>

- safetext(text)
    Safely escape &, <, >: htmlkit2.safetext("a < b & c > d") → a &lt; b &amp; c &gt; d

--------------------------------------------------------------------------------
CSS Helper Functions

- style(selector, *props)
    Create a CSS rule: htmlkit2.style("p", "font-size:16px", "color:blue")
    → p{font-size:16px; color:blue;}

- ink(color)
    CSS for text color: htmlkit2.ink("red") → color:red;

- paper(color)
    CSS for background color: htmlkit2.paper("white") → background-color:white;

- italic()
    CSS for italics: htmlkit2.italic() → font-style: italic;

- bold()
    CSS for bold: htmlkit2.bold() → font-weight: bold;

- smallcaps()
    CSS for small-caps: htmlkit2.smallcaps() → font-variant: small-caps;

--------------------------------------------------------------------------------
Complete Example

import htmlkit

page = htmlkit2.HtmlPage("Sample Page")
page.add_style("body { font-family: sans-serif; }")
page.append_body(htmlkit2.heading(1, "Welcome!"))

fruits = htmlkit2.ItemList()
fruits.add_list(["Apple", "Banana", "Cherry"])
page.append_body(fruits.get_list())

table = htmlkit2.Table()
table.add_head("Name")
table.add_head("Score")
table.add_row(["Alice", "92"])
table.add_row(["Bob", "88"])
page.append_body(table.get_table())

page.save("sample.html")

--------------------------------------------------------------------------------
Summary

- HtmlPage: Generate and output entire HTML documents.
- ItemList: Easily build <ul>/<ol> lists.
- Table: Programmatically build tables.
- Element: Custom tag or span/div element creator.
- AutoID: Automatic numbering for element IDs/classes.
- Helper functions: tags, links, headings, comments, images, safe text, and CSS.

htmlkit lets you automate and script the authoring of HTML/CSS for web pages, reports, and custom output—entirely from Python!

--------------------------------------------------------------------------------
For more details, example usage, or troubleshooting, consult the in-code comments or contact the project maintainer.
