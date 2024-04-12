# import urllib library
from urllib.request import urlopen

# import json
import json
import pprint
# store the URL in url as
# parameter for urlopen

import json



url = "https://dummyjson.com/users"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data = json.loads(response.read())


# print the json response
# print(data)


class read_json_from_api():
    def json_from_api(self):
        # Opening JSON file
        f = open('data.json')

        # Iterating through the json
        # list

        print(type(data))
        # Closing file
        f.close()

        # print(list(data.values()))
        dict = {}
        dict = data['users']

        record = []
        rec = []

        for mydict in dict:
            record = ','.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
            app = record + ']' + "\n"
            rec.append(app)

        print(rec)
        print(type(rec))
        blist = []
        for i in range(len(rec)):
            blist.append(rec)
            if i == rec:
                print('\n')
        pprint.pprint(blist)


# reading the data from json and store into the data variable
class read_json_file():
    def json_from_file(self):
        with open('data.json') as f:
            data = json.load(f)

    pprint.pprint(data)


# creating the object of the  read_json_from_api and read_json_file

#object1 = read_json_from_api()
#object1.json_from_api() # calling the object && commenting the object so that it will not open the file and write the data
object2 = read_json_file()
object2.json_from_file()  # calling the object