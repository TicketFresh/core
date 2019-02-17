from utilities.classes import *
import random
import uuid
import argparse
import lorem




def random_first_name():
    """Picks a random first name from predefined list, and returns it as a string"""
    names = ["Nicola","Synthia","Hank","Antonietta","Melda","Aileen","Burton","Inge","Kurtis","Robbyn","Jerrold","Gena","Micha","Conchita","Hobert","Elissa","Towanda","Rubin",
    "Elouise","Williams","Lurlene","Lacresha","Elodia","Calvin","Richie","Agnus","Drew","Sona","Fred", "Kitty", "Elon"]
    return random.choice(names)


def random_last_name():
    """Picks a random last name from predefined list, and returns it as a string"""
    names = ["Racine","Mershon","Carboni","Chambers","Kimmer","Agron","Hemingway","Fort","Popham","Hutto","Berrios","Moniz","Erb","Holtzman","Cawley","Hogge","Merideth","Landis",
    "Chance","Losee","Merrihew","Mackey","Fischbach", "Caouette","Esterly","Collman","Wolfe","Orme","Whelan", "Royals"]
    return random.choice(names)

def random_full_name():
    return "{} {}".format(random_first_name(), random_last_name())

def random_phone_number():
    """Picks a random phone number from predefined list, and returns it as a string"""
    phone_numbers = ["(403)251-1234 ", "(403)679-1234","(403)382-1234","(403)765-1234", "(403)257-3124"]
    return random.choice(phone_numbers)

def random_company():
    """Picks a random company from predefined list, and returns it as a string"""
    companies = ["Driive","Google","Rosignol","Nike","Addidas","Audi","Tesla","Enmax","the futur","Coca-Cola","Mcdonalds","Taco Time","Blind Studios","Blizzard","Electronic Arts",
    "Apple","American Eagle","Bootlegger","Walmart","Helly Hansen","University of Calgary","Bob's Burgers","Microsoft","North Face","Samsung","Sandisk","Intel","AMD","ASUS", "Gigabyte"]
    return random.choice(companies)

def generate_user(mode="cli"):
    return user(random_first_name(), random_last_name(), "Randomly Generated")


def generate_ticket(mode="cli"):
    return ticket(lorem.sentence(), random_full_name(), random_company(), lorem.sentence(), "Randomly Generated")


# Static classes for temporary testing
test_user_logged_in = generate_user()
test_user_logged_out = user("Login", "", "")
test_company = company(random_company())
test_ticket = generate_ticket()
###############################################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create random information to test with")

    parser.add_argument("-u", "--user", dest='random_user', action='store_const', const=generate_user(),
    help='Generates a random user and prints the contents to stdout')

    parser.add_argument("-t", "--ticket", dest='random_ticket', action='store_const', const=generate_ticket(),
    help='Generates a random ticket and prints the contents to stdout')

    args = parser.parse_args()

    if args.random_user:
        print(args.random_user)

    elif args.random_ticket:
        print(args.random_ticket)


    
