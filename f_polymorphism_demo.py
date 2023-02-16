# This program demonstrates polymorphism.

import f_animals as animals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()
    


    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')

    sound(mammal)
    sound(dog)
    sound(cat)
    #mammal.show_species()
    #mammal.make_sound()
    #print()

    #dog.show_species()
    #dog.make_sound()

    #print()

    #cat.show_species()
    #cat.make_sound()

def sound(animal):
    if isinstance(animal, amimals.Mammal):

        animal.show_species()
        animal.make_sound()
    else:
        print(f'{animal} is not a mammal!')
    print()
    
# Call the main function.
main()
