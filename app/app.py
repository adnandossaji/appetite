import requests
import json

def make_url(base_url="", api="", **kwargs):
    new_url = base_url + api + "?"

    for num, (key, val) in enumerate(kwargs.iteritems()):
        if (num != len(kwargs) - 1):
            new_url += str(key) + "=" + str(val) + "&"
        else:
            new_url += str(key) + "=" + str(val)

    return new_url

def get_recipes(ingredients=[], **kwargs):

    base_url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com"

    if kwargs['api'] == "findByIngredients":
        base_url += "/recipes/"
        url = make_url(base_url=base_url, api="findByIngredients", ingredients=ingredients, limit_license=False, number=28, ranking=1)
    elif kwargs['api'] == "recipes":
        base_url += "/recipes/" + kwargs['id']
        url = base_url + "/information"
        print url

    headers = {
        "X-Mashape-Key": "H8Cx7lqJhLmsh6Ti1QgDYaTqw5kxp1wAXrFjsnXb46We1mv2L4",
        "Accept": "application/json"
    }


    r = requests.get(url, headers=headers)

    response = json.loads(r.__dict__['_content'])

    return response