#web page html and css utils

class htmlpage:
	doctype = "<!DOCTYPE html>"
	def __init__(self,title="title"):
		self.title = title
		self.head = []
		self.style = []
		self.body = []
		
	def set_title(self,title):
		self.title = title
	
		
	def page(self):
		pagetext = []
		pagetext.append(self.doctype)
		pagetext.append("<html>\n<head>")
		pagetext.append("<title>" + self.title + "</title>")
		pagetext.extend(self.style)		
		pagetext.append("</head>\n<body>")
		pagetext.extend(self.body)
		pagetext.append("</body></html>")
		return "\n".join(pagetext)
	def set_body(self,textblock):
		self.body = textblock
	def append_body(self,text):
		self.body.append(text)
	

class itemlist:
	def __init__(self,startno=""):
		self.body = []
		if startno == "":
			self.tag = "ul"
		else:
			self.tag = "ol"	
	def get_list(self):
		listtext = []
		listtext.append(f"<{self.tag}>")
		listtext.extend(self.body)
		listtext.append(f"</{self.tag}>")
		return ("\n".join(listtext))
	def get_body(self):
		return(self.body)
	def additem(self,text):
		self.body.append("<li>" + text + "</li>")
		
def tag(tagname,text):
	return("<{0}>{1}</{0}>".format(tagname,text))
def heading(level,text,idno=0):
	id = "id" + str(idno)
	#return("<h{0}>{1}</h{0}>".format(level,text))
	return("<h{0} id=\"{2}\">{1}</h{0}>".format(level,text,id))

