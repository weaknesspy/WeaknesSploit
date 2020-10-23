# Inteligent Wordlist Generator
#
# By: WeaknesSPY
# WeaknesSPY Wordlist Generator
# Version: 2.0
#
#
##################

import itertools


ban = '''

                                                    '''

print('\n------------------\n\n WeaknesSPY \033[32m2.0\033[m | WORDGENERATOR\n\n~ by: Weaknesspy\n\n------------------\n')

scale = input('\033[36m[!] provide a size scale [eg: "1 to 10000" = 1:10000] : ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])

use_nouse = str(input("\n\033[36m[?] Do you want to enter personal data ? [y/N]: "))
if use_nouse == 'y':
        first_name = str(input("\n\033[36m[*] Fist Name: "))
        last_name = str(input("\n\033[36m[*] Last Name: "))
        birthday = str(input("\n\033[36m[*] Birthday: "))
        month = str(input("\n\033[36m[*] Month: "))
        year = str(input("\n\033[36m[*] Year: "))
        chrs = first_name + last_name + birthday + month + year
else:
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        pass

chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'

file_name = input('\n\033[36m[!] Insert a name for your wordlist file: ')
arq = open(file_name, 'w')
if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
        chrs = ''.join([chrs, chrs_up])
if input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y':
        chrs = ''.join([chrs, chrs_specials])
if input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y':
        chrs = ''.join([chrs, chrs_numerics])

for i in range(start, final+1):
        for j in itertools.product(chrs, repeat=i):
                temp = ''.join(j)
                print(temp)
                arq.write(temp + '\n')
arq.close()
