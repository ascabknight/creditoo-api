def split_name(name):
	tokens = name.split(" ")
	names = []
	
	especial_tokens = ['da', 'de', 'di', 'do', 'del', 'la', 'las', 'le', 'los', 'mac', 'mc', 'van', 'von', 'y', 'i', 'san', 'santa']
 
	prev = ""
	for token in tokens:
		_token = token.lower()
		if _token in especial_tokens:
			prev += token + " "
		else:
			names.append(prev + token)
			prev = ""
			
	return names