"""
[ADIM 5.2]

Atomik istek sayacı kontrolü (SELECT FOR UPDATE).

Bunu önce küçük bir izole script ile dene: "aynı anda iki istek
gelirse ne olur" senaryosunu simüle et (örn. asyncio ile iki paralel
çağrı), sonra buraya entegre et.
"""
