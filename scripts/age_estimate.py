import csv


def calculate_age(lifespan: int) -> str:
    num_weeks = int(lifespan / 10)
    num_years, remainder = divmod(num_weeks, 4 * 12)
    num_months = int(remainder / 4)

    return f"{num_years} years, {num_months} months"


data = []
with open("lifespans.csv") as input_stream:
    reader = csv.DictReader(input_stream)
    for row in reader:
        row["Estimated age*"] = calculate_age(int(row["Lifespan"]))
        data.append(row)

# for row in sorted(data, key=lambda row: row["Breed"]):
#    print(row)

with open("ages.csv", "w") as output_stream:
    writer = csv.DictWriter(output_stream, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
