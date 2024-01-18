# import urllib
# use urllib.request to get data from the url
# define a fuction that takes a url
# return a response

import urllib.request as urllib

def main(url):
    print("Checking Connectivity...")

    response = urllib.urlopen(url)

    print("Connected to ", url, " Successfully")
    print("The response code was ", response.getcode())

print("PYTHON SITE CONNECTIVITY CHECKER")
print("--------------------------------\n")
input_url = input("Input the site url you want to check: ")
main(input_url)