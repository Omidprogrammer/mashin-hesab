# input_module.py
def get_number(prompt):
    while True:
        num_str = input(prompt)
        # بررسی طول عدد
        if len(num_str) > 10:
            print("❌ خطا: طول عدد نمی‌تواند بیش از 10 رقم باشد.")
            continue
        # بررسی اینکه فقط عدد باشد
        if not num_str.isdigit():
            print("❌ خطا: لطفاً فقط عدد صحیح وارد کنید.")
            continue
        # تبدیل به عدد صحیح و بررسی مثبت بودن
        num = int(num_str)
        if num < 0:
            print("❌ خطا: عدد باید مثبت باشد.")
            continue
        return num

def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("عملگر مورد نظر خود را وارد کنید (+, -, *, /): ")
        if op not in valid_operators:
            print("❌ خطا: لطفاً یکی از عملگرهای معتبر را وارد کنید.")
            continue
        return op

