class Flower:
    def __init__(self, name, color, height, vase_life, cost):
        self.name = name
        self.color = color
        self.height = height
        self.vase_life = vase_life
        self.cost = cost


class Rose(Flower):
    def __init__(self, name, color, height, vase_life, cost, has_thorns):
        super().__init__(name, color, height, vase_life, cost)
        self.has_thorns = has_thorns


class Chamomile(Flower):
    def __init__(self, name, color, height, vase_life, cost):
        super().__init__(name, color, height, vase_life, cost)


class Orchid(Flower):
    def __init__(self, name, color, height, vase_life, cost, flower_type):
        super().__init__(name, color, height, vase_life, cost)
        self.type = flower_type


rose = Rose('Роза', 'Красный', 30, 3, 100, True)
chamomile = Chamomile('Ромашка', 'Белый', 10, 1, 15)
orchid = Orchid('Орхидея', 'Сиреневый', 25, 7, 550, 'Дикая')

class Bouquet:
    def __init__(self, flowers: list, order_flowers: dict):
        self.flowers = flowers
        self.order_flowers = order_flowers

    def calculate_cost(self):
        total_cost = 0

        for flower in self.order_flowers:
            total_cost += self.order_flowers[flower] * flower.cost

        return total_cost

    def calculate_days_lifespan(self):
        return sum([flower.vase_life for flower in self.order_flowers]) / len(self.order_flowers)

    def sort_by_vase_life(self):
        return sorted(self.flowers, key=lambda x: x.vase_life)

    def sort_by_name(self):
        return sorted(self.flowers, key=lambda x: x.name)

    def sort_by_color(self):
        return sorted(self.flowers, key=lambda x: x.color)

    def sort_by_cost(self):
        return sorted(self.flowers, key=lambda x: x.cost)

    def find_by_param(self, param, param_name):
        for flower in self.flowers:
            if getattr(flower, param_name) == param:
                return flower

        return None

    def find_by_name(self, name):
        flower = self.find_by_param(name, 'name')
        return flower

    def find_by_height(self, height):
        flower = self.find_by_param(height, 'height')
        return flower


bouq = [rose, chamomile, orchid]
order = {rose: 10, chamomile: 15, orchid: 2}
bouquet = Bouquet(bouq, order)
days = bouquet.calculate_days_lifespan()
t_cost = bouquet.calculate_cost()
new_flower = bouquet.find_by_name('Роза')
sort_flowers_vase_life = bouquet.sort_by_vase_life()
sort_flowers_by_name = bouquet.sort_by_name()

print(days)
print(t_cost)
print(new_flower)
print(sort_flowers_vase_life)
print(sort_flowers_by_name)
