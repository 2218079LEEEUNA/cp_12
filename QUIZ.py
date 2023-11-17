class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def calculate(self, quantity):
        total_price = self.price * quantity
        print(f"{self.name} {quantity}잔을 주문하셨습니다. 총 가격은 {total_price}원 입니다.")
        return total_price
Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)
selected_beverage = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")
if selected_beverage == "커피":
    Coffee.calculate = Coffee
elif selected_beverage == "녹차":
    Coffee.calculate  = GreenTea
elif selected_beverage == "아이스티":
    Coffee.calculate = IceTea
else:
    print("올바르지 않은 음료입니다. 프로그램을 종료합니다.")
    exit()
quantity = int(input(f"{selected_beverage} 몇 잔을 주문하시겠습니까?: "))
total_price = Coffee.calculate.calculate(quantity)
