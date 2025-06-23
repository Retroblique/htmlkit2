import htmlkit2 as htmlkit

def demo_html_features():
    # Create the HtmlPage instance
    page = htmlkit.HtmlPage("Feature Showcase")

    # Link the external CSS file
    page.set_style("mvp.css", mode="external")

    # Demonstrate various features
    page.append_body(htmlkit.comment("Page built with htmlkit"))
    page.append_body(htmlkit.heading(1, "htmlkit Demo Page"))
    page.append_body(htmlkit.hr())

    unsafe_text = '5 < 10 & 10 > 5, "Quotes" & \'apostrophes\' safe?'
    page.append_body(htmlkit.tag("p", "Escaped output: " + htmlkit.safetext(unsafe_text)))

    # Add items to demonstrate the list feature
    fruits_list = htmlkit.ItemList()
    fruits_list.add_list(["Apple", "Banana", "Cherry"])
    page.append_body(htmlkit.heading(2, "Fruit List"))
    page.append_body(fruits_list.get_list())

    steps = htmlkit.ItemList(startno=1)
    steps.add_list(["Install Python", "Install htmlkit", "Write some code!"])
    page.append_body(htmlkit.heading(2, "Getting Started Steps"))
    page.append_body(steps.get_list())

    # Add a demo table
    table = htmlkit.Table()
    table.set_class("demo-class")
    table.set_id("main-table")
    table.set_caption("Sample Data Table")
    table.add_head("User")
    table.add_head("Score")
    table.add_row(["Alice", "95"])
    table.add_row(["Bob", "89"])
    table.end_row()

    page.append_body(htmlkit.heading(2, "Demo Table"))
    page.append_body(table.get_table())

    # Save the page
    page.save("feature_showcase.html")
    print("feature_showcase.html with mvp.css has been created.")

def main():
    demo_html_features()
    # Other tests like head management, CSS handling, etc.
    # test_head_management()
    # test_css_file_handling()
    # test_html_file_writing()

if __name__ == "__main__":
    main()