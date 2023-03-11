from json import load, dumps
from copy import deepcopy

template = load(open('template.json', 'r', encoding='utf-8'))
categories = load(open('./meta/categories.json', 'r', encoding='utf-8'))
country_codes = load(open('./meta/country_codes.json', 'r', encoding='utf-8'))

category_list = list(categories.keys())

def validate_registrant(code: str):
    charset = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code_upper = code.upper()
    if len(code) != 5:
        return False, "Registrant code must be five characters"
    if code_upper[:2] not in country_codes:
        return False, "Country code not recognized."
    for char in code_upper[2:]:
        if char not in charset:
            return False, "Registrant code has non-alphanumeric character(s)."
    return True, code_upper

def validate_category(catnum):
    try:
        catnum = int(catnum)
        if category_list[catnum]:
            return True, category_list[catnum]
        else:
            return False, "Number not listed above."
    except ValueError:
        return False, "Please enter an interger."
    
def validate_string(input):
    if isinstance(input, str):
        return True, input
    else:
        return False, "Must be string."
    
def validate_discogs(link: str):
    if 'https://www.discogs.com/' in link:
        return True, link
    else:
        return False, "Not a discogs artist link, should start with https://www.discogs.com/"
    
def comma_list(input):
    return True, [x.strip() for x in input.split(',')]

def repeat_input(question: str, validate):
    while True:
        ans = input(question+": ")
        check = validate(ans)
        if check[0] != False:
            return check[1]
        else:
            print("Invalid input: "+check[1])

def ask_yn(question: str):
    while True:
        ans = input(question+" (Y/N): ").upper()
        if ans == "Y":
            return True
        elif ans == "N":
            return False
        else:
            print("Invalid input.")


# Registrant Code
entry_registrant = repeat_input("Enter registrant code", validate_registrant)

# Registrant Name
entry_name = repeat_input("Enter the name for the registrant", validate_string)

# Registrant Category
for i, v in enumerate(category_list):
    print(f"[{i}] {v} - {categories[v]}")
entry_category = repeat_input("Enter the category number of the distributor", validate_category)

# Registrant description
entry_descrption = repeat_input("Enter a short description of the entry", validate_string)

# Registrant discogs link
entry_discogs = repeat_input("Enter the link for the registrant on discogs", validate_discogs)

# Genres
entry_genres = repeat_input("Enter the genres that the registrant relate to, separated by a comma", comma_list)

# Sublabels (ONLY applicable to distributors and labels)
entry_sublabels = repeat_input("Any sublabels for this registrant? Enter them", comma_list)

print('\n==================================\n')

entry = deepcopy(template)

entry['name'] = entry_name
entry['country'] = country_codes[entry_registrant[:2]]
entry['country_code'] = entry_registrant[:2]
entry['registrant_code'] = entry_registrant[2:]
entry['category'] = entry_category
entry['description'] = entry_descrption
entry['discogs_link'] = entry_discogs
entry['genres'] = entry_genres
entry['sublabels'] = entry_sublabels

print("Your entered data is as follows:\n")
print(dumps(entry, indent=4))
finish = ask_yn("Is this correct?")
if finish == True:
    with open(f'./isrc/{entry_registrant}.json', 'w', encoding='utf-8') as file:
        file.write(dumps(entry,indent=4))
        file.close()
        print("Entry added!")
        input("Press enter to exit script.")
else:
    input("Press enter to exit script, then restart again.")
