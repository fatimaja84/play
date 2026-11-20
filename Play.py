import random

print("================================")
print("     بازی سنگ، کاغذ، قیچی")
print("================================")

name = input("اسم بازیکن را وارد کنید: ").strip()

if name == "":
    name = "بازیکن"

player_score = 0
computer_score = 0
draw_count = 0
round_count = 0

choices = ["سنگ", "کاغذ", "قیچی"]

while True:
    print("\n========== منوی بازی ==========")
    print("1. سنگ")
    print("2. کاغذ")
    print("3. قیچی")
    print("4. نمایش جدول امتیازات")
    print("5. خروج از بازی")

    choice = input("انتخاب شما: ")

    if choice == "5":
        print("\n========== نتیجه نهایی ==========")
        print("تعداد دورهای بازی:", round_count)
        print("امتیاز", name + ":", player_score)
        print("امتیاز کامپیوتر:", computer_score)
        print("تعداد مساوی‌ها:", draw_count)

        if player_score > computer_score:
            print("برنده نهایی:", name)
        elif computer_score > player_score:
            print("برنده نهایی: کامپیوتر")
        elif round_count == 0:
            print("هنوز بازی‌ای انجام نشده است.")
        else:
            print("نتیجه نهایی مساوی شد!")

        print("ممنون که بازی کردی!")
        break

    elif choice == "4":
        print("\n========== جدول امتیازات ==========")
        print(name, ":", player_score)
        print("کامپیوتر:", computer_score)
        print("مساوی:", draw_count)
        print("تعداد دورها:", round_count)

    elif choice == "1" or choice == "2" or choice == "3":
        player = choices[int(choice) - 1]
        computer = random.choice(choices)
        round_count += 1

        print("\nانتخاب", name + ":", player)
        print("انتخاب کامپیوتر:", computer)

        if player == computer:
            print("این دور مساوی شد!")
            draw_count += 1
        elif (player == "سنگ" and computer == "قیچی") or \
             (player == "کاغذ" and computer == "سنگ") or \
             (player == "قیچی" and computer == "کاغذ"):
            print(name, "این دور را برد!")
            player_score += 1
        else:
            print("کامپیوتر این دور را برد!")
            computer_score += 1

        print("\n========== جدول امتیازات ==========")
        print(name, ":", player_score)
        print("کامپیوتر:", computer_score)
        print("مساوی:", draw_count)
        print("تعداد دورها:", round_count)

    else:
        print("انتخاب اشتباه است! لطفاً عدد 1 تا 5 را وارد کنید.")
