#!/usr/bin/env python

import csv
import uuid
import random
from faker import Faker

RECORD_COUNT = 10000

faker = Faker()


def write_to_csv():
    with open("./publishing_data.csv", "w", newline="") as csvfile:
        fieldnames = ["id", "title", "body", "author"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(RECORD_COUNT):
            id = uuid.uuid3(uuid.NAMESPACE_DNS, faker.url())
            writer.writerow(
                {
                    "id": id,
                    "title": faker.sentence(),
                    "body": faker.paragraph(50).replace("\n", ", "),
                    "author": faker.name(),
                }
            )


if __name__ == "__main__":
    write_to_csv()
