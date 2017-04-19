def app(environ, start_response):
	"""Simplest possible application object"""
	data = b"str\n"
	data += str.encode(environ['QUERY_STRING'])
	status = '200 OK'
	response_headers = [
		('Content-type','text/plain'),
		('Content-type', str(len(data)))
	]
	start_response(status, response_headers)
	return iter([data])
