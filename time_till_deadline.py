import datetime as dt

user_input = input("enter your goal with a deadline separated by colon\n->")
input_list = user_input.split(":")

goal= input_list[0]
deadline = input_list[1]

deadline_date = (dt.datetime.strptime(deadline,"%m.%d.%Y"))
today_date = dt.datetime.today()
time_till = deadline_date - today_date
print(f'Dear user, time remaining for your goal: "{goal}" is {time_till.days} days')
