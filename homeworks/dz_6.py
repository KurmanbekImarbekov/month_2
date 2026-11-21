class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"{self.earn()}! {self.superpower()}!"


class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return f"{self.live()}! {self.superpower()}!"


class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return f"{self.earn()}! {self.viral()}!"


glow = GlowStreamer()
viral = ViralCyborg()
donat = DonateMage()
print(GlowStreamer.mro())
print(ViralCyborg.mro())
print(DonateMage.mro())

print(glow.ultimate_content())
print(viral.ultimate_content())
print(donat.ultimate_content())

stars = [glow, viral, donat]

for star in stars:
    print(star.live())


"""
Персонаж	       Родители	            Чей live() сработает

GlowStreamer	Streamer, Mutant	    Streamer

ViralCyborg	    TikToker, Mutant	    TikToker

DonateMage	   Streamer, TikToker	    Streamer

"""