# import matplotlib.pyplot as plt
# from collections import Counter

# # لیست داده‌ها
# # data = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# def get_Amounts(data):
# # شمارش تعداد تکرار هر عدد
#     counter = Counter(data)

#     # انتخاب مقادیر و تعداد تکرارها برای استفاده در نمودار
#     labels = list(counter.keys())
#     sizes = list(counter.values())

#     fig, (ax1, ax2) = plt.subplots(1, 2)


#     ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
#     ax1.set_title("Pie Chart")
#     # رسم نمودار
#     ax2.bar(labels, sizes)
#     ax2.set_xlabel("Amounts")
#     ax2.set_ylabel('number of users')
#     ax2.set_title("Bar Chart")

#     # ذخیره کردن نمودار به صورت فایل PNG
#     plt.savefig('bar_chart.png')

#     return 'bar_chart.png'

from collections import Counter
import matplotlib.pyplot as plt

# لیست لغات شما
# word_list = ["apple", "banana", "orange", "apple", "orange", "banana", "apple"]
def get_list_words(word_list):
# محاسبه تعداد تکرار هر لغت با استفاده از Counter
    word_count = Counter(word_list)

    # انتخاب 10 تکرار بیشترین تکرارها
    top_10 = word_count.most_common(10)

    # ایجاد داده‌های برای نمودار
    words = [item[0] for item in top_10]
    counts = [item[1] for item in top_10]

    # رسم نمودار
    plt.figure(figsize=(8, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('word')
    # plt.ylabel('تعداد تکرار')
    plt.ylabel("number of repetitions")
    # plt.title('نمودار ۱۰ تکرار بیشترین لغات')
    plt.title("giagram of top 10 most frequent words")
    plt.savefig('bar_chart.png')

    return 'bar_chart.png'
    # plt.show()

# get_list_words(["apple", "banana", "orange", "apple", "orange", "banana", "apple"])

