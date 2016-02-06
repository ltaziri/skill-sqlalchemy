"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name=="Corvette", Model.brand_name=="Chevrolet").all();
# Get all models that are older than 1960.
Model.query.filter(Model.year<1960).all()
# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded>1920).all()
# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()
# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded==1903, Brand.discontinued==None ).all()
# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter((Brand.founded<1950) | (Brand.discontinued!=None)).all()
# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name !="Chevrolet").all()
# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = db.session.query(Model.name, 
                                  Model.brand_name, 
                                  Brand.headquarters).join(Brand).filter(Model.year==year).one()

    print "Model name: %s, Brand name: %s, Headquarters: %s" % (model_info[0], model_info[1], model_info[2])



def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    models_by_brand = db.session.query(Model.brand_name, Model.name).distinct().all();

    brand_dict={}

    for car in models_by_brand:
        brand = car[0]
        model = car[1]
        if brand_dict.get(brand):
            brand_dict[brand].append(model)
        else:
            brand_dict[brand]=[model]

    for brand in brand_dict:
        models = brand_dict[brand]
        model_string = brand_dict[brand][0]
        for model in models[1:]:
            model_string=model_string + ", " +  model 

    print "Brand: %s\t\tModels: %s\n" % (brand, model_string)
          
# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# You are returning a SQLAlchemy object that allows you to use query methods on it.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table is a table that contains no unique data of its own, only 
# foreign keys of other tables. The sole purpose of it is to connect two other 
# tables that if tried to combine directly they would have a many to many relationship. 
