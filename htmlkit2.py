# HTML and CSS utilities for generating web pages programmatically.

import re
import os

class HtmlPage:
    # Represents and constructs an HTML web page.
    doctype = "<!DOCTYPE html>"

    def __init__(self, title="title"):
        # Initializes a new HTML page with an optional title.
        self.title = title
        self.head = []
        self.style_external = []
        self.style_internal = []
        self.body = []

    def set_title(self, title):
        # Sets the HTML document's <title>.
        self.title = title

    def set_style(self, css, mode="internal"):
        if css != "":
            if mode == "external":
                self.style_external.append(f'<link rel="stylesheet" href="{css}">')
            else:
                if os.path.exists(css):
                    try:
                        with open(css, "r") as cssfile:
                            csstext = cssfile.read()
                        self.style_internal.append(csstext)
                    except IOError:
                        print(f"Error: Could not read file {css}.")
                else:
                    print(f"Error: CSS file {css} does not exist.")

    def add_style(self, text):
        # Appends a given CSS text block to internal styles.
        self.style_internal.append(text)

    def page(self):
        # Builds and returns the complete HTML page as a string.
        pagetext = []
        pagetext.append(self.doctype)
        pagetext.append("<html>\n<head>")
        pagetext.append(f"<title>{self.title}</title>")
        pagetext.append(comment("style here"))

        if self.style_external:
            pagetext.extend(self.style_external)
        if self.style_internal:
            pagetext.append("<style>")
            pagetext.extend(self.style_internal)
            pagetext.append("</style>")

        pagetext.append("</head>\n<body>")
        pagetext.extend(self.body)
        pagetext.append("</body></html>")
        return "\n".join(pagetext)

    def set_body(self, textblock):
        # Sets the body content (takes a list of HTML strings).
        self.body = textblock

    def append_body(self, text):
        # Adds an HTML string to the end of the page body.
        self.body.append(text)

    def save(self, filename):
        try:
            with open(filename, "w") as fileout:
                fileout.write(self.page())
        except IOError:
            print(f"Error: Could not write to file {filename}.")


class ItemList:
    # Creates HTML ordered (<ol>) or unordered (<ul>) lists.
    def __init__(self, startno=""):
        # Initializes a list. Unordered by default; ordered if 'startno' is provided.
        self.body = []
        self.tag = "ul" if startno == "" else "ol"

    def get_list(self):
        # Returns the full HTML code for the list.
        listtext = [f"<{self.tag}>"]
        listtext.extend(self.body)
        listtext.append(f"</{self.tag}>")
        return "\n".join(listtext)

    def get_body(self):
        # Returns the raw list of items.
        return self.body

    def add_item(self, text):
        # Appends a single HTML list item.
        self.body.append(f"<li>{text}</li>")

    def add_list(self, items):
        # Appends multiple items (as a list of strings) to the list.
        for item in items:
            self.add_item(item)


class Table:
    # Builds simple HTML tables with headers and rows.
    def __init__(self):
        # Initializes a new table.
        self.heads = []
        self.body = []
        self.currentrow = []
        self.classname = ""
        self.id = ""
        self.border = True
        self.caption = ""

    def set_class(self, classname):
        # Sets a CSS class for the table.
        self.classname = classname

    def set_caption(self, caption):
        # Sets a caption for the table.
        self.caption = caption

    def set_id(self, id):
        # Sets the HTML id attribute for the table.
        self.id = id

    def borderon(self):
        # Enables a table border.
        self.border = True

    def borderoff(self):
        # Disables the table border.
        self.border = False

    def add_row(self, row):
        # Adds a full row to the table; expects a list of strings.
        self.body.append(row)

    def new_row(self):
        # Starts a new, empty table row.
        self.currentrow = []

    def add_cell(self, text):
        # Appends a cell to the current row.
        self.currentrow.append(text)

    def end_row(self):
        # Finalizes the current row and adds it to the table body.
        self.body.append(self.currentrow)

    def add_head(self, text):
        # Appends a header cell to the table.
        self.heads.append(text)

    def get_table(self):
        # Returns the complete HTML string for the table.
        tabletext = []
        opentag = "<table"
        if self.classname:
            opentag += f' class="{self.classname}"'
        if self.id:
            opentag += f' id="{self.id}"'
        if self.border:
            opentag += ' border="1" cellspacing="0"'
        tabletext.append(opentag + '>')

        if self.caption:
            tabletext.append(f"<caption>{self.caption}</caption>")

        if self.heads:
            tabletext.append("<tr>")
            for cell in self.heads:
                tabletext.append(f"<th>{cell}</th>")
            tabletext.append("</tr>")
        for row in self.body:
            tabletext.append("<tr>")
            for cell in row:
                tabletext.append(f"<td>{cell}</td>")
            tabletext.append("</tr>")
        tabletext.append("</table>")
        return "\n".join(tabletext)


