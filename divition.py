#احسب كم  ساعهودقيقه او ثانيه في عدد الثواني الذي يدخلها المستخدم
#عدد الثواني الذي  يدخلها المستخدم
total_moments = int(input('Number of moments :  '))
#احسب عدد الساعات
hours = total_moments // 3600
#احسب عدد الدقائق
menits = total_moments  //60 %60
#احسب عدد الثواني
moments = total_moments % 60


print(f"You have {hours} Hours , and {menits} Menits and {moments} Moments")
