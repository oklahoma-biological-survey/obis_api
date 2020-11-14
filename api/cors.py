class CorsMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response
	
	def __call__(self, request, response):
		response["Access-Control-Allow-Headers"] = "*"
		response["Access-Control-Allow-Methods"] = "*"
		return response
