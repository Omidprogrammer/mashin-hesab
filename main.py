# main.py
from input_module import get_number, get_operator
from menu import show_menu

history = []

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("❌ خطا: تقسیم بر صفر امکان‌پذیر نیست.")
            return None
        return num1 / num2

def main():
    print("🔹 به ماشین‌حساب فارسی خوش آمدید!")
    while True:
        choice = show_menu()
        if choice == '1':  # انجام محاسبه جدید
            num1 = get_number("عدد اول را وارد کنید: ")
            operator = get_operator()
            num2 = get_number("عدد دوم را وارد کنید: ")
            result = calculate(num1, num2, operator)
            if result is not None:
                print(f"نتیجه: {num1} {operator} {num2} = {result}")
                history.append((num1, operator, num2, result))
        elif choice == '2':  # نمایش تاریخچه
            if not history:
                print("🛈 هیچ تاریخچه‌ای موجود نیست.")
            else:
                print("📜 تاریخچه:")
                for h in history:
                    print(f"{h[0]} {h[1]} {h[2]} = {h[3]}")
        elif choice == '3':  # پاک کردن تاریخچه
            history.clear()
            print("🗑️ تاریخچه پاک شد.")
        elif choice == '4':  # خروج
            print("👋 خداحافظ!")
            break
        else:
            print("❌ گزینه نامعتبر است.")

if __name__ == "__main__":
    main()
