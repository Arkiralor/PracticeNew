from faker import Faker

fake = Faker('en-IN')

# rep = fake.text(max_nb_chars=10000)
# rep = fake.sentence(nb_words=10, variable_nb_words=True)
fname = fake.first_name()
lname = fake.last_name()
# zip_code = fake.zipcode()

print(f"{fname} {lname}")
# print(zip_code)