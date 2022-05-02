# This code allows the user to decide the number of letters, numbers, and symbols that they would want in their random password
import random

alphabet = 'QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm'
num = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
symbols = '!$#*?'

num_letters = input('Enter the amount of letters you would want in your password: ')
num_numbers = input('Enter the amount of numbers you would want in your password: ')
num_symbols = input('Enter the amount of symbols you would want in your password: ')

# Sample() outputs a specific amount of random items from a list, tuple, string, or set
rand_letters = random.sample(alphabet, int(num_letters))
rand_nums = random.sample(num, int(num_numbers))
rand_symbol = random.sample(symbols, int(num_symbols))

random_password = rand_letters + rand_nums + rand_symbol
random.shuffle(random_password)

new_password = ''.join(str(n) for n in random_password)

print('Here is your random password: ' + new_password)

#------------------------------------------------------------------------------------
# This code just completely gives a random password
import random

alphabet = 'QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm'
num = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
symbols = '!$#*?'

num_letters = random.randint(0, len(alphabet))
num_numbers = random.randint(0, len(num))
num_symbols = random.randint(0, len(symbols))

# Sample() outputs a specific amount of random items from a list, tuple, string, or set
rand_letters = random.sample(alphabet, k=num_letters)
rand_nums = random.sample(num, k=num_numbers)
rand_symbol = random.sample(symbols, k=num_symbols)

random_password = rand_letters + rand_nums + rand_symbol
random.shuffle(random_password)

new_password = ''.join(str(n) for n in random_password)

print('Here is a random password: ' + new_password)
