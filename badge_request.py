import csv
import os

def select_zone():
    print("출입 요청 구역을 선택하세요:")
    print("1: 본사")
    print("2: 강남사무소")
    print("3: 둘다")
    zone = input("선택 (1/2/3): ").strip()
    while zone not in {"1", "2", "3"}:
        zone = input("잘못된 입력입니다. 다시 선택하세요 (1/2/3): ").strip()
    return zone

def select_main_floor():
    print("본사 주 사용 층을 선택하세요 (10~13층):")
    floor = input("층 입력: ").strip()
    while floor not in {"10", "11", "12", "13"}:
        floor = input("잘못된 입력입니다. 층을 다시 입력하세요 (10~13): ").strip()
    dept = input("주 근무층 부서를 입력하세요 (선택 사항, 엔터시 생략): ").strip()
    return floor, dept

def select_floor14():
    val = input("14층 출입 권한이 필요한가요? (o/x): ").strip().lower()
    while val not in {"o", "x"}:
        val = input("잘못된 입력입니다. (o/x) 로 입력하세요: ").strip().lower()
    return val

def select_category():
    print("구분을 선택하세요:")
    print("1: 신규권한")
    print("2: 재발급")
    cat = input("선택 (1/2): ").strip()
    while cat not in {"1", "2"}:
        cat = input("잘못된 입력입니다. 다시 선택하세요 (1/2): ").strip()
    return cat

def gather_employee_info():
    dept = input("부서: ").strip()
    position = input("직위: ").strip()
    emp_id = input("사번: ").strip()
    name = input("이름: ").strip()
    return dept, position, emp_id, name


def zone_text(zone):
    return {"1": "본사", "2": "강남사무소", "3": "둘다"}[zone]


def category_text(cat):
    return {"1": "신규권한", "2": "재발급"}[cat]


def export_to_csv(data, filename="badge_requests.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "출입구역",
                "주층",
                "주층부서",
                "14층출입",
                "구분",
                "부서",
                "직위",
                "사번",
                "이름",
            ])
        writer.writerow(data)
    print(f"데이터가 {filename} 파일에 저장되었습니다.")


def main():
    zone = select_zone()
    main_floor = ""
    main_floor_dept = ""
    if zone in {"1", "3"}:
        main_floor, main_floor_dept = select_main_floor()
    floor14 = select_floor14()
    category = select_category()
    dept, position, emp_id, name = gather_employee_info()
    data = [
        zone_text(zone),
        main_floor,
        main_floor_dept,
        floor14,
        category_text(category),
        dept,
        position,
        emp_id,
        name,
    ]
    export_to_csv(data)

if __name__ == "__main__":
    main()
