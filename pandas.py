# -------------------------------------------
# 📘 CONTACTS DATA ANALYSIS NOTEBOOK (Enhanced)
# -------------------------------------------

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# 🟢 Step 1: Load dataset
df = pd.read_csv("/kaggle/input/new-contact/dataset_100rows.csv")

# 🟢 Step 2: Preview the dataset
print("🔹 First 5 records:")
display(df.head())

print("\n🔹 Basic Info:")
df.info()

# -------------------------------------------
# 🧭 SEARCH & FILTER FUNCTIONS
# -------------------------------------------

# 🔹 General search across all columns
def search_contact(keyword):
    result = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False).any(), axis=1)]
    if not result.empty:
        display(result)
    else:
        print("No results found.")

  # 🔹 Filter by Age Range
def filter_by_age(min_age, max_age):
    result = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]
    print(f"\n🔹 Contacts aged between {min_age} and {max_age}:")
    display(result)

# 🔹 Filter by Gender
def filter_by_gender(gender):
    result = df[df['Gender'].str.lower() == gender.lower()]
    print(f"\n🔹 Contacts with gender = {gender}:")
    display(result)

# 🔹 Filter by Address / State
def filter_by_address(keyword):
    result = df[df['Address'].str.contains(keyword, case=False, na=False)]
    print(f"\n🔹 Contacts from {keyword}:")
    display(result)

# 🔹 Filter by Name Starting Letter
def filter_by_name_initial(initial):
    result = df[df['Name'].str.startswith(initial, na=False)]
    print(f"\n🔹 Contacts whose name starts with '{initial}':")
    display(result)

# 🔹 Filter by Contact Number Range
def filter_by_number_range(start, end):
    result = df[(df['Number'] >= start) & (df['Number'] <= end)]
    print(f"\n🔹 Contacts with numbers between {start} and {end}:")
    display(result)


# -------------------------------------------
# 🧮 Examples
# -------------------------------------------

print("\n🔹 Searching for name 'Aman':")
search_contact("Aman")

print("\n🔹 Contacts from Delhi:")
filter_by_address("DL")

print("\n🔹 Contacts aged between 20 and 30:")
filter_by_age(20, 30)

print("\n🔹 Female contacts:")
filter_by_gender("Female")

print("\n🔹 Names starting with 'A':")
filter_by_name_initial("A")

print("\n🔹 Numbers between 5000000000 and 8000000000:")
filter_by_number_range(5000000000, 8000000000)


# -------------------------------------------
# 🧾 Sorting Examples
# -------------------------------------------

print("\n🔹 Sorted by Name (A-Z):")
display(df.sort_values(by='Name'))

print("\n🔹 Sorted by Age (Youngest → Oldest):")
display(df.sort_values(by='Age'))

# -------------------------------------------
# 📊 Basic Statistics
# -------------------------------------------

print("\n🔹 Basic Statistics:")
display(df.describe(include='all'))

# -------------------------------------------
# 💾 Export Filtered Data (Optional)
# -------------------------------------------

# Example: Save all contacts older than 25 to a new CSV file
df[df['Age'] > 25].to_csv("filtered_contacts.csv", index=False)
print("\n✅ Filtered contacts (Age > 25) saved to 'filtered_contacts.csv'")
