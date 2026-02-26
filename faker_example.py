from faker import Faker

faker = Faker()

#print(faker.email())
# print(faker.address())
# print(faker.building_name())

data = {
    "name": faker.name(),
    "age": faker.random_int(18, 80),
    "email": faker.email(),
    "phone": faker.phone_number()
}

print(data)
