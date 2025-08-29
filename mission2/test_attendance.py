import pytest

from attendance2 import Club, Member


@pytest.fixture
def club():
    club = Club()
    return club


def test_club_instance(club):
    assert isinstance(club, Club)


def test_member_attend_action():
    member = Member('james', 1)
    for i in range(10):
        member.attend('wednesday')
    assert member.weekdays['wednesday'] == 10


def test_make_members(club):
    club.membermanager.get_member('james')
    club.membermanager.get_member('james2')
    assert len(club.members) == 2


def test_make_member_once(club):
    club.membermanager.get_member('james')
    club.membermanager.get_member('james')
    club.membermanager.get_member('james')
    assert len(club.members) == 1




def test_give_attend_score(club):
    member = club.membermanager.get_member('james')
    club.give_attend_point(member, 'monday')
    club.give_attend_point(member, 'wednesday')
    club.give_attend_point(member, 'sunday')
    assert member.point == 6


def test_give_bonus_point(club):
    member = club.membermanager.get_member('james')
    for i in range(10):
        member.attend('monday')
        member.attend('wednesday')
        member.attend('sunday')
    club.give_bonus_points_for_closing()
    assert member.point == 20


def test_get_silver_medal(club):
    member = club.membermanager.get_member('james')
    for i in range(31):
        member.attend('monday')
        club.give_attend_point(member, 'monday')
    club.give_bonus_points_for_closing()
    assert member.medal == "SILVER"


def test_get_silver_gold(club):
    member = club.membermanager.get_member('james')
    for i in range(50):
        member.attend('monday')
        club.give_attend_point(member, 'monday')
    club.give_bonus_points_for_closing()
    assert member.medal == "GOLD"


def test_kickout_member(capsys):
    club = Club()
    james = club.membermanager.get_member('james')
    michael = club.membermanager.get_member('michael')
    james.attend('monday')
    michael.attend('sunday')
    club.announce_kicked_out_member()
    out, err = capsys.readouterr()
    assert "james" in out
    assert "michael" not in out


def test_announce_all_members_score_medal(capsys):
    club = Club()
    club.membermanager.get_member('james')
    club.announce_all_members_score_medal()
    out, err = capsys.readouterr()
    assert "NAME : james, POINT : 0, GRADE : NORMAL\n" == out
