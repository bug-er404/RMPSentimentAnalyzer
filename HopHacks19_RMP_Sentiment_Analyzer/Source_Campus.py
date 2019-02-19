import urllib
from bs4 import BeautifulSoup

def Function_Campus():

	search = "https://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=schoolName&query="

	input = open('Campus_Name.txt', 'r')
	for current_char in input:
		   if current_char == ' ':
		           search = search + '+'
		   else:
		           search = search + current_char

	page = urllib.urlopen(search)
	soup = BeautifulSoup(page, 'html.parser')

	search_result = soup.find('li', {'class' : 'listing SCHOOL'})
	href_id = search_result.find('a')

	link = "https://www.ratemyprofessors.com" + href_id.get('href')
	page = urllib.urlopen(link)
	soup = BeautifulSoup(page, 'html.parser')

	comments_list = soup.findAll('td', {'class' : 'comments'})

	file = open('Comments_Campus.txt', 'w')

	for current_comment in comments_list:
		   for result in current_comment.find('p'):
		           file.write(result.encode('utf-8'))

	file.close()
	
if __name__ == '__main__':

	Function_Campus()
