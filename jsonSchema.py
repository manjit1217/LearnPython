import json
from pprint import pprint
import requests
# from genson import SchemaBuilder #This is used to convert to JSON Schema
# from jsonschema import validate# this is used to Validate the JSON Responce with Json Schema
# # schema = {
# #    "type" : "object",
# #      "properties" : {
# #         "price" : {"type" : "number"},
# #          "name" : {"type" : "number"},
# #     },
# # }
# responceJson={"name" : "Eggs", "price" : 34.99}
# #Below Code is used to Load a Json file and convert it to JSON schema responce
# filename='demojson.json'
# builder = SchemaBuilder()
# with open(filename, 'r') as f:
#     datastore = json.load(f)
#     builder.add_object(datastore )
# res=builder.to_schema()
# # pprint(res)
# # print("JSON Schema Responce:" ,res)
#
# url="http://www.github.com"
# r = requests.get('http://httpbin.org/get')
#
# print(r.json())
#
# # validate(instance=responceJson,schema=schema)#Here we are validating the Json resopnce with Json Schema

a={'electromagnetic': {'relative strength': '10^36', 'range': 'infinity', 'mediator': 'photons'}, 'strong': {'relative strength': '10^38', 'range': '10^-15', 'mediator': 'gluons'}, 'weak': {'relative strength': '10^25', 'range': '10^-18', 'mediator': 'W/Z bosons'}, 'gravity': {'relative strength': '1', 'range': 'infinity', 'mediator': 'gravitons'}}

print(type(a))
print(json.dumps(a))
print(json.load(a))
x = ['524901','703448','2643743']
filename='demojson.json'
with open(filename, 'r') as f:
    datastore = json.load(f)
print(type(datastore))
# x=list(map(str, input("Enter the id: ").split()))
# print(x)
# id=','.join(x)
# url=f'http://api.openweathermap.org/data/2.5/group?id={id}&units=metric&appid=6d4c202370ae8d7c76ee8edefc512a4f'
# r=requests.get(url)
# x=r.json()

#
# outp={}
# country=[]
# x=datastore
# for c in x['list']:
#     country = []
#     x=c['sys']['country']
#     if x in outp:
#         outp[x].append(c['name'])
#     else:
#         country.append(c['name'])
#         outp[x] = country
# print(outp)

# a={'a':2,'b':3}
# print(a['b'])
# if 'a' in a:
#     print('a')
# else:print('b')
# #     for sys in c['sys']:
# #         print (c[sys]
#
