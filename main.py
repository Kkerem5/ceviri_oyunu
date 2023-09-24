import random
import time

dogru_sayısı = 0
eng_words = ['Hi', 'Bye', 'Task', 'Programm']
tr_words = ['Merhaba', 'Hoşça kalın', 'Görev', 'Program']
kelimeler = {'Hi':'Merhaba','Bye':'Hoşca kalın','Task':'Görev','Programm':'Program'}
score = 0
soru_sayısı = 0
while True:
    mode = input("Bir mod seçin: Yeni kelimeler eklemek için 0, çeviri yapmak için 1: \n")
    while mode not in ['0', '1']:
        mode = input("Geçersiz sembol! Sadece 0 veya 1 yazın (Yeni kelimeler eklemek için 0, çeviri yapmak için 1, çıkmak için 9) \n")

    if mode == "1":
        print("Belirli bir süre içinde ne kadar çok kelime çevirebilirsiniz?")
        total_questions = 10  
        time_limit = 15 
        start_time = time.time()  

        while time.time() - start_time < time_limit and total_questions > 0:
            random_key = random.choice(list(kelimeler.keys()))
            print("Tercümesi bu şekilde olmalı: " + random_key)
            soru_sayısı += 1
            user_input = input()
            if user_input == kelimeler[random_key]:
                print("Harika!!!")
                dogru_sayısı += 1
                score += 1
            else:
                print(f"Bir yanlışlık var... Doğru kelime - {kelimeler[random_key]}")
            total_questions -= 1

        print(f"Süre doldu! Toplam doğru sayısı: {dogru_sayısı}/{soru_sayısı}")
    elif mode == '9':
        break
    else:
        word = input("İngilizce bir kelime yazın: ")
        translate = input("Kelimenin tercümesini yazın: ")
        if len(word) > 0 and len(translate) > 0:
            eng_words.append(word)
            tr_words.append(translate)
            print("Kelime başarıyla eklendi!")
