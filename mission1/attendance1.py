BONUS_10TIMES = 10
MAX_PEOPLE_NUM = 100
DEFALT_MEDAL = 'NORMAL'

people_list = {}
weeks_points = {
    'monday': 1,
    'tuesday': 1,
    'wednesday': 3,
    'thursday': 1,
    'friday': 1,
    'saturday': 2,
    'sunday': 2,
}


def get_medal(point: int) -> str:
    if point >= 50:
        return "GOLD"
    if point >= 30:
        return "SILVER"
    return DEFALT_MEDAL


def get_10times_bonus(cnt: int) -> int:
    if cnt >= 10:
        return BONUS_10TIMES
    return 0


def resist_name_if_not_exist(name: str) -> None:
    if name in people_list:
        return
    people_list[name] = {
        'back_number': len(people_list) + 1,
        'point': 0,
        'weekdays': {weekday: 0 for weekday in weeks_points}
    }


def checking_attendance(name: str, weekday: str) -> None:
    # 출석날짜기록
    people_list[name]['weekdays'][weekday] += 1
    # 출석점수부여
    people_list[name]['point'] += weeks_points[weekday]


def input_file():
    try:
        with open("../attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line: break
                parts = line.strip().split()
                if len(parts) != 2: continue
                name, weekday = parts
                # 전체출석체크
                resist_name_if_not_exist(name)
                checking_attendance(name, weekday)

        # 결과 출력
        for name in people_list:
            wednes_cnt = people_list[name]['weekdays']['wednesday']
            weekends_cnt = people_list[name]['weekdays']['saturday'] + people_list[name]['weekdays']['sunday']

            people_list[name]['point'] += get_10times_bonus(wednes_cnt) + get_10times_bonus(weekends_cnt)
            point = people_list[name]['point']
            medal = get_medal(point)
            print(f"NAME : {name}, POINT : {point}, GRADE : {medal}")

        #탈락자 출력
        print("\nRemoved player")
        print("==============")
        for name in people_list:
            point = people_list[name]['point']
            medal = get_medal(point)
            wednes_cnt = people_list[name]['weekdays']['wednesday']
            weekends_cnt = people_list[name]['weekdays']['saturday'] + people_list[name]['weekdays']['sunday']
            if (medal == DEFALT_MEDAL) and (wednes_cnt + weekends_cnt == 0):
                print(name)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    input_file()
