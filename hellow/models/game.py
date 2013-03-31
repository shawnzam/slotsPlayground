# coding: utf8
#db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])

db.define_table('game',
    Field('auth_user', 'reference auth_user'),
    Field('balance', 'integer'))
