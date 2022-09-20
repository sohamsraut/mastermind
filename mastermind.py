#MastermindV2.1
import random
print('Welcome to Mastermind!!!')
print('In this game, you will have to find out a random number.')
print('After each guess, the number of exact numbers used and the number of correct positions will be shown.')
print('Your guess must be a 4 digit number without any digit repeated.')
print('You have 12 tries to guess the number correctly.')
print('All the best!')
ans = 'y'
points=0
while (ans.lower()  == 'y'):
    no = 1
    r = 1
    found = e = p = 0
    while True:
        rep = 0
        fix = random.randint(1000,9999)
        sfix = str(fix)
        for i in sfix:
            if (sfix.count(i) > 1):
                rep = 1
        if rep == 0:
            break
    while (found == 0 and no <= 12):
        p = e = 0
        r = 1
        n = int(input('\nGuess :'))
        s = str(n)
        for i in s:
            if (s.count(i) > 1):
                print('No number should be repeated')
                r = 0
                break
            continue
        if (n == fix):
            print('Correct!')
            print('You have won the game in', no, 'tries!!')
            points += 5
            found = 1
        elif (len(s) != 4):
            print('Invalid guess: Guess must be a 4 digit number')
            continue
        elif (no == 12):
            print('Game Over: Number of chances exceeded')
            print('The answer is :', fix)
            break
        elif (found == 0 and r == 1):
            for i in range(0, 4):
                if sfix[i] == s[i]:
                    p += 1
            print('Correct positions: ', p)
            for i in s:
                if i in sfix:
                    e += 1
            print('Exact numbers used: ', e)
            no += 1
    print('\nTotal points: ', points)
    ans = input('Play again?(Enter y/n): ')
else:
    print('\nThank you for playing Mastermind!')
