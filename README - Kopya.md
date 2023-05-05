# GPT-3 Tabanlı Kişiselleştirilmiş Chatbot

Bu, OpenAI'nin GPT-3 API'sini kullanarak bir chatbot uygulamasıdır. Flask web uygulaması, bir web sayfası aracılığıyla kullanıcıdan gelen mesajları OpenAI API'sine gönderir ve API'den gelen yanıtı mesaj baloncuğunda gösterir.

## Kullanım

Bu uygulamayı kullanmak için önce `ayarlar.cfg` dosyasında OpenAI API anahtarınızı ayarlamanız gerekir. Ayrıca `openai_settings` sözlüğünü, GPT-3 API'si isteklerinde kullanmak istediğiniz ayarlarla özelleştirebilirsiniz.

Uygulamayı başlatmak için, komut satırında şu komutu çalıştırın:

```
python app.py
```

Uygulama başarıyla başlatıldıktan sonra, tarayıcınızda `http://localhost:3131` adresini açın ve chatbot'la konuşmaya başlayabilirsiniz.

## Uyarılar

- Bu uygulamayı kullanmak için OpenAI API üyeliğiniz olması gerekmektedir.
- Bu uygulama, kullanıcının gönderdiği mesajları kaydeden bir log dosyası oluşturur. Kullanıcı gizliliği için bu log dosyası güvenli bir şekilde saklanmalıdır.
- Bu uygulamanın yalnızca test amaçlı kullanılması önerilir. Gerçek dünya uygulamalarında kullanılacak chatbot'lar, daha kapsamlı bir eğitim ve doğrulama sürecinden geçmelidir.

## İletişim

Bu uygulamayla ilgili herhangi bir sorunuz veya geri bildiriminiz varsa, lütfen bana ulaşın.
```
discord: mertcan#0001
instagram: mertcvn.jpg

```