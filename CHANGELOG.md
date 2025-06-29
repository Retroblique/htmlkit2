# Changelog

All notable changes to this project are documented in this file.

This format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.1.0] - 2025-06-23

### Added
- **Enhanced `<head>` Management**: Users can now add arbitrary elements to the `<head>`, such as `<meta>`, `<script>`, or custom tags, using the `add_to_head` method.

### Improved
- **File Handling Robustness**: Introduced checks to ensure files exist before attempting to open them, along with more graceful handling of file-related exceptions.
- **Safe Write Operations**: Enhanced `save` method with user-friendly error handling during file write operations. 

---

## [1.0.0] - 2025-06-18

### Added
- Modernized Python class names to CamelCase (e.g., `HtmlPage`, `ItemList`, `Table`, etc.)
- Comprehensive code cleanup: improved code formatting, indentation, and consistent naming conventions.
- Safer file handling using context managers (`with open(...) as ...`)
- Clarifying and detailed code comments for all classes, methods, and functions.
- New, rich documentation including `htmlkit.manual.md` and a complete, example-focused `README.md`.
- Backwards compatibility aliases for all original lowercase class and function names (`htmlpage`, `itemlist`, etc.), allowing legacy code to continue working unchanged.

### Changed
- Refactored core classes and functions for improved safety, maintainability, and readability.
- Standardized documentation style in both code and manuals.
- Clear public API for legacy (lowercase) and modern (CamelCase) usage.

### Fixed
- Minor issues in file I/O handling.
- Spelling, formatting, and ambiguous documentation in both the code and markdown manuals.

---

## Credits
- Forked from the original [htmlkit](https://github.com/adclawrence/htmlkit) by Andrew Lawrence [adclawrence](https://github.com/adclawrence).