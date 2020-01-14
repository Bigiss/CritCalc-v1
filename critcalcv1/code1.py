#######################################################################################################################
# This program calculates the critical hit chance of players in EQ Classless custom server.
# Written by Dingus, Jan 2020
#######################################################################################################################

#######################################################################################################################
# These are variables in use
#######################################################################################################################
stren = 10
dext = 10
agil = 10
stam = 10
intel = 10
wisd = 10
char = 10
mainstat = 0
mainstatchoice = 0

#######################################################################################################################
# These variables are not in use, yet...

# stattotal = stren + dext + agil + stam + intel + wisd + char
# fastcast = 0
# sixtycrit = 0

# Here is the formulas we are using. These were confirmed by Ailia, a Classless developer, on Discord on Jan 9th, 2020.
# critrate = dext / (1.33 * mainstat + dext + agil + (0.9 * char))

# SECTION - This is the welcome and user input section
#######################################################################################################################

print('Welcome to D4C: Dinguses Crit Chance Calculator for Classless.')

print('This tool will tell you what your chance to hit critically is. Please type your primary stat:')

#######################################################################################################################
# Offers users a list of input options
#######################################################################################################################

mainstatlist = ["strength", "intelligence", "wisdom"]

print(mainstatlist[0:4])
mainstatchoice = input()

#######################################################################################################################
# If 'Strength' is input, asks users to input their STR value, and sets that as the Main Stat for the critical hit formula
#######################################################################################################################

if mainstatchoice == (str('strength')):
    print('Your main stat is Strength. You are so stronk.')
    print('Please enter your Strength total')
    stren = input()
    mainstat = stren

#######################################################################################################################
# If 'Intelligence' is input, asks users to input their INT value, and sets that as the Main Stat for the critical hit formula
#######################################################################################################################

elif mainstatchoice == (str('intelligence')):
    print('Your main stat is Intelligence. You should have written your own calculator.')
    print('Please enter your Intelligence total')
    intel = input()
    mainstat = intel

#######################################################################################################################
# If 'Wisdom' is input, asks users to input their WIS value, and sets that as the Main Stat for the critical hit formula
#######################################################################################################################

elif mainstatchoice == (str('wisdom')):
    print('Your main stat is Wisdom. Please get back to healing. Your group needs you.')
    print('Please enter your Wisdom total')
    wisd = input()
    mainstat = wisd

#######################################################################################################################
# Unknown inputs break the program currently
#######################################################################################################################

else:
    print('Invalid input. Please enter \'Strength\' \'Intelligence\' or \'Wisdom\'')

#######################################################################################################################
# Asks the user to input their DEX, AGI, and CHA stat counts, which are required for the critical hit formula
#######################################################################################################################

print('I will also need to know your Dexterity, Agility, and Charisma values.')
print('Please enter your Dexterity total')
dext = input()
print('Your Dexterity is ' + str(dext))

print('Please enter your Agility total')
agil = input()

print('Please enter yout Charisma total')
char = input()

#######################################################################################################################
# Shows the user their stat distribution as used by the critical hit formula
#######################################################################################################################

print('You have ' + str(stren) + ' Strength.')
print('You have ' + str(dext) + ' Dexterity.')
print('You have ' + str(agil) + ' Agility.')
print('You have ' + str(char) + ' Charisma.')
print('Your main stat, ' + str(mainstatchoice) + ', is ' + str(mainstat))

#######################################################################################################################
# Computes the critical hit formula
#######################################################################################################################

critrate = float(dext) / (1.33 * float(mainstat) + float(dext) + float(agil) + (0.9 * float(char)))

#######################################################################################################################
# Sets the critical hit rate as a percentage
#######################################################################################################################

critpercent = critrate * 100

#######################################################################################################################
# Tells the user their given critical hit chance using their input main stat and stat distribution
#######################################################################################################################

print('Given your current stat allocation, your chance to strike critically with skills, spells and abilities that use ' + str(mainstatchoice) + ' for scaling is:')
print(str(critpercent))
