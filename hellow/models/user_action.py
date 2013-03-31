# coding: utf8
db.define_table('user_action',
    Field('game', 'reference game'),
    Field('auth_user', 'reference auth_user'),
    Field('slot', 'reference slot'),
    Field('bet', 'integer'),
    Field('winnings', 'integer'),
    Field('won'),
    Field('odds', 'integer'),
    Field('event_time' 'datetime'))
