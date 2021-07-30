names = input('Enter name(seperated by comma): ')
assignments = int(input('Enter assignment(seperated by comma):'))

grades = int(input('Enter grade(seperated by comma):'))
final_score = 2 * assignments + grades

print('Hi ' + names +'! This is a reminder that you have \
   assignments assignments left to \
        submit before you can graduate. Your current grade \
            is grades and can increase \
                to final_scoreRoss if you submit all \
                    assignments before the due date.')