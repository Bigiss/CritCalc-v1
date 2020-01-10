#adding this to try github commit

stren=10

dext=10

agil=10

stam=10

intel=10

wisd=10

char=10

mainstat=0

mainstatchoice=0

stattotal=stren+dext+agil+stam+intel+wisd+char

#critrate = dext / ( 1.33 * mainstat + dext + agil + ( 0.9 * char ) )

#critpercent=critrate * 100

fastcast=0

sixtycrit=0

print ('Welcome to D4C: Dinguses Crit Chance Calculator for Classless.')

mainstatlist= ["Strength", "Intelligence", "Wisdom"]

print ('This tool will tell you what your chance to hit critically is. Please choose your primary stat:')
print (mainstatlist[0:4])
mainstatchoice=input()
if mainstatchoice==(str('strength')):
    print ('Your main stat is Strength. You are so stronk.')
    print ('Please enter your Strength value')
    stren=input()
    mainstat=stren

elif mainstatchoice==(str('intelligence')):
    print ('Your main stat is Intelligence. You should have written your own calculator.')
    print ('Please enter your Intelligence  value')
    intel=input()
    mainstat=intel
        
elif mainstatchoice==(str('wisdom')):
    print ('Your main stat is Wisdom. Please get back to healing. Your group needs you.')
    print ('Please enter your Wisdom value')
    wiinput()
    mainstat=wisd

else:
    print ('You have broken this program. Please run it again.')

print ('I will also need to know your Dexterirty, Agility, and Charisma values. Please enter your Dexterity')
dext=input()
print ('Your Dexterity is ' + str(dext))

print('Please enter your Agility value?')
agil=input()
print ('Your Agility is ' + str(agil))

print('What is your Charisma?')
char=input()
print ('Your Charisma is ' + str(char))

print ('You have ' + str(stren) + ' Strength.')
print ('You have ' + str(dext) + ' Dexterity.')
print ('You have ' + str(agil) + ' Agility.')
print ('You have ' + str(char) + ' Charisma.')
print ('Your main stat, ' + str(mainstatchoice) + ', is ' + str(mainstat))

critrate = float ( dext ) / ( 1.33 * float ( mainstat ) + float ( dext ) + float ( agil ) + ( 0.9 * float( char ) ) )

critpercent=critrate * 100

print('Given your current stat allocation, your chance to strike critically with skill, spells and abilities using your main stat is ' + str(critpercent))
