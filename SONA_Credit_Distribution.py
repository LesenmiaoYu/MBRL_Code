# import pandas as pd
# import os
#
# # Get the current directory where the script is running
# directory = os.getcwd()
#
# # List to store the results
# results = []
#
# # Loop through each file in the directory
# for filename in os.listdir(directory):
#     if filename.endswith('.csv'):
#         # Construct the full file path
#         filepath = os.path.join(directory, filename)
#
#         # Try to load the CSV file into a DataFrame, handling potential parsing errors
#         try:
#             df = pd.read_csv(filepath, header=0)
#             if df.empty:
#                 print(f"Skipping empty file: {filename}")
#                 continue
#
#             # Report the number of entries (rows) in the current CSV
#             print(f"Processing {filename} with {len(df)} entries.")
#
#             # Convert the 'Overall Creditpoints Earned' to float for proper comparison
#             df['Overall Creditpoints Earned'] = pd.to_numeric(df['Overall Creditpoints Earned'], errors='coerce')
#
#             # Filter rows where 'Overall Creditpoints Earned' is 0
#             zero_creditpoints = df[df['Overall Creditpoints Earned'] == 0]
#
#             # Iterate through these rows and store the required information
#             for index, row in zero_creditpoints.iterrows():
#                 results.append({'Email': row['Email'], 'CSV File Name': filename})
#
#         except pd.errors.EmptyDataError:
#             print(f"No data in file {filename}, skipping.")
#             continue
#         except pd.errors.ParserError as e:
#             print(f"Skipping file {filename} due to a parsing error: {e}")
#             continue
#         except Exception as e:
#             print(f"An unexpected error occurred while processing {filename}: {e}")
#             continue
#
# # Convert the results list to a DataFrame
# results_df = pd.DataFrame(results)
#
# # Path for the output CSV file, saved in the same directory
# output_csv_path = os.path.join(directory, 'results.csv')
#
# # Save the results to a new CSV file
# results_df.to_csv(output_csv_path, index=False)
#
# print('Results have been saved to:', output_csv_path)

#-------------------------------------------------------

import pandas as pd
import os
import numpy as np

# Get the current directory where the script is running
directory = os.getcwd()

# # #304
# # Define bins and labels for the credit completion categorization
# bins = [0, 0.49, 0.99, 1.49, 1.99, 2.49,2.99, float('inf')]
# labels = ['0-0.49', '0.5-0.99', '1-1.49', '1.5-1.99', '2-2.49', '2.5-2.99','3+']

# #497
# # Define bins and labels for the credit completion categorization
# bins = [0, 0.49, 0.99, 1.49, 1.99,  float('inf')]
# labels = ['0-0.49', '0.5-0.99', '1-1.49', '1.5-1.99', '2+']

#307
# Define bins and labels for the credit completion categorization
bins = [0, 0.49, 0.99, 1.49, 1.99, 2.49, 2.99, 3.49, 3.99, float('inf')]
labels = ['0-0.49', '0.5-0.99', '1-1.49', '1.5-1.99', '2-2.49', '2.5-2.99', "3-3.49", "3.5-3.99", "4+"]

# Initialize a list to store results
credit_distributions = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Construct the full file path
        filepath = os.path.join(directory, filename)

        # Try to load the CSV file into a DataFrame
        try:
            df = pd.read_csv(filepath, header=0)
            if df.empty:
                print(f"Skipping empty file: {filename}")
                continue

            # Ensure 'Creditpoints Earned for Course' is treated as a float
            df['Overall Creditpoints Earned'] = pd.to_numeric(df['Overall Creditpoints Earned'], errors='coerce')

            # Bin the data using the defined bins and labels
            df['category'] = pd.cut(df['Overall Creditpoints Earned'], bins=bins, labels=labels, right=False)

            # Calculate the counts for each category
            category_counts = df['category'].value_counts().reindex(labels, fill_value=0)

            # Append the results with class name and counts
            credit_distributions.append([filename] + category_counts.tolist())

        except Exception as e:
            print(f"An unexpected error occurred while processing {filename}: {e}")
            continue

# Create DataFrame from results
columns = ['class name (csv name)'] + labels
results_df = pd.DataFrame(credit_distributions, columns=columns)

# Path for the output CSV file, saved in the same directory
output_csv_path = os.path.join(directory, 'credit_distribution.csv')

# Save the results to a new CSV file
results_df.to_csv(output_csv_path, index=False)

print('Credit distribution has been saved to:', output_csv_path)
#-------------------
# import pandas as pd
# import os
#
# # Define the directory where your class CSV files are stored
# directory = os.getcwd()
#
# # Load the completion roster
# completion_df = pd.read_csv('completedContacts.csv')
# completed_emails = set(completion_df['email'].str.strip('"'))  # Remove quotes and create a set for faster lookup
#
# # List to store the results
# non_completed_students = []
#
# # Loop through each file in the directory
# for filename in os.listdir(directory):
#     if filename.endswith('.csv') and filename != 'completedContacts.csv':
#         # Construct the full file path
#         filepath = os.path.join(directory, filename)
#
#         # Load the class CSV file
#         df = pd.read_csv(filepath)
#         # Assume the email field in these files is also quoted and strip them
#         df['Email'] = df['Email'].str.strip('"')
#
#         # Filter to find non-completed students
#         non_completed = df[~df['Email'].isin(completed_emails)]
#
#         # Collect first name, last name, and email of non-completed students
#         for index, row in non_completed.iterrows():
#             non_completed_students.append({
#                 'First Name': row['First Name'],
#                 'Last Name': row['Last Name'],
#                 'Email': row['Email'],
#                 'Class CSV': filename
#             })
#
# # Convert the results to a DataFrame
# results_df = pd.DataFrame(non_completed_students)
#
# # Define the path for the output CSV
# output_csv_path = os.path.join(directory, 'non_completed_students.csv')
#
# # Save the results to a new CSV file
# results_df.to_csv(output_csv_path, index=False)
#
# print('Non-completed student details have been saved to:', output_csv_path)
