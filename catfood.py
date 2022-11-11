from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
# Jinja environment
env = Environment( 
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

# Source Data, price in dollars / lbs
foods = [
'''
name:Royal Canin Veterinary Diet Adult Selected Protein PD Dry Cat Food
price:140/17.6
ingredients:Peas, Duck By-Product Meal, Pea Protein, Coconut Oil, Natural Flavors, Hydrolyzed Soy Protein, Vegetable Oil, Calcium Sulfate, Sodium Bisulfate, Dl-Methionine, Fish Oil, Sodium Pyrophosphate, Choline Chloride, Salt, Monocalcium Phosphate, Vitamins [Dl-Alpha Tocopherol Acetate (Source Of Vitamin E), Niacin Supplement, L-Ascorbyl-2-Polyphosphate (Source Of Vitamin C), D-Calcium Pantothenate, Biotin, Pyridoxine Hydrochloride (Vitamin B6), Riboflavin Supplement, Thiamine Mononitrate (Vitamin B1), Vitamin A Acetate, Folic Acid, Vitamin B12 Supplement, Vitamin D3 Supplement], Taurine, Calcium Carbonate, Trace Minerals [Zinc Proteinate, Zinc Oxide, Manganese Proteinate, Ferrous Sulfate, Manganous Oxide, Copper Sulfate, Sodium Selenite, Calcium Iodate, Copper Proteinate], Rosemary Extract, Preserved With Mixed Tocopherols And Citric Acid.
''','''
name:Blue Buffalo Basics Skin & Stomach Care Grain-Free Formula Duck & Potato Indoor Adult Dry Cat Food
price:45/11
ingredients:Deboned Duck, Duck Meal, Pea Protein, Peas, Tapioca Starch, Potatoes, Canola Oil, Pea Fiber, Flaxseed (source of Omega 6 Fatty Acids), Pea Starch, Natural Flavor, Fish Oil (source of Omega 3 Fatty Acids), DL-Methionine, Choline Chloride, Potassium Chloride, Calcium Sulfate, Taurine, Pumpkin, Dried Chicory Root, Alfalfa Nutrient Concentrate, Calcium Carbonate, Salt, Calcium Chloride, Vitamin E Supplement, preserved with Mixed Tocopherols, L-Ascorbyl-2-Polyphosphate (source of Vitamin C), Vegetable Juice for color, Ferrous Sulfate, Niacin (Vitamin B3), Iron Amino Acid Chelate, Zinc Amino Acid Chelate, Zinc Sulfate, Blueberries, Cranberries, Barley Grass, Parsley, Turmeric, Dried Kelp, Yucca Schidigera Extract, Copper Sulfate, Thiamine Mononitrate (Vitamin B1), Copper Amino Acid Chelate, L-Lysine, Biotin (Vitamin B7), Vitamin A Supplement, Manganese Sulfate, Manganese Amino Acid Chelate, Pyridoxine Hydrochloride (Vitamin B6), Calcium Pantothenate (Vitamin B5), Riboflavin (Vitamin B2), Vitamin D3 Supplement, Vitamin B12 Supplement, Folic Acid (Vitamin B9), Dried Yeast, Dried Enterococcus faecium fermentation product, Dried Lactobacillus acidophilus fermentation product, Dried Aspergillus niger fermentation extract, Dried Trichoderma longibrachiatum fermentation extract, Dried Bacillus subtilis fermentation extract, Calcium Iodate, Sodium Selenite, Oil of Rosemary.
''','''
name:Natural Balance L.I.D. Limited Ingredient Diets Green Pea & Duck Formula Grain-Free Dry Cat Food
price:43/10
ingredients:Green Peas, Duck, Duck Meal, Pea Protein, Canola Oil (Preserved with Mixed Tocopherols), Natural Flavor, Salmon Oil (Preserved with Mixed Tocopherols), Flaxseed, Salt, Choline Chloride, Dl-Methionine, Minerals (Zinc Proteinate, Zinc Sulfate, Ferrous Sulfate, Iron Proteinate, Copper Sulfate, Copper Proteinate, Manganese Sulfate, Manganese Proteinate, Calcium Iodate, Sodium Selenite), Vitamins (Vitamin E Supplement, Niacin, Thiamine Mononitrate, D-Calcium Pantothenate, Vitamin A Supplement, Pyridoxine Hydrochloride, Riboflavin Supplement, Vitamin D3 Supplement, Vitamin B12 Supplement, Folic Acid, Biotin), Taurine, Mixed Tocopherols (Preservative), Rosemary Extract, Green Tea Extract, Spearmint Extract.
''','''
name:Go! SENSITIVITIES Limited Ingredient Duck Grain-Free Dry Cat Food
price:73/16
ingredients:De-Boned Duck, Duck Meal, Whole Dried Egg, Peas, Pea Flour, Tapioca, Lentils, Chickpeas, Chicken Fat (Preserved With Mixed Tocopherols), Flaxseed, Natural Flavour, Sodium Chloride, Choline Chloride, Calcium Carbonate, Dried Chicory Root, Phosphoric Acid, Potassium Chloride, Vitamins (Vitamin A Supplement, Vitamin D3 Supplement, Vitamin E Supplement, Niacin, L-Ascorbyl-2-Polyphosphate (A Source Of Vitamin C), Thiamine Mononitrate, D-Calcium Pantothenate, Riboflavin, Pyridoxine Hydrochloride, Beta-Carotene, Folic Acid, Biotin, Vitamin B12 Supplement), Minerals (Zinc Proteinate, Iron Proteinate, Copper Proteinate, Zinc Oxide, Manganese Proteinate, Copper Sulphate, Calcium Iodate, Ferrous Sulphate, Manganous Oxide, Sodium Selenite), Taurine, Dried Rosemary.
''']

# Categories, contains extra stuff from cleaning development
meats_protein = ['duck by-product meal','pea protein','hydrolyzed soy protein','deboned duck','duck meal','duck','de-boned duck','whole dried egg','chicken fat']
plants_oil = ['peas','coconut oil','vegetable oil','fish oil','rosemary','rosemary extract','tapioca starch','potatoes','canola oil','pea fiber','flaxseed (omega 6 fatty acids)','pea starch','fish oil (omega 3 fatty acids)','pumpkin','dried chicory root','alfalfa nutrient concentrate','blueberries','cranberries','barley grass','parsley','turmeric','dried kelp','yucca schidigera extract','oil of rosemary','green peas','canola oil','salmon oil','flaxseed','green tea extract','spearmint extract','pea flour','tapioca','lentils','chickpeas','dried rosemary']
vits_minerals = ['dl-methionine','choline chloride','salt','niacin supplement','l-ascorbyl-2-polyphosphate (vitamin c)','d-calcium pantothenate','biotin','pyridoxine hydrochloride (vitamin b6)','riboflavin supplement','thiamine mononitrate (vitamin b1)','vitamin a acetate','folic acid','vitamin b12 supplement','vitamin d3 supplement','taurine','zinc oxide','manganese proteinate','ferrous sulfate','manganous oxide','copper sulfate','sodium selenite','calcium iodate','copper proteinate','dl-alpha tocopherol acetate (vitamin e)','zinc proteinate','potassium chloride','vitamin e supplement','niacin (vitamin b3)','iron amino acid chelate','zinc amino acid chelate','zinc sulfate','copper amino acid chelate','l-lysine','biotin (vitamin b7)','vitamin a supplement','manganese sulfate','manganese amino acid chelate','calcium pantothenate (vitamin b5)','riboflavin (vitamin b2)','vitamin d3 supplement','folic acid (vitamin b9)','iron proteinate','copper proteinate','sodium selenite','niacin','thiamine mononitrate','pyridoxine hydrochloride','biotin','sodium chloride','l-ascorbyl-2-polyphosphate\xa0(vitamin c)','riboflavin','beta-carotene','vitamin b12 supplement','copper sulphate','ferrous sulphate']
biotics = ['dried yeast','dried enterococcus faecium fermentation product','dried lactobacillus acidophilus fermentation product','dried aspergillus niger fermentation extract','dried trichoderma longibrachiatum fermentation extract','dried bacillus subtilis fermentation extract']
others = ['natural flavors','calcium sulfate','sodium bisulfate','sodium pyrophosphate','monocalcium phosphate','calcium carbonate','mixed tocopherols and citric acid','natural flavor','calcium chloride','preserved with mixed tocopherols','vegetable juice for color','mixed tocopherols (preservative)','natural flavour','phosphoric acid', 'mixed tocopherols']

# Translations, unify common names and rename vitamins for categorization
renames = {'duck by-product meal':'duck meal', 'de-boned duck':'duck', 'deboned duck': 'duck', 'copper sulphate':'copper sulfate',
 'natural flavors':'natural flavor', 'natural flavour':'natural flavor', 'sodium chloride':'salt', 
 'vegetable oil':'canola oil','rosemary extract':'rosemary', 'oil of rosemary':'rosemary', 'dried rosemary':'rosemary', 'tapioca starch':'tapioca', 
 'mixed tocopherols and citric acid':'mixed tocopherols', 'mixed tocopherols (preservative)':'mixed tocopherols',
 'folic acid':'vitamin B9', 'niacin':'vitamin B3', 'riboflavin':'vitamin B2',
 'pyrodoxine hydrochloride':'vitamine B6','pyridoxine hydrochloride':'vitamin B6', 'thiamine mononitrate': 'vitamin B1',
 'd-calcium pantothenate': 'vitamin B5', 'biotin':'vitamin B7', 
 'beta-carotene':'vitamin A', 'vitamin a acetate': 'vitamin A'}

# break lists of stuff, eliminate certain things 
adjust_list = ['vitamins [', 'trace minerals [', 'preserved with ', 'minerals (', 'vitamins (']
chop_list = [' (preserved with mixed tocopherols)', '.', ']', ' (omega 3 fatty acids)', ' (omega 6 fatty acids)']

# Food class for processing information
class Food:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price.split('/')
        self.ingredients = ingredients.split(',')
        
        self.categories = {} # categories for web page, corresponding to above
        self.categories['proteins'] = []
        self.categories['plants_oils'] = []
        self.categories['nutrients'] = []
        self.categories['vitamins'] = []
        self.categories['biotics'] = []
        self.categories['others'] = []
        
        self.price_per_pound()
        self.cursory_clean()
        self.specific_clean()
        self.vitamin_names()
        self.vitamin_names()
        self.vitamin_names()
        self.vitamin_names()
        self.vitamin_names()

        self.ingredients = [val.title() for val in self.ingredients]
        self.categorize()       
        for val in self.categories.keys():
            self.categories[val].sort()

    def price_per_pound(self): # normalize price
        if type(self.price) == float:
            return
        elif type(self.price) == list:
            self.price = round(float(self.price[0])/float(self.price[1]),2)
        else:
            print(f'{self.name} has invalid price!')
            return
    
    def cursory_clean(self): # take out trailing whitespace, certain characters+phrases
        cleaned_ingredients = []
        for val in self.ingredients:
            cleaned_ingredients.append(val.strip().strip(']').strip('.'))
        self.ingredients = cleaned_ingredients
        for val in self.ingredients:
            if val.lower().find('(source of ') > 1:
                self.ingredients.remove(val)
                self.ingredients.append(val.lower().replace('source of ',''))
            elif val.lower().find('(a source of ') > 1:
                self.ingredients.remove(val)
                self.ingredients.append(val.lower().replace('a source of ',''))
            elif val.lower().find(' supplement') > 1:
                self.ingredients.remove(val)
                self.ingredients.append(val.lower().replace(' supplement',''))               
        
    def specific_clean(self): # see list of checks above
        for check in adjust_list: # break lists and others from beginning
            for val in self.ingredients:
                if val.lower().startswith(check):
                    self.ingredients.remove(val)
                    self.ingredients.append(val.lower().replace(check,''))

        for check in chop_list: # remove certain info/characters from end
            for val in self.ingredients:
                if val.lower().endswith(check):
                    self.ingredients.remove(val)
                    self.ingredients.append(val.lower().replace(check,''))

        for val in self.ingredients: # leftovers from lists
            if val.find(')') > 0 and val.find('(') < 0:
                self.ingredients.remove(val)
                self.ingredients.append(val.replace(')',''))

    def vitamin_names(self): # reduce name to Vitamin Y from X (Vitamin Y)
        for val in self.ingredients: 
            if val.lower().find('(vitamin ') > 0:
                self.ingredients.remove(val)
                self.ingredients.append(val[val.lower().find('(vitamin ')+1:-1])
        for val in self.ingredients:  # renames, needs multiple iterations
            if val.lower() in renames.keys():
                self.ingredients.remove(val)
                self.ingredients.append(renames[val.lower()])
        for val in self.ingredients: # redo in case
            if val.lower().find(' supplement') > 1: 
                self.ingredients.remove(val)
                self.ingredients.append(val.lower().replace(' supplement',''))     
    
    def __str__(self): # convenient print for template
        return f'{self.name}\n${self.price} per pound'
        
    def categorize(self): # add ingredients to categories, alert if not categorized
        for val in self.ingredients:
            if val.lower().startswith('vitamin '):
                self.categories['vitamins'].append(val)
            elif val.lower() in meats_protein:
                self.categories['proteins'].append(val)
            elif val.lower() in vits_minerals:
                self.categories['nutrients'].append(val)
            elif val.lower() in plants_oil:
                self.categories['plants_oils'].append(val)         
            elif val.lower() in biotics:
                self.categories['biotics'].append(val)  
            elif val.lower() in others:
                self.categories['others'].append(val)
            else:
                print(val, 'NOT CATEGORIZED!!!')

# split up source information and generate cleaned and categorized data
data = {}
for val in foods:
    val_list = val.split('\n')[1:-1]
    name = val_list[0].split(':')[1]
    price = val_list[1].split(':')[1]
    ingredients = val_list[2].split(':')[1]
    data[name] = Food(name, price,ingredients)

# bold ingredients that are unique across foods, in a given category
for key in data.keys(): 
    food = data[key]
    others = list(data.keys())
    others.remove(key)   
    for cat in food.categories.keys():
        for item in food.categories[cat]:
            check = False
            for other in others:
                if item.startswith('Pea') or item.endswith(' Peas'): # various forms of peas in everything
                    check = True
                    break
                if item in data[other].categories[cat]:
                    check = True
                    break
            if not check:
                food.categories[cat][food.categories[cat].index(item)] = f'<span class="text-warning bg-dark pe-2 py-1">{item}</span>'

# generate Jinja2 template                
template = env.get_template('catfood.html')
favi = str(Path(Path.cwd(), 'static', 'favicon.png'))
with open(Path('test.html'), 'w', encoding='utf-8') as page:
    page.write(template.render(data=data, favi=favi))                   