class Element:
    # Represents a generic HTML tag with attributes.
    def __init__(self, tagname, classname=""):
        # Initializes a tag, optionally with a CSS class.
        self.tagname = tagname
        self.classname = classname
        self.opentag = f'<{self.tagname}'
        if classname:
            self.opentag += f' class="{classname}"'
        self.closetag = f"</{self.tagname}>"

    def tag(self, text):
        # Wraps the given text within the tag and its attributes.
        return f"{self.opentag}>{text}{self.closetag}"


def tag(tagname, text):
    # Returns a string wrapped in a specified HTML tag.
    return f"<{tagname}>{text}</{tagname}>"


def heading(level, text, idno=""):
    # Returns an HTML heading (h1-h6) with optional id.
    id_attr = f' id="id{idno}"' if idno else ""
    return f"<h{level}{id_attr}>{text}</h{level}>"


def link(url, text):
    # Returns an HTML anchor tag for a link.
    return f'<a href="{url}">{text}</a>'


def comment(text):
    # Returns a single-line HTML comment.
    return f"<!-- {text} -->"


def commentblock(text):
    # Returns a multi-line HTML comment.
    return f"<!--\n{text}\n-->"


def hr():
    # Returns an HTML horizontal rule.
    return "<hr>"


def image(src, alt=""):
    # Returns an HTML image tag with an optional alt text.
    if alt == "":
        return f'<img src="{src}">'
    else:
        return f'<img src="{src}" alt="{alt}">'


class AutoID:
    # Generates sequentially numbered IDs or classnames for HTML elements.
    def __init__(self, prefix="id", startvalue=1):
        # Initializes the counter with a prefix and starting number.
        self.prefix = prefix
        self.startvalue = startvalue
        self.counter = startvalue

    def id(self):
        # Returns the current ID value (does not increment).
        return f"{self.prefix}{self.counter}"

    def auto(self):
        # Returns the current ID value and increments the counter.
        new_id = f"{self.prefix}{self.counter}"
        self.counter += 1
        return new_id

    def reset(self):
        # Resets the counter to the initial value.
        self.counter = self.startvalue


def safetext(text):
    # Escapes &, <, and > characters to their HTML entity codes.
    entity = {"&": "&amp;", "<": "&lt;", ">": "&gt;"}
    entset = "".join(entity.keys())
    rx = re.compile(f"[{entset}]")
    result = rx.search(text)
    if result:
        textout = rx.sub(lambda x: entity[x.group(0)], text)
    else:
        textout = text
    return textout


def style(selector, *args):
    # Generates a CSS rule for a selector with the given properties.
    return f"{selector}{{" + "; ".join(args) + ";}}"


def ink(textcolour):
    # Returns a CSS color property for text color.
    return f"color:{textcolour};"


def paper(backgroundcolour):
    # Returns a CSS background-color property.
    return f"background-color:{backgroundcolour};"


def italic():
    # Returns a CSS declaration for italic text.
    return "font-style: italic;"


def bold():
    # Returns a CSS declaration for bold text.
    return "font-weight: bold;"


def smallcaps():
    # Returns a CSS declaration for small-caps font variant.
    return "font-variant: small-caps;"


def main():
    # Provides a placeholder for main program logic (runs if module executed directly).
    pass

# Backwards compatibility aliases for original class names
htmlpage = HtmlPage
itemlist = ItemList
table = Table
element = Element
autoid = AutoID

print("Well, we got there!")

if __name__ == "__main__":
    main()