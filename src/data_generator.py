import csv
import uuid
import random
from faker import Faker
from rich.progress import track

RECORD_COUNT = 10_000

faker = Faker()


def generate_data():
    total = 0
    with open("data/publishing_data.csv", "w", newline="") as csvfile:
        fieldnames = ["id", "title", "body", "author"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in track(range(RECORD_COUNT), description="Generating data records..."):
            id = uuid.uuid3(uuid.NAMESPACE_DNS, faker.url())
            writer.writerow(
                {
                    "id": id,
                    "title": faker.sentence(),
                    "body": faker.paragraph(50).replace("\n", ", "),
                    "author": faker.name(),
                }
            )
            total += 1
    print(f"Generated {total} records.")
