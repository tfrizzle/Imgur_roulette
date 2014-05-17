import urllib.request, string, random

LETTERNUM = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	
def main():	
	print("imgur_roulette main ran")

# generates random alphanum of whatever length passed as i
def gen_id(i, result = ''):
	for x in range(i): result += random.choice(LETTERNUM)
	return result

# checks a url for redirects, returns false if none are detected
def imgur_removed_check(url):
	result = urllib.request.urlopen(url).geturl()
	if result == url: return False
	else: return True

# checks a url and returns the http code. 200 = good.
def check_url(url = 'http://www.google.com'):
	return urllib.request.urlopen(url).getcode()

# for use as a support lib
def gen_url(length = 5):
	while True:
		test_case = 'http://i.imgur.com/%s.jpg' % gen_id(length)
		if check_url(test_case) is 200 and not imgur_removed_check(test_case): 
			break
	return test_case
			

	
main()