import random

def is_hit(x, y, r):
    distance_squared = x ** 2 + y ** 2
    radius_squared = r ** 2
    
    if (x >= 0 and y >= 0 and distance_squared == radius_squared) or \
       (x <= 0 and y <= 0 and distance_squared == radius_squared) or \
       (x <= 0 and y >= 0 and y == x + r) or \
       (y == 0 and x ** 2 <= radius_squared) or \
       (x == 0 and y < 0 and y ** 2 <= radius_squared):
        return "На межі"
    elif (x > 0 and y > 0 and distance_squared < radius_squared) or \
         (x < 0 and y < 0 and distance_squared < radius_squared) or \
         (x < 0 and y > 0 and y < x + r) or \
         (x == 0 and y ** 2 < radius_squared) or \
         (y == 0 and x ** 2 < radius_squared):
        return "потрапив в мішень"
    else:
        return "мішень не ушкоджена"

def generate_shots(num_shots, r):
    shots = []
    for i in range(num_shots):
        x = random.randint(-r+2, r+2)
        y = random.randint(-r+2, r+2)
        result = is_hit(x, y, r)
        shots.append((i + 1, x, y, result))
    return shots

def print_results(shots):
    print(f"{'№ пострілу':<10}{'Координати пострілу':<20}{'Результат':<25}")
    print("-" * 55)
    for shot in shots:
        print(f"{shot[0]:<10}({shot[1]}, {shot[2]}){'':<8}{shot[3]:<25}")

if __name__ == "__main__":
    r = int(input("Введіть радіус мішені: "))
    shots = generate_shots(10, r)
    print_results(shots)
