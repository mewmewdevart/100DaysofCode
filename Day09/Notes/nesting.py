# Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

# Nesting a list in a Dictionary
# key : value | Nesting aceita apenas uma key e um value, para dicionar mais é necessario colocar a formatação do dicionario []
country_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# How to create a nested dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)

# Access elements of a Nested Dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
}

print(people[1]['name'])
print(people[1]['age'])
print(people[2]['sex'])

# Nesting a Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

wish_travel = {
    "North_America" : {"Canada" : ["Toronto", "Quebec", "Montreal"], "total_wish": 3,
                       "United States": ["New York", "Las Vegas", "Seattle"], "total_wish": 3,
                       "Mexico" : ["Mexico City"], "total_wish" : 1}
}

# Nesting a Dictionary in a List []
log_travel = [
    {
        "Country" : "Canada",
        "Cities_visited" : ["Toronto", "Quebec", "Montreal"], 
        "total_wish": 3
    },
    {
        "Country" : "United States",
        "Cities_visited" : ["New York", "Las Vegas", "Seattle"],
        "total_wish": 3
    },
    {
        "Country" : "Mexico",
        "Cities_visited" : ["Mexico City"],
        "total_wish" : 1
    }
]