'''
Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False


'''
import datetime

entered_code = 123
correct_code = 123
current_date = 162

expiration_date = 5433

def check_coupon(entered_code, correct_code, current_date, expiration_date):



    pass

x = datetime.datetime(2020, 5, 17)

print(x.strftime("%B"))