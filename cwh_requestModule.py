
# requests Module - The requests.Response() Object contains the server's response to the HTTP Object

# import requests
# from bs4 import BeautifulSoup

# Example 1 

# response = requests.get("https://www.codewithharry.com")
# print(response.text)


# Example 2

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title" : 'foo',
#     "body"  : 'bar',
#     "userId":  1,
# }

# headers = {
#     'Content-type' : 'application/json; charset=UTF-8',
# }

# response = requests.post(url, headers=headers, json = data)

# print(response.txt)


# Example 3

# url = "https://www.codewithharry.com/blogpost/djangocheatsheet/"

# r = requests.get(url)

# soup = BeautifulSoup(r.text, 'html.parser')

# # print(soup.prettify())

# ## to get all the blog headings in h2 size we do as follows:

# for heading in soup.find_all("h2"):
#     print(heading.text)

