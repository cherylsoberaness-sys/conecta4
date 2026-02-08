
import pytest
from conecta4.player import Player, HumanPlayer
from conecta4.match import Match
"""
cucu = Player ("Prof. Cucu")
otto = Player("Dr Octopus")
"""
@pytest.fixture
def players():
    return HumanPlayer("Prof. Cucu"), Player("Dr Octopus")
    
def test_different_players_have_different_chars(players):
    cucu, otto = players
    t = Match(cucu, otto)
    assert cucu.char != otto.char

def test_no_player_with_none_char(players):
    cucu, otto = players
    t = Match(cucu, otto)
    assert cucu.char != None
    assert otto.char != None


def test_next_player_is_round_robbin(players):
    #"round robbin" -> especie de lista circular 
    cucu, otto = players
    t = Match(otto, cucu)
    p1 = t.next_player
    p2 = t.next_player
    assert p1 != p2

def test_players_are_opponents(players):
    cucu, otto = players
    t = Match(otto, cucu)
    x = t.get_player("x")
    o = t.get_player("o")
    assert o.opponent == x
    assert x.opponent == o
    