#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Card(object):
    def __init__(self, cardId, cardPasswd, cardMoney):
        self.cardId = cardId
        self.cardPasswd = cardPasswd
        self.cardMony = cardMoney
        self.cardLock = False