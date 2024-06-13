import random
from DB_connection import save
from faker import Faker
from calculation import save_record, calculate, status

fake = Faker()
for _ in range(50):
    w = random.randrange(50, 400)
    h = random.uniform(1.30, 2.20)
    bmi = calculate(w=w, h=h)
    stat = status(bmi)
    save(name=fake.name(), lname=fake.last_name(), h=h, w=w, bmi=bmi, status=stat)
    