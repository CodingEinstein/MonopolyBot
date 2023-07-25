from PIL import Image
import random
n1 = int()
n2 = int()
img = Image.open("DICE_EMPTY.jpg")
img.load()
img2 = Image.open("DICE_EMPTY.jpg")
img2.load()
point = Image.open("DICE_POINT_edited.png")
point.load()


def gen_dice(num, image_obj, savename):
    if num == 1:
        new_image = image_obj
        new_image.paste(point, (500, 1000), mask=point)
        image_obj.putdata(new_image, 1, 0)
        image_obj.save(savename)
        return image_obj
    if num == 2:
        new_image = image_obj
        new_image.paste(point, (650, 1150), mask=point)
        new_image.paste(point, (350, 850), mask=point)
        image_obj.putdata(new_image, 1, 0)
        image_obj.save(savename)
        return image_obj
    if num == 3:
        new_image = image_obj
        new_image.paste(point, (650, 1150), mask=point)
        new_image.paste(point, (350, 850), mask=point)
        new_image.paste(point, (500, 1000), mask=point)
        image_obj.putdata(new_image, 1, 0)
        image_obj.save(savename)
        return image_obj
    if num == 4:
        new_image = image_obj
        new_image.paste(point, (650, 1150), mask=point)
        new_image.paste(point, (350, 850), mask=point)
        new_image.paste(point, (350, 1149), mask=point)
        new_image.paste(point, (650, 850), mask=point)
        image_obj.putdata(new_image, 1, 0)
        image_obj.save(savename)
        return image_obj
    if num == 5:
        new_image = image_obj
        new_image.paste(point, (650, 1150), mask=point)
        new_image.paste(point, (350, 850), mask=point)
        new_image.paste(point, (350, 1149), mask=point)
        new_image.paste(point, (500, 1000), mask=point)
        new_image.paste(point, (650, 850), mask=point)
        new_image.save(savename)
        image_obj.putdata(new_image, 1, 0)
        return image_obj
    if num == 6:
        new_image = image_obj
        new_image.paste(point, (650, 1150), mask=point)
        new_image.paste(point, (350, 850), mask=point)
        new_image.paste(point, (350, 1000), mask=point)
        new_image.paste(point, (650, 1000), mask=point)
        new_image.paste(point, (350, 1149), mask=point)
        new_image.paste(point, (650, 850), mask=point)
        image_obj.putdata(new_image, 1, 0)
        image_obj.save(savename)
        return image_obj


def call(number1, number2, savename1, savename2):
    number1 = int(random.uniform(1, 7))
    number2 = int(random.uniform(1, 7))
    print(number1, number2)
    dice1 = gen_dice(number1, img, savename1)
    dice2 = gen_dice(number2, img2, savename2)
    # print(number1, number2)
    result = Image.new('RGB', (2160, 1440))
    result.load()
    dice1.load()
    dice2.load()
    result.paste(dice1, (0, 0))
    result.paste(dice2, (1080, 0))
    result.save("dice_result.jpg")
    result.show()
    move_points = number1 + number2
    print("You got", move_points, "points!")
    return result


call(0,0, "dice1.jpg", "dice2.jpg")
