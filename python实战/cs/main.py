#!/usr/bin/env python
# -*- coding:utf-8 -*-

from cs.grenade import Grenade
from cs.gun import Gun
from cs.bulletbox import Bulletbox
from cs.gengster import Gengster
from cs.profector import Profector
# 参数：枪，手榴弹，血（默认100，且上限为100）

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