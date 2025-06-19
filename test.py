# test.py
# Demonstrates the use of all major features of htmlkit.

import htmlkit2 as htmlkit

# --- Create and style the page ---
page = htmlkit.HtmlPage("htmlkit Test & Feature Showcase")
page.set_style("test_styles.css", mode="external")  # For demo, assume the file exists or handle gracefully
page.add_style("""
h1 { color: steelblue; }
ul { margin-top: 0; }
.demo-class { background: #eef; padding: 10px; margin-bottom: 10px; }
""")

# --- Add a heading and a comment ---
page.append_body(htmlkit.comment("Page built with htmlkit"))
page.append_body(htmlkit.heading(1, "htmlkit Demo Page"))
page.append_body(htmlkit.hr())

# --- Add a paragraph with safetext ---
unsafe_text = '5 < 10 & 10 > 5, "Quotes" & \'apostrophes\' safe?'
page.append_body(htmlkit.tag("p", "Escaped output: " + htmlkit.safetext(unsafe_text)))

# --- Add a bulleted list ---
fruits_list = htmlkit.ItemList()
fruits_list.add_list(["Apple", "Banana", "Cherry"])
page.append_body(htmlkit.heading(2, "Fruit List"))
page.append_body(fruits_list.get_list())

# --- Add an ordered list ---
steps = htmlkit.ItemList(startno=1)
steps.add_list(["Install Python", "Install htmlkit", "Write some code!"])
page.append_body(htmlkit.heading(2, "Getting Started Steps"))
page.append_body(steps.get_list())

# --- Add a table with header, rows, class, ID, caption ---
table = htmlkit.Table()
table.set_class("demo-class")
table.set_id("main-table")
table.set_caption("Sample Data Table")
table.add_head("User")
table.add_head("Score")

table.add_row(["Alice", "95"])
table.add_row(["Bob", "89"])
table.new_row()
table.add_cell("Charlie")
table.add_cell("88")
table.end_row()
page.append_body(htmlkit.heading(2, "Demo Table"))
page.append_body(table.get_table())

# --- Demonstrate quick style & css helpers ---
styled_text = htmlkit.tag("div", "Colorful text!", )
page.append_body(htmlkit.tag("p", "CSS style helper (red, blue bg, bold):"))
css_rule = htmlkit.style(".highlight", htmlkit.ink("red"), htmlkit.paper("#bde"), htmlkit.bold())
page.add_style(css_rule)
page.append_body(htmlkit.tag("span", "Styled span created with CSS helpers").replace("span", "span class=\"highlight\""))

# --- Demonstrate generic element ---
span = htmlkit.Element("span", "demo-class")
page.append_body(span.tag("This is in a custom <span> with a class."))

# --- Demonstrate autoid ---
auto = htmlkit.AutoID(prefix="example-id-", startvalue=101)
for i in range(3):
    page.append_body(htmlkit.tag("p", f"Auto-generated id: {auto.auto()}"))

# --- Demonstrate image and link ---
page.append_body(htmlkit.heading(2, "Image & Link"))
page.append_body(htmlkit.image("https://placekitten.com/200/200", alt="Cute kitten"))
page.append_body(htmlkit.tag("p", htmlkit.link("https://github.com/adclawrence/htmlkit", "Original htmlkit by Andrew Lawrence")))

# --- Demonstrate horizontal rule, comments, and block comments ---
page.append_body(htmlkit.hr())
page.append_body(htmlkit.commentblock("This is a multiline\nHTML comment block"))

# --- Save to file ---
page.save("test_output.html")
print("test_output.html has been created with all htmlkit features demonstrated.")