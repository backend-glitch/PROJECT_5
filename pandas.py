

import pandas as pd
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv("/kaggle/input/new-contact/dataset_100rows.csv")


print("🔹 First 5 records:")
display(df.head())

print("\n🔹 Basic Info:")
df.info()



def filter_by_age(min_age, max_age):
    result = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]
    print(f"\n🔹 Contacts aged between {min_age} and {max_age}:")
    display(result)


def filter_by_gender(gender):
    result = df[df['Gender'].str.lower() == gender.lower()]
    print(f"\n🔹 Contacts with gender = {gender}:")
    display(result)


def filter_by_address(keyword):
    result = df[df['Address'].str.contains(keyword, case=False, na=False)]
    print(f"\n🔹 Contacts from {keyword}:")
    display(result)


def filter_by_name_initial(initial):
    result = df[df['Name'].str.startswith(initial, na=False)]
    print(f"\n🔹 Contacts whose name starts with '{initial}':")
    display(result)


def filter_by_number_range(start, end):
    result = df[(df['Number'] >= start) & (df['Number'] <= end)]
    print(f"\n🔹 Contacts with numbers between {start} and {end}:")
    display(result)


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



print("\n🔹 Sorted by Name (A-Z):")
display(df.sort_values(by='Name'))

print("\n🔹 Sorted by Age (Youngest → Oldest):")
display(df.sort_values(by='Age'))



print("\n🔹 Basic Statistics:")
display(df.describe(include='all'))



