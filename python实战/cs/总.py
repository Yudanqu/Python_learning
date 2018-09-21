#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Bulletbox(object):
    def __init__(self,bulletcount):
        self.bulletcount = bulletcount


class Gun(object):
    def __init__(self,bulletbox):
        self.bulletbox = bulletbox

    def shoot(self):
        if self.bulletbox.bulletcount == 0:
            print('没子弹了')
        else:
            self.bulletbox.bulletcount -= 1
            print(str(self) + '开一枪，还剩%d颗子弹' % (self.bulletbox.bulletcount))


class Grenade(object):
    def __init__(self,grenadecount):
        self.grenadecount = grenadecount

    def damage(self):
        if self.grenadecount == 0:
            print('手雷没有了')
        else:
            self.grenadecount -= 1
            print(str(self) + "轰他一炮，手雷还剩%d颗" % (self.grenadecount))


class Person(object):
    def __init__(self, gun, grenade, blood):
        self.gun = gun
        self.grenade = grenade
        self.blood = blood

    def fire(self, person):
        person.blood -= 5
        self.gun.shoot()
        print(str(person) + "血量减少5，剩余" + str(person.blood) )

    def fire2(self, person):
        person.blood -= 10
        self.grenade.damage()
        print(str(person) + "血量减少10，剩余" + str(person.blood) )

    def fillbullet(self):
        self.gun.bulletbox.bulletcount += 10

    def fillblood(self,num):
        self.blood += num
        if self.blood > 100:
            self.blood = 100
        print(str(self) + "补血后血量：" + str(self.blood))


class Profector(Person):
    def __init__(self, gun, grenade, blood = 100):
        super(Profector,self).__init__(gun, grenade, blood)


class Gengster(Person):
    def __init__(self, gun, grenade, blood=100):
        super(Gengster, self).__init__(gun, grenade, blood)


bulletbox = Bulletbox(10)
gun = Gun(bulletbox)
grenade = Grenade(20)

good1 = Profector(gun,grenade)
good2 = Profector(gun,grenade)
bad1 = Gengster(gun,grenade)
bad2 = Gengster(gun,grenade)

print("好人1开枪打坏人1和2")
good1.fire(bad1)
good1.fire(bad2)
print("好人2开枪打坏人1和2")
good2.fire(bad1)
good2.fire(bad2)
print("坏人1炸好人1和2")
bad1.fire2(good1)
bad1.fire2(good2)
print("坏人2炸好人1和2")
bad2.fire2(good1)
bad2.fire2(good2)
print("坏人1补血3个")
bad1.fillblood(3)