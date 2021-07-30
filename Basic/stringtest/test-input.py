names = input('Enter name(seperated by comma): ')
assignments = input('Enter assignment(seperated by comma):')

grades = input('Enter grade(seperated by comma):')
final_score = 2 * assignments + grades
for student in range names.len(),
print('Hi {names}! This is a reminder that you have \
{assignments} assignments left to \
submit before you can graduate. Your current grade \
is {grades} and can increase \
to {final_score} if you submit all \
assignments before the due \
date.'.format(names=names,assignments=assignments,grades=grades,final_score=final_score))