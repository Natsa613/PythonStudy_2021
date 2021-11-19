
# Todolist
# 1. 아이템 추가시 수량도 인자로 받음
# 2. inventory  전역함수인데, 인자로 받아서 처리하기
# call by reference
def add_item(item, amount, t_inventory):
    # 존재하면 1 추가
    if check_item(item, t_inventory):
        inventory[item] += amount
        print(item+"의 수량이 "+str(t_inventory[item])+"개가 되었습니다.")
   # 존재하지 않으면 추가하면서 수량은 1
    else:
       t_inventory[item] = amount
       print(item+"이 추가되었습니다.")
# 기존의 수량을 모두 버림(수량0)
# 존재하지 않으면 무시
def remove_item(item, t_inventory):
    if check_item(item, t_inventory):
        inventory[item] == 0
        print(item+"의 수량이 0이 되었습니다.")
    else:
        print(item+"이 존재하지 않습니다.")
# 새로운 함수 , 포션 사용
# 존재하는 아이템을 수량 1 빼기
def consume_item(item):
    if check_item(item):
        if inventory[item] >= 1:
            inventory[item] -= 1
            print(item+"아이템을 사용하여 "+str(inventory[item])+"개가 되었습니다.")
        else:
            inventory[item] = 0
            print("해당 아이템의 수량이 0입니다.")
    else:
        print("해당 아이템이 존재하지 않습니다.")

def check_item(item, t_inventory):
    return item in t_inventory

def print_itemMenu():
    print("0.끝내기")
    print("1.아이템 추가")
    print("2.아이템 삭제")
    print("3.아이템 확인")
    print("4.아이템 사용")

# Todolist 2
# while문을 아이템 다루기 함수로 구현 
def use_item():
    while True:
        print_itemMenu()
        option = int(input("메뉴 번호를 입력하세요)"))
        if option == 0:
            print("종료합니다.")
            break
        elif option == 1:
            new_item = input("아이템을 입력하세요.)")
            amount = int(input("수량을 입력하세요.)"))
            # Todolist 1
            # 함수 인자 추가하는 기능 구현시
            add_item(new_item, amount, inventory)
        elif option == 2:
            eliminated_item = input("아이템을 입력하세요.)")
            remove_item(eliminated_item, inventory)
        elif option == 3:
            print(inventory)
        elif option == 4:
            use_item = input("사용할 아이템을 입력하세요.)")
            consume_item(use_item)
        else:
            print("잘못된 번호를 입력하셨습니다.")

# key = item 이름, value = 수량
inventory = {}
# todolist 3
# 캐릭터 만들기
character = {}
select_character = None
def new_character (name, t_character):
    if check_character (name, t_character):
        print("이미 존재하는 캐릭터의 이름입니다.")
    else:
        inventory = {}
        t_character [name] = inventory

        
def check_character (name, t_character):
    return name in t_character

def print_characterMenu():
    print("0.끝내기")
    print("1.캐릭터 추가")
    print("2.캐릭터 조회")
    print("3.캐릭터 선택")
    print("4.캐릭터 인벤토리 조작")

while True:
    print_characterMenu()
    option = int(input("메뉴를 선택해주세요.)"))
    if option == 0:
        print("종료되었습니다.")
        break
    elif option == 1:
        name = input("캐릭터 이름을 입력하세요.)")
        new_character (name, character)
    elif option == 2:
        i = 1
        print ("#######################")
        for name in character.keys():
            print(str(i)+". "+name)
            i+=1
        print ("#######################")
    elif option == 3:
        temp_name = input("선택한 캐릭터의 이름을 입력해주세요.)")
        if check_character(temp_name, character):
            select_character = temp_name
            print(select_character+"이 선택되었습니다.")
        else:
            print(temp_name+"은 존재하지 않는 캐릭터 입니다.")
# 캐릭터 이름으로 식별
# 캐릭터 인벤토리
# 캐릭터 장착기능
