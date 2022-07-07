from faker import Faker

fake = Faker()

# rep = fake.text(max_nb_chars=10000)
rep = fake.sentence(nb_words=10, variable_nb_words=True)

print(rep)