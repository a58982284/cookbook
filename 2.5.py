'''
text = 'yeah, but no, but yeah, but no, but yeah'
a = text.replace('yeah', 'yep')
print (a)
'''

from calendar import month_abbr
def change_data(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))