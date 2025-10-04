from django.shortcuts import render
from django.http import HttpResponse

songi_yangiliklar =  [
    {
        "title": "Python Backend Dasturlashga Kirish",
        "date": "15 Mart, 2024",
        "content": "Python – boshlovchilar uchun eng qulay va kuchli backend tillaridan biridir. Avvaliga HTTP, server va API nima ekanini tushunib oling. Keyin Flask yoki FastAPI kabi engil framework bilan kichik REST API yozib ko‘ring. Har kuni biror kichik endpoint yozish – o‘rganishni tezlashtiradi."
    },
    {
        "title": "Nega API Muhim?",
        "date": "10 Mart, 2024",
        "content": "API – backendning yuragi. U frontend bilan muloqot qiladi, ma’lumotlarni yuboradi va qaytaradi. Agar yaxshi API qursangiz, frontendchilar sizni qahramondek ko‘radi. Maslahat: Postman yoki Thunder Client’da API’laringizni test qilib turing – bu ishlab chiqarishda xatolarni kamaytiradi."
    },
    {
        "title": "Birinchi Backend Loyihangiz",
        "date": "5 Mart, 2024",
        "content": "Birinchi backend loyihangizni yaratish – haqiqiy dasturchilikni his qilishning eng yaxshi usuli. Masalan, oddiy “To-do list” REST API qiling: foydalanuvchi yaratadi, o‘chiradi, yangilaydi. Kodni GitHub’ga yuklashni unutmang – portfolio uchun juda foydali!"
    }
]


def main(request):
    data = {'posts': songi_yangiliklar}
    return render(request, 'blog/home.html', data)


def blogs(request):
    return render(request, 'blog/blogs.html')


def about(request):
    return render(request, 'blog/about.html')