from logpy import *
from logpy.core import lall

# Declare the variable
people = var()

# Define the rules
rules = lall(
    # There are 5 people
    (eq, (var(), var(), var(), var(), var()), people),

    # Норвежец живет в первом доме
    (membero, ('норвежец', var(), var(), var(), var()), people),

    # Англичанин живет в красном доме
    (membero, ('англичанин', 'красный', var(), var(), var()), people),
    # Зеленый дом находится левее белого!?!?
    # Датчанин пьет чай
    (membero, ('датчанин', var(), var(), var(), 'чай'), people),

    # Tот, кто курит Rothmans, живет рядом с тем, кто
    # выращивает кошек
    (membero, (var(), var(), 'Rothmans', var(), var()), people),

    # Тот, кто живет в желтом доме, курит Dunhill
    (membero, (var(), 'желтый', 'Dunhill', 'var()', var()), people),

    # Немец курит Marlboro
    (membero, ('Немец', var(), 'Marlboro', var(), var()), people),

    # Тот, кто живет в центре, пьет молоко
    (membero, (var(), var(), var(), var(), 'молоко'), people),

    # Сосед того, кто курит Rothmans, пьет воду
    (membero, (var(), var(), var(), var(), 'воду'), people),

    # Тот, кто курит Pall Mall, выращивает птиц
    (membero, (var(), var(), 'Pall Mall', 'птиц', var()), people),

    # Швед выращивает собак
    (membero, ('швед', var(), var(), 'собака', var()), people),

     # Норвежец живет рядом с синим домом

      # Тот, кто выращивает лошадей, живет в синем доме
    (membero, (var(), 'синий', var(), 'лошадь', var()), people),

       # Тот, кто курит Philip Morris, пьет пиво.
    (membero, (var(), var(), ' Philip Morris', var(), 'пиво'), people),

       # В зеленом доме пьют кофе
    (membero, (var(), 'зеленый', var(), var(), 'кофе'), people),

       # а кто ж выращивает рыб?
    (membero, (var(), var(), var(), 'рыбки', var()), people)
)

# Run the solver
solutions = run(0, people, rules)

# Extract the output
output = [house for house in solutions[0] if 'рыбки' in house][0][0]

# Print the output
print('\n' + output + ' is the owner of the рыбки')
print('\nHere are all the details:')
attribs = ['Нацииональность', 'Цвет_дома', 'марка_сигарет', 'животное', 'напиток']
print('\n' + '\t\t'.join(attribs))
print('=' * 57)
for item in solutions[0]:
    print('')
    print('\t\t'.join([str(x) for x in item]))

