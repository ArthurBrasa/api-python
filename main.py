import requests

r = requests.get('https://www.googleapis.com/customsearch/v1?key=AIzaSyCPGtQu_S6OGEIFgWx5vWGH2WSFZmeTFug&cx=e1f978a5b39b8481c&q=teste')
print(r.status_code)

print(r.json())




# Press the green button in the gutter to run the script.
# if __name__ == '__main__':

