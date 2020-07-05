import json
from genson import SchemaBuilder

filename='demojson.json'
builder = SchemaBuilder()
with open(filename, 'r') as f:
    datastore = json.load(f)
    builder.add_object(datastore )

builder.to_schema()
print(builder.to_json())