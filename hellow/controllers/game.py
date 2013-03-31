# coding: utf8
# try something like
import random
import datetime


def show():
    id = request.args[0]
    game = db.game(id)
    auth_user = (game.auth_user)
    
    query=((db.game.id==db.game_slots.game)&(db.slot.id==db.game_slots.slot))
    #game_and_slots=(db.game.id==db.game_slots.game)&(db.slot.id==db.game_slots.slot)
    rows = db(query).select(db.slot.id, db.slot.odds)
    
    otherForm = form_from_factory(rows, game, id)
    return dict(name=auth_user.first_name.capitalize() + " " + auth_user.last_name.capitalize(), balance = game.balance, slots = rows, gameid = id, otherForm=otherForm)
    
def form_from_factory(rows , game, id):
    game_and_slots=db((db.game_slots.game == id)&(db.slot.id==db.game_slots.slot))
    otherForm = SQLFORM.factory(
        Field('bet', requires=IS_NOT_EMPTY()),
        Field('slot', requires=IS_IN_DB(game_and_slots, 'slot.id'), widget=SQLFORM.widgets.radio.widget))
   
    if otherForm.process().accepted:
        mybet = int(otherForm.vars.bet)
        currentBalance =  int(game.balance)
        remainingBalance = calcWinnings(int(otherForm.vars.slot), mybet, currentBalance)
        won = isWinner(currentBalance, remainingBalance)
        game.update_record(balance=str(remainingBalance))
        db.user_action.insert(game = game, auth_user = game.auth_user, slot = otherForm.vars.slot, bet = mybet, winnings = remainingBalance, won = won, odds = db.slot(otherForm.vars.slot).odds, event_timedatetime = datetime.datetime.now())
    elif otherForm.errors:
        response.flash = 'form has errors'
    return otherForm
    
def calcWinnings(odds, bet, balance):
    if(random.randint(1, 10) > odds):
        response.flash = 'You won' 
        return bet + balance
    else:
        response.flash = 'You lost'
        return balance - bet
def isWinner(cb, rb):
    if (rb > cb):
        return "yes"
    else: return "no"
