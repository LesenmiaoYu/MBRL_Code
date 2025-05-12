import csv

# File paths
operator_list_file = "operatorList.csv"
output_file = "output.csv"
merged_file = "merged_results.csv"

def merge_operator_results():
    # Load operator list into a set for fast lookup
    operators = []
    with open(operator_list_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            operators.append(row[0].strip())  # Assuming one operator per row

    # Load output file into a dictionary for quick access
    output_results = {}
    with open(output_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            name = row[1].strip()  # Operator name
            result = row[2].strip()  # Result value
            output_results[name] = result

    # Prepare merged data
    merged_data = []
    for operator in operators:
        if operator in output_results:
            merged_data.append([operator, output_results[operator]])  # Match found
        else:
            merged_data.append([operator, "999"])  # Default value if no match

    # Write merged data to a new CSV
    with open(merged_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Operator", "Result"])  # Header row
        writer.writerows(merged_data)

    print(f"Merged results saved to {merged_file}")

# Run the merge function
merge_operator_results()