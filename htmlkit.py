"""web page html and css utils"""

class htmlpage:
	"""class to create html web pages"""
	doctype = "<!DOCTYPE html>"
	def __init__(self,title="title"):
		"""creates now html page. optional title parameter can be specified"""
		self.title = title
		self.head = []
		self.style_external = []
		self.style_internal = []
		self.body = []
		
	def set_title(self,title):
		"""set title tag in document head"""
		self.title = title

	def set_style(self,mode = "internal" ,css=""):
		"""specifies css file and mode
		"external" mode links to css file
		"internal" (default) mode copies css file contents into <style></style> tag in document head"""
		
		
			
		if css != "":
			if mode == "external":
				#self.style.append('<link rel="stylesheet" href="{}">'.format(css))
				self.style_external.append('<link rel="stylesheet" href="{}">'.format(css))
			else:
				cssfile = open(css,"r")
				csstext = cssfile.read()
				cssfile.close()
				#self.style_internal.append("<style>")
				self.style_internal.append(csstext)
				#self.style._internal.append("</style>")
		else:
			pass
	
	def add_style(self,text):
		self.style_internal.append(text)

	
		
	def page(self):
		"""returns full html page"""
		pagetext = []
		pagetext.append(self.doctype)
		pagetext.append("<html>\n<head>")
		pagetext.append("<title>" + self.title + "</title>")
		pagetext.append(comment("style here"))
		#pagetext.append(comment(self.body[0]))
		if len(self.style_external) > 0:
		
		#if	self.style[0].startswith("<link"):
			pagetext.extend(self.style_external)
		#else:
		if len(self.style_internal) > 0:
			pagetext.append("<style>")
			pagetext.extend(self.style_internal)
			pagetext.append("</style>")
		
		pagetext.append("</head>\n<body>")
		pagetext.extend(self.body)
		pagetext.append("</body></html>")
		return "\n".join(pagetext)
	def set_body(self,textblock):
		self.body = textblock
	def append_body(self,text):
		"""adds text to end of html body"""
		self.body.append(text)	
	def save(self,filename):
		"""writes page html to file"""
		fileout = open(filename,"w")
		fileout.write(self.page())
		fileout.close()
		
	
class itemlist:
	"""class for html ordered or unordered list"""
	def __init__(self,startno=""):
		"""creates new list in html. default is unordered. specify starting parameter for ordered list"""
		self.body = []
		if startno == "":
			self.tag = "ul"
		else:
			self.tag = "ol"	
	def get_list(self):
		"""return entire html list"""
		listtext = []
		listtext.append(f"<{self.tag}>")
		listtext.extend(self.body)
		listtext.append(f"</{self.tag}>")
		return ("\n".join(listtext))
	def get_body(self):
		return(self.body)
	def add_item(self,text):
		self.body.append("<li>" + text + "</li>")
	def add_list(self,list):
		"""add entire list to html list"""
		for item in list:
			self.body.append("<li>" + item + "</li>")

class table:
	"""class to create simple html tables"""
	def __init__(self):
		self.heads = []
		self.body = []
		self.currentrow = []
		self.classname = ""
		self.id = ""
		self.border = True
		self.caption = ""
	def set_class(self,classname):
		self.classname = classname
	def set_caption(self,caption):
		self.caption = caption
	def set_id(self,id):
		self.id = id
	def borderon(self):
		self.border = True
	def borderoff(self):
		self.border = False
	def add_row(self,text):
		"""add row of items to table. text will be treated as a list"""
		self.body.append(text)
	def new_row(self):
		"""starts new table row. add items with add_cell. complete with end_row"""
		self.currentrow = []
	def add_cell(self,text):
		"""adds cell (table data) to row. new_row should be called first"""
		self.currentrow.append(text)
	def end_row(self):
		"""adds row to table. row should be started with new_row and populated with add_cell. row will be lost if this method is not called"""
		self.body.append(self.currentrow)
	def add_head(self,text):
		"""adds table column heading (table head) to table"""
		self.heads.append(text)
	def get_table(self):
		"""returns complete html table code"""
		tabletext = []
		#opening tag
		opentag = "<table"
		if self.classname != "":
			opentag += f' class="{self.classname}"'
		if self.id != "":
			opentag += f' id="{self.id}"'
		if self.border:
			opentag +=  ' border="1" cellspacing="0"'
		tabletext.append(opentag + '>')
		
		if self.caption != "":
			tabletext.append(f"<caption>{self.caption}</caption>")
		
		#tabletext.extend(self.body)
		if len(self.heads) > 0:
			tabletext.append("<tr>")
			for cell in self.heads:
				tabletext.append("<th>" + cell + "</th>")
			tabletext.append("</tr>")
		for row in self.body:
			tabletext.append("<tr>")
			for cell in row:
				tabletext.append("<td>" + cell + "</td>")
			tabletext.append("</tr>")	
		tabletext.append("</table>")
		return("\n".join(tabletext))
	
class element:
	"""class to define tags with attributes
	"""
	def __init__(self,tagname,classname=""):
		self.tagname = tagname
		self.classname = classname
		self.opentag = f'<{self.tagname}'
		if classname != "":
			self.opentag += f' class="{self.classname}"'
		self.closetag = f"</{self.tagname}>"
	
	def	tag(self,text):
		"""returns text enclosed in define tag"""
		return(f'{self.opentag}>{text}{self.closetag}')
	
def tag(tagname,text):
	"""function to return simple html tags
	returns <tagname>text</tagname>
	use element class with tag method for more advanced tag features
	"""
	return("<{0}>{1}</{0}>".format(tagname,text))
def heading(level,text,idno=""):
	"""returns heading text at specified heading level (1-6)
	optional id can be specified
	"""
	if idno != "":
		#id = ' id="id=' + idno + '"'
		id = f' id="id{idno}"'
	else:
		id = ""
	#return("<h{0}>{1}</h{0}>".format(level,text))
	#return("<h{0} id=\"{2}\">{1}</h{0}>".format(level,text,id))
	return(f'<h{level}>{text}</h{level}{id}>')

def link(url,text):
	return(f'<a href="{url}">{text}</a>')

def comment(text):
	"""returns text in comment"""
	return(f"<!-- {text} -->")
def commentblock(text):
	"""returns text as multi-line comment"""
	return(f"<!--\n{text}\n-->")
def hr():
	"""return horizontal rule tag"""
	return("<hr>")
def image(src,alt=""):
	"""return img tag from source url, optional alt paramete"""
	if alt == "":
		return(f'<img src="{src}">')
	else:
		return(f'<img src="{src}" alt="{alt}">')

#css functions
def style(selector,*args):
	"""returns selector{arg,arg,arg....}"""
	return(f"{selector}{{" + "; ".join(args) + ";}")

		
#quick / shortcut style functions
def ink(textcolour):
	"""return style declaration for text colour"""
	return(f"color:{textcolour};")
	
def paper(backgroundcolour):
	"""returns style declaration for background colour"""
	return(f"background-color:{backgroundcolour};")

def italic():
	"""shortcut returning 'font-style: italic;'"""
	return("font-style: italic;")

def bold():
	"""shortcut function returning 'font-weight: bold;'"""
	return("font-weight: bold;")
	
def smallcaps():
	"""shortcut function returning 'font-variant: small-caps;'"""
	return("font-variant: small-caps;")


### MAIN ####
def main():
	pass
	print("running as program rather than module")
	print("end")
	
if __name__ == "__main__":
	main()