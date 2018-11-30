class HouseItem():

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[{}] 占地面积 {:.2f}".format(self.name, self.area)


class House():
    # 需要外部传入的参数，才在函数中定义成形参，内部自己决定的参数不需要定义成形参，比如下面的剩余面积，家具名称
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # python能自动的将一对括号诶的代码连接在一起
        return ("户型：{}\n总面积： {:.2f}[剩余：{:.2f}]\n家具：{}"
                .format(self.house_type, self.area,
                        self.free_area, self.item_list))
    # 这里的wang只是作为形参指向HouseItem的对象，可以是任意的名称，随意改动
    def add_item(self, wang):
        print("要添加{}".format(wang))
        # 1.判断家具的面积
        if wang.area > self.free_area:
            print("{}面积太大了，无法添加".format(wang.name))

            return

            # 2.将家具的名称添加到列表
        self.item_list.append(wang.name)

        # 3.计算剩余面积
        self.free_area -= wang.area


# 1.创建家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(chest)
print(bed)
print(table)
# 2.创建房子对象
my_home = House("两室一厅", 60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)