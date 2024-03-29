############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name= name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    Musk = MelonType('musk',1988,'green', True, True,'muskMelon')
    Musk.add_pairing('mint')

    Casaba = MelonType('cas',2003,'orange',True,False,'Casaba')
    Casaba.add_pairing('strawberries')
    Casaba.add_pairing('mint')

    Crenshaw = MelonType('cren',1996,'green',True,False,'Crenshaw')
    Crenshaw.add_pairing('proscuitto')


    Yellow_Watermelon = MelonType('yw',2013,'yellow',True,True,'Yellow Watermelon')
    Yellow_Watermelon.add_pairing('ice cream')

    all_melon_types.append(Musk)
    all_melon_types.append(Casaba)
    all_melon_types.append(Crenshaw)
    all_melon_types.append(Yellow_Watermelon)




    return all_melon_types



# def print_pairing_info(melon_types):
#     """Prints information about each melon type's pairings."""

#     # Fill in the rest
#     for melon in melon_types:

#         print(f"{melon.name} pairs with")
#         for pairing in melon.pairings:
#           print(f"-{pairing}") 

# melonT = make_melon_types()
# print_pairing_info(melonT)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    
    mon_dict = {}
    for melon in melon_types:
         mon_dict[melon.code] = melon

    return mon_dict
melonT = make_melon_types()
print (make_melon_type_lookup(melonT))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    """Initialize a melon."""
    def __init__(self, melon_type, shape_rating, color_rating, number_of_harvest, name):

    
        self.type = melon_type
        self.rating = shape_rating
        self.number_of_harvest = number_of_harvest
        self.name = name



    def is_sellable(self):
        if (self.rating > 5) and  (self.color_rating > 5) and (self.number_of_harvest != 3):
            return True

        else:
            return False


melon1 = Melon('yw',8,7,2,'Sheila')

print(melon1)
t = melon1.is_sellable
print('t is', t)

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



