# CatFood Overview

This is a rudimentary Python script designed to process a few ingredient lists and compare them in an HTML document.

### Requirements

[Jinja](https://jinja.palletsprojects.com/)
[Python](https://www.python.org/)

# Process

  1. Copy source information into list
  2. Iterate through list to generate `Food` objects
  3. Present each unique ingredient and categorize, note terms to clean/rename
  4. Categorize `Food` ingredients
  5. Find unique ingredients for each category (ex: Food A has blueberries in "Plants", no others do)
  6. Generate HTML page with **Jinja2** template
  7. Compare formulations!
  
## Source Information

Information was manually copied from an online retailer. See [text document](/source_info.txt).

## Cleaning

Leading / trailing whitespace and various superflous information was removed on the initial cleaning.
Later, more specific things were removed or altered. For example, a list of vitamins, "..., Vitamins (x,y,z . . .), ..."
were broken out into individual ingredients (x,y,z . . .). Cleaning steps will not be fullly described.

Regex could have been a cleaner option to process the ingredient lists.

## Categorization

Category lists were populated as the cleaning steps were developed. 
Therefore, the lists in the script contain more terms than will be necessary.

The `adjusters` list was used to capture the parsed ingredients to be cleaned, and to determine cleaning methods.
The following illustrates how the lists were populated:

```python
for val in data.values():
    for item in val.ingredients:
        item = item.lower()
        if item not in meats_protein and item not in plants_oil and item not in vits_minerals and item not in biotics and item not in others and item not in adjusters:
            print(item,'\n')
            print('1. ', 'meats')
            print('2. ', 'plants-oils')
            print('3. ', 'vits-minerals')
            print('4. ', 'biotics')
            print('5. ', 'others')
            print('6. ', 'adjust')
            cat = int(input('Enter category number for ingredient:'))
            
            if cat == 1:
                meats_protein.append(item)
            elif cat == 2:
                plants_oil.append(item)
            elif cat == 3:
                vits_minerals.append(item)
            elif cat == 4:
                biotics.append(item)
            elif cat == 5:
                others.append(item)
            elif cat == 6:
                adjusters.append(item)
            else:
                print('Invalid category!')
        print('\n\n')
```


## Re-Naming

Some ingredients were renamed to consolidate related items, such as "de-boned duck" and "deboned duck" to "duck".
All vitamin supplements and sources were renamed to their `Vitamin X` name, and added to their own category.

After vitamins were renamed, the final categories for each ingredient list were:
  * Proteins
  * Plants/Oils
  * Vitamins
  * Nutrients
  * Biotics
  * Others
  
Categorization served to provide easy comparison of formulations, and 
was not meant to provide accurate description of each ingredient.
  
## HTML Generation

The processed data was passed through Jinja2 to an HTML [template](/templates/catfood.html), and saved. 
See the [output here](/example.html). Unique ingredients for each category were highlighted. The top row was stickied.

**Page Layout**

|  | Food A, price | Food B, price |  ... |
| :----: | --- | --- | --- |
| Meats/Protein | *alphabetized list* | *...* | *...* |
| Plants/Oils | *alphabetized list* | *...* | *...* |
| Vitamins | *alphabetized list* | *...* | *...* |
| Nutrients | *list+wiki links* | *...* | *...* |
| Others | *alphabetized list* | *...* | *...* |

