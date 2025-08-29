BONUS_POINT = 10
MAX_PEOPLE_NUM = 100
DEFALT_MEDAL = 'NORMAL'
DEFALT_POINT = 1
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


class Member:
    def __init__(self, name, back_number):
        self.name = name
        self.back_number = back_number
        self._point = 0
        self.weekdays = {weekday: 0 for weekday in weekdays}
        self.medal = DEFALT_MEDAL

    def attend(self, weekday: str):
        self.weekdays[weekday] += 1

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value


class MemberManager:
    def __init__(self):
        self.members = {}

    def _add_member(self, name: str) -> None:
        self.members[name] = Member(
            name=name,
            back_number=len(self.members) + 1
        )

    def get_member(self, name: str) -> Member:
        if name not in self.members:
            self._add_member(name)
        return self.members[name]


class PointCalculator:
    @classmethod
    def get_attend_point(self, weekday: str) -> int:
        if weekday in ['wednesday']:
            return 3
        if weekday in ['saturday', 'sunday']:
            return 2
        return DEFALT_POINT

    @classmethod
    def get_bonus(self, cnt: int) -> int:
        if cnt >= 10:
            return BONUS_POINT
        return 0


class MedalCreator:
    @classmethod
    def make_medal(self, point) -> str:
        if point >= 50:
            return "GOLD"
        if point >= 30:
            return "SILVER"
        return DEFALT_MEDAL


class Club:
    def __init__(self):
        self.membermanager = MemberManager()
        self.members = self.membermanager.members
        self.pg = PointCalculator()
        self.mc = MedalCreator()

    def give_attend_point(self, member: Member, weekday: str):
        member.point += self.pg.get_attend_point(weekday)

    def give_bonus_points_for_closing(self):
        for member in self.members.values():
            wednes_cnt = member.weekdays['wednesday']
            weekends_cnt = member.weekdays['saturday'] + member.weekdays['sunday']
            member.point += self.pg.get_bonus(wednes_cnt) + self.pg.get_bonus(weekends_cnt)
            member.medal = self.mc.make_medal(member.point)

    def announce_all_members_score_medal(self):
        for member in self.members.values():
            print(f"NAME : {member.name}, POINT : {member.point}, GRADE : {member.medal}")

    def announce_kicked_out_member(self):
        print("\nRemoved player")
        print("==============")
        for member in self.members.values():
            wednes_cnt = member.weekdays['wednesday']
            weekends_cnt = member.weekdays['saturday'] + member.weekdays['sunday']
            if (member.medal == 'NORMAL') and (wednes_cnt + weekends_cnt == 0):
                print(member.name)


def input_file():
    try:
        club = Club()
        with open("../attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line: break
                parts = line.strip().split()
                if len(parts) != 2: continue
                name, weekday = parts
                member = club.membermanager.get_member(name)
                member.attend(weekday)
                club.give_attend_point(member, weekday)
        club.give_bonus_points_for_closing()
        club.announce_all_members_score_medal()
        club.announce_kicked_out_member()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    input_file()
