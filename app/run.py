from flask import Flask, render_template, request
import datetime
from app import get_recipes
import json

app = Flask(__name__)

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

@app.route("/")
def template_test():

    response = dict(
    )

    return render_template('index.html', title="Appetite Maker", response=response)

@app.route("/home")
def home():

    response = dict(
       my_string="Wheeeee!",
       my_list=[0,1,2,3,4,5],
       current_time=datetime.datetime.now()
    )

    return render_template('template.html', title="Home", response=response)

@app.route("/about")
def about():

    response = dict(
       my_string="Wheeeee!",
       my_list=[0,1,2,3,4,5],
       current_time=datetime.datetime.now()
    )

    return render_template('template.html', title="About", response=response)

@app.route("/contact")
def contact():

    response = dict(
       my_string="Wheeeee!",
       my_list=[0,1,2,3,4,5],
       current_time=datetime.datetime.now()
    )

    return render_template('template.html', title="Contact Us", response=response)

@app.route("/recipes")
def recipes():

    ingredients = request.args.get('ingredients')

    ingredients = ingredients.split('  ')

    ingredients = filter(None, ingredients)

    json = get_recipes(ingredients, api="findByIngredients")

    common_ingredients = 0

    for item in json:
        id = item['id']
        recipe = get_recipes(id=str(id), api='recipes')
        for ing in recipe['extendedIngredients']:
            ing_name = str(ing['name'])
            if (ing_name in ingredients):
                common_ingredients += 1
        item['extraIngredients'] = len(recipe['extendedIngredients']) - common_ingredients


    response = dict(
       json=json
    )

    return render_template('recipes.html', title="Recipes", response=response)

@app.route("/recipe")
def recipe():

    id = request.args.get('id')

    json = get_recipes(id=id, api='recipes')

    response = dict(
       json=json
    )

    return render_template('recipe.html', title="Recipe", response=response)


@app.context_processor
def inject_enumerate():
    return dict(
        enumerate=enumerate
    )

if __name__ == '__main__':
    app.run(host= '104.236.44.120', port="80")
