# htmlkit2

**htmlkit2** is a lightweight Python toolkit for generating HTML and CSS programmatically. This project is a backwards-compatible fork of the original [htmlkit](https://github.com/adclawrence/htmlkit) by Andrew Lawrence ([adclawrence](https://github.com/adclawrence)), updated with modern Python conventions, improved safety, and enhanced documentation—while preserving support for legacy code.

---

## Features

- **Build complete HTML pages** with customizable head, style, and body sections
- **Generate HTML tables**, ordered/unordered lists, and arbitrary elements
- **Create links, images, comments, and headings** quickly and safely
- **Safely escape HTML** for direct text insertion
- **Automate ID/class naming** for dynamic elements and styling
- **Produce CSS rules** and reusable style declarations with ease
- **Backwards compatible**—all original lowercase class and function names remain supported

---

## Installation

Simply copy or clone `htmlkit.py` into your project folder.  
No external dependencies are required (built on Python’s standard library).

---

## Quick Example

```python
import htmlkit2 as htmlkit

# Create a new HTML page
page = htmlkit.HtmlPage("Demo Page")
page.add_style("body { font-family: sans-serif; }")
page.append_body(htmlkit.heading(1, "Welcome!"))

# Add a list
fruits = htmlkit.ItemList()
fruits.add_list(["Apple", "Banana", "Cherry"])
page.append_body(fruits.get_list())

# Add a data table
table = htmlkit.Table()
table.add_head("Name")
table.add_head("Score")
table.add_row(["Alice", "92"])
table.add_row(["Bob", "88"])
page.append_body(table.get_table())

# Save the page to a file
page.save("demo.html")
```

---

## Documentation

A full user manual is available in [htmlkit.manual.md](./htmlkit.manual.md), with API details and usage recipes.  
See the many inline comments in `htmlkit.py` for additional guidance.

Core components include:

- **HtmlPage** — HTML page structure and manipulation
- **ItemList** — Ordered and unordered lists
- **Table** — HTML table creation
- **Element** — Custom element/tag building
- **AutoID** — Automatic ID/class string generation
- **Helper functions** — Tags, links, images, headings, comments, safe text, CSS style builders

---

## Compatibility

- Python 3 (standard library only)
- Fully backwards compatible: legacy code using original lowercase class and function names (e.g., `htmlkit.htmlpage`, `htmlkit.table`) will continue to work

---

## Contributing

Contributions, bug reports, and feature requests are welcome!
Please use [Issues](https://github.com/your-repo/issues) or submit a Pull Request.

---

## License

[MIT License](LICENSE)

---

## Credits

- Original htmlkit author: Andrew Lawrence ([adclawrence](https://github.com/adclawrence))
- This fork: Maintained by Mark Stevens

---

**htmlkit**: Programmatic HTML and CSS, the Python way—improved, modernized, and backwards compatible.

---

*Tip: For in-depth usage and examples, see [htmlkit.manual.md](./htmlkit.manual.md).*
