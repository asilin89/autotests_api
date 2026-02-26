from jsonschema import validate


schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
    },
    "required": ["name"]
}

data = {
    "name": "Alex",
    "age": 20,
}

a = validate(instance=data, schema=schema)

print(a)
print(type(a))