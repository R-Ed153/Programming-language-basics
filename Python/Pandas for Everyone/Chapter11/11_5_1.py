import re

tele_num = "1234567890"

m =  re.match(pattern="\d\d\d\d\d\d\d",string=tele_num)
print(type(m))
print(m)

tele_num_space_paren_dash = "(123) 456-7890"
p = "\(?\d{3}\)?\s?\d{3}\s?-?\d{4}"
m_2 = re.match(pattern=p,string = tele_num_space_paren_dash)
print(m_2.span())

cnty_tele_num_space_paren_dash = "+1 (123) 456-7890"
p_3 = "\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}"
m_3 = re.match(pattern=p_3,string=cnty_tele_num_space_paren_dash)
print(m_3.group())