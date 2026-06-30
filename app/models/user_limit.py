"""
[ADIM 2.3] (opsiyonel - SaaS'tan kalan ama concurrency gösterimi için saklanabilir)

Günlük istek sayacı. rate_limit.py servisindeki
"SELECT FOR UPDATE" atomik kontrolünü burada uygulayacaksın.
Bu dosyayı tamamen silmek de mantıklı bir seçenek - portföy odaklı
gidiyorsan SaaS kredi mantığına gerek yok, ama "race condition'a
karşı nasıl korunulur" bilgisini göstermek istiyorsan basitleştirip tut.
"""
