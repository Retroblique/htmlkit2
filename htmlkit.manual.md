# htmlkit module usage manual

Python module for quick generation of basic html and css code.

## htmlpage class

### initialisation
webpage = htmllkit.htmlpage(title)

The title argument is optional and if omitted a default value of "title" will be used

Creates a the basic outline of a webpage in html5

At initialisation this will be:
```
<!DOCTYPE html>
<html>
<head>
<title>title</title>
<!-- style here -->
</head>
<body>
</body></html>
```

### page method
webpage.page()
return the text of the htmlpage object webpage

### save method
webpage.save(filename)

Saves the text of the htmlpage to textfile filename

### set_title method
webpage.set_title(titlename)
Sets the the title element to titlename. Replaces any previous title value


### set_style method
webpage.set_style(css,mode)
adds a css file to the htmlpage
css is the name of the style file
mode can be either "external" or "internal". The default mode is "internal" if the parameter is omitted.

external mode adds a link tag into the head of the htmlpage

example
webpage.set_style("htmlkit.css","external")
will insert the line 
<link rel="stylesheet" href="htmlkit.css">

internal mode will copy the contents of the style file into the style element in the head of the htmlpage
example
webpage.set_style("htmlkit.css","internal")

will insert
```
<style>
/* content of htmlkit.css file */
</style>
```
Note - in either mode this method does not check that the contents of the css file is valid css code.

### add_style method
webpage.add_style(text)
inserts text into the style element in the head the htmlpage

Note - this method does not check that the text is valid css code


### append_body method
webpage.append_body(text)
append text to the body element of the html page at the end of any existing context

webpage.set_body(textblock)


class element

Defines html element tags, with option of specifying a class attribute. Particularly intended for span and div element. 

tagname = htmlkit.element(tagname,classname)
defines elements 

elementname.tag(text)

example
boldtext = htmlkit.element("strong")
boldtext.tag("Alpha")
will return
<strong>Alpha</strong>

italictext = htmlkit.element("span","italic")
italictext.tag("Beta")
will return
<span class="italic">Beta</span>

This similar but more flexible than the tag function






## itemlist class

list = htmlkit.itemlist()
create an empty ordered or unordered 

### list.get_list()
returns the text of the itenlist object

### list.add_item(text)
insert a new item into the itemlist

## table class 
creates html tables

table = htmlkit.table()
generated basic table

### get_table() method
returns the html text of the table object

example
t = htmlkit.table()
t.get_table()
returns
```
<table border="1" cellspacing="0">
</table>
```



## html functions

### comment function
htmlkit.comment(text)
returns text inside comment tags
example
htmlkit.comment("simple comment"))
returns
```
<!-- simple comment -->
```

htmlkit.commentblock(text)
returns text in multi-line comment
example
htmlkit.commentblock("not so\nsimple comment")
```
<!--
not so
simple comment
-->
```

### tag function
htmlkit.tag(tagname,text)
returns text as an element surrounded by tagname tag
example
tag("p","paragraph text")
returns
<p>paragraph text</p>


### link function
htmlkit.link(src,text)
creates a hyperlink

example
htmlkit.link<"https://apod.nasa.gov/apod/astropix.html","APOD")
returns
<a href="https://apod.nasa.gov/apod/astropix.html">APOD</a>

### image function
htmlkit.image(src,alt)

### safetext function
htmlkit.safetext(text)
Replaces & > < characters in text with entity codes

example
htmlkit.safetext("a-b-c-d-e-f-g-<-&->")
returns 

## css functions

### style function
htmlkit.style(selector,*properties)

### ink function
htmlkit.ink(textcolour)
returns style declaration to set text colour to textcolur

example
htmlkit.ink("red")
returns
{color:red);

### paper function
htmlkit.paper(backgroundcolour)
returns style declaration to return background colour to backgroundcolour

example
htmlkit.paper("white")
returns
{background-color:white};
 
 