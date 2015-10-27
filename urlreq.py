import urllib2
req =urllib2.Request('http://voidspace.org.uk')
response =urllib2.urlopen(req)
the_page = response.read()
