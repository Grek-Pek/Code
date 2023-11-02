review_text = input('Введите отзыв: ').lower()
pos_words = ['весело', 'увлекательно', 'развлечения']
positive_reviews = 0
for word in pos_words:
    if word in review_text:
        positive_reviews += 1
print('Результат анализа:', positive_reviews)






















