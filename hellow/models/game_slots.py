# coding: utf8
db.define_table('game_slots',
    Field('game', 'reference game'),
    Field('slot', 'reference slot'),format='%(game)s %(slot)s')
