import pandas as pd

# Load operator names into a DataFrame (remove duplicates)
operators_df = pd.read_csv('operatorsListLatest.csv', header=None, names=['Operator'])
operators_df = operators_df.drop_duplicates()

# Load results into another DataFrame
results_df = pd.read_csv('output.csv', header=None, names=['ID', 'Operator', 'Values'])

# Convert 'Values' to numeric
results_df['Values'] = pd.to_numeric(results_df['Values'], errors='coerce')

# Merge the two DataFrames based on the operator names
merged_df = pd.merge(operators_df, results_df[['Operator', 'Values']], on='Operator', how='inner')

# Filter rows where 'Values' is not 0
filtered_df = merged_df[merged_df['Values'] != 0]

# Remove duplicate rows (same 'Operator' and 'Values')
filtered_df = filtered_df.drop_duplicates(subset=['Operator', 'Values'])


sorted_df = filtered_df.sort_values(by='Operator')

# Save the result to a new file without the 'ID' field
sorted_df[['Operator', 'Values']].to_csv('filteredResults.csv', index=False)

print("Filtered results without duplicates saved to 'filtered_results.csv'.")
