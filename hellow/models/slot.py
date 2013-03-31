# coding: utf8
#db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
db.define_table(
    'slot',
    Field('odds', 'integer'), format='SLOT %(id)s')
