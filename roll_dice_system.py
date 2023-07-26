""""" Import modules """""
import random
from PIL import Image

img = Image.open("DICE_EMPTY.jpg")
img.load()
img2 = Image.open("DICE_EMPTY.jpg")
img2.load()
point = Image.open("DICE_POINT_edited.png")
point.load()


def gen_dice(num, save_slot_name):
    if num == 1:
        image_obj = Image.open("DICE_EMPTY.jpg")
        image_obj.paste(point, (500, 1000), mask=point)
        image_obj.save(save_slot_name)
        return image_obj
    if num == 2:
        image_obj = Image.open("DICE_EMPTY.jpg")
        image_obj.paste(point, (650, 1150), mask=point)
        image_obj.paste(point, (350, 850), mask=point)
        image_obj.save(save_slot_name)
        return image_obj
    if num == 3:
        image_obj = Image.open("DICE_EMPTY.jpg")
        image_obj.paste(point, (650, 1150), mask=point)
        image_obj.paste(point, (350, 850), mask=point)
        image_obj.paste(point, (500, 1000), mask=point)
        image_obj.save(save_slot_name)
        return image_obj
    if num == 4:
        image_obj = Image.open("DICE_EMPTY.jpg")
        image_obj.paste(point, (650, 1150), mask=point)
        image_obj.paste(point, (350, 850), mask=point)
        image_obj.paste(point, (350, 1149), mask=point)
        image_obj.paste(point, (650, 850), mask=point)
        image_obj.save(save_slot_name)
        return image_obj
    if num == 5:
        image_obj = Image.open("DICE_EMPTY.jpg")
        image_obj.paste(point, (650, 1150), mask=point)
        image_obj.paste(point, (350, 850), mask=point)
        image_obj.paste(point, (350, 1149), mask=point)
        image_obj.paste(point, (500, 1000), mask=point)
        image_obj.paste(point, (650, 850), mask=point)
        image_obj.save(save_slot_name)
        return image_obj
    if num == 6:
        image_obj = Image.open("DICE_EMPTY.jpg")
        image_obj.paste(point, (650, 1150), mask=point)
        image_obj.paste(point, (350, 850), mask=point)
        image_obj.paste(point, (350, 1000), mask=point)
        image_obj.paste(point, (650, 1000), mask=point)
        image_obj.paste(point, (350, 1149), mask=point)
        image_obj.paste(point, (650, 850), mask=point)
        image_obj.save(save_slot_name)
        return image_obj


def call():
    number1 = int(random.uniform(1, 7))
    number2 = int(random.uniform(1, 7))
    print(number1, number2)
    dice1 = gen_dice(number1, "dice1.jpg")
    dice2 = gen_dice(number2, "dice2.jpg")
    result = Image.new('RGB', (2160, 1440))
    result.load()
    dice1.load()
    dice2.load()
    result.paste(dice1, (0, 0))
    result.paste(dice2, (1080, 0))
    result.save("dice_result.jpg")
    move_points = number1 + number2
    print("You got", move_points, "points!")
    return result
