import csv
from pathlib import Path

CSV_FILE = Path("./food.csv")

def main():
    with open(CSV_FILE, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(
            csvfile,
            delimiter=',',
            quotechar='\''
        )

        # current wip
        line = next(reader)

    print("Wohoo! My food database is complete!")


if __name__ == "__main__":
    main()