# Create a YAML file with sample data using the pyyaml library.
import yaml

# code to read from sample yaml file
# with open('sample.yaml', 'r') as file:
#     prime_service = yaml.safe_load(file)

# # print(prime_service)
# print(prime_service['rest']['port'])
names_for_yaml = """
- 'eric'
- 'sita'
- 'hari'
"""
names = yaml.safe_load(names_for_yaml)

with open('names.yaml', 'w') as file:
    yaml.dump(names, file)

print(open('names.yaml').read())
