import re

str = 'edu_dup_accId_his_HIT1143220116_1457233315661'
print(re.sub(r'edu_dup_accId_his_','', str))
