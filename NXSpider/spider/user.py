#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by Lipson on 2018/4/25.
# email to LipsonChan@yahoo.com
#
from NXSpider.model.mongo_model import UserModel
from NXSpider.spider.base_driver import Music163Obj


class User(Music163Obj):
    __model_name__ = UserModel
    __model__rfilter__ = {
        'userId',

        # garbage properties
        'avatarImgId',
        'backgroundImgId',
        'avatarImgIdStr',
        'backgroundImgIdStr',
        'avatarImgId_str',
    }
