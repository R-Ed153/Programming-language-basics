from datetime import datetime

now = datetime.now()
print(f"Last time this chapter was rendered for print: {now}")

t2 = datetime(1970,1,1)
print(t2)
print(t2-now)