import csv


def clean_and_get_top_10(file_path, output_file, column_name):
    # Read the CSV and remove duplicates
    unique_entries = {}
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            operator = row["Operator"]
            result = float(row[column_name])
            # Keep the highest result for each operator
            if operator not in unique_entries or result > unique_entries[operator]:
                unique_entries[operator] = result

    # Sort the unique entries by Result in descending order
    sorted_entries = sorted(unique_entries.items(), key=lambda x: x[1], reverse=True)

    # Save the cleaned results to a new CSV
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Operator", column_name])  # Write header
        writer.writerows(sorted_entries)

    # Print the top 10 entries
    print("Top 10 entries by Result:")
    for i, (operator, result) in enumerate(sorted_entries[:10], start=1):
        print(f"{i}. {operator}: {result}")


# Specify file paths and column
input_csv = "merged_results.csv"
cleaned_csv = "cleaned_results.csv"
result_column = "Result"

# Clean the CSV and print the top 10
clean_and_get_top_10(input_csv, cleaned_csv, result_column)