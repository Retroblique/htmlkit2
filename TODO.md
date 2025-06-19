# htmlkit Development Roadmap

This roadmap highlights both planned improvements and new features for htmlkit.py, broken down into **Major** and **Minor** categories and listed in a recommended order of implementation.

---

## Major Improvements & Features

1. **File Handling Robustness** *(Improvement)*
   - Ensure all file operations (open/read/write) check that files exist and handle missing file errors gracefully.
2. **Safe Write Operations** *(Improvement)*
   - Protect all file write operations with try/except blocks to catch permission or disk errors, and provide clear error messages to users.
3. **Enhanced `<head>` Element Management** *(Improvement)*
   - Expand the `HtmlPage` class to let users add arbitrary elements to the `<head>`, including meta tags, scripts, favicons, etc.
4. **Support for Arbitrary Element Attributes** *(Improvement)*
   - Allow adding any valid attribute (e.g., `data-*`, `aria-*`, event handlers) when generating HTML tags via `Element`, `tag`, or similar functions/classes.
5. **HTML Forms Builder** *(New Feature)*
   - Build helper classes/functions for generating HTML forms, including fields, labels, validation, and form attribute management.

---

## Minor Improvements & Features

1. **Expanded safetext/webtext Functionality** *(Improvement)*
   - Make `safetext` (or a new `webtext`) escape more HTML entities (e.g., single and double quotes) for general web safety and form inputs.
2. **CSS Semicolon Auto-handling** *(Improvement)*
   - Update CSS helper functions so users don’t need to manually manage trailing semicolons.
3. **Quick Style Functions Enhancements** *(Improvement)*
   - Allow for composition and chaining/combo of quick style functions (e.g., combine bold+italic+color in one call).
4. **Combined Ink and Paper Color Helper** *(New Feature)*
   - Add a helper that returns a string with both foreground and background color CSS properties in one call.
5. **Save Stylesheet to File** *(New Feature)*
   - Provide a function or method to write assembled CSS to an external `.css` file, not just inline in HTML.
6. **ID Autonumbering Refinement** *(Improvement)*
   - Improve `AutoID` to ensure thread safety, predictable incrementation, and easier, more flexible usage in HTML generation.

---

## Future/Possible Features

- **Templates/Component System (Major New Feature)**
  - Support reusable blocks/components (e.g., cards, navbars) to reduce boilerplate.

- **Built-in Minification (Minor New Feature)**
  - Option to minify generated HTML or CSS for smaller file sizes in production.

---
*Help the project grow! Suggestions and PRs are welcome as we work toward a modern, robust, and user-friendly HTML/CSS toolkit for Python.*