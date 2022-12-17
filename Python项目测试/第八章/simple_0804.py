# 练习8-6：城市名
def city_country(city, country):
    """一座城市名以及所属国家"""
    recivice = f"{city.title()},{country.title()}!"
    return recivice
infom1 = city_country('santiago', 'chile')
infom2 = city_country('shanxi', 'china')
infom3 = city_country('xiamen', 'china')
print(f"{infom1}\n{infom2}\n{infom3}")

print('-----------------------------------------------------')
print('-----------------------------------------------------')


"""
# 练习8-7：专辑
def make_album(name, song, num=None):

    album = {
        'names': name,
        'songs': song,
    }
    if num:
        album['nums'] = num
    return album
new_album = make_album('张杰', '看月亮爬上来')
print(new_album)
new_album = make_album(name='张靓颖', song='哈哈哈', num=3)
print(new_album)

"""
# 练习8-8
def make_album(name, song, num=None):
    """一个描述音乐专辑的字典"""
    album = {
        'names': name,
        'songs': song,
    }
    if num:
        album['nums'] = num
    return album
while True:
    print("输入专辑的歌手和名称,在任意时刻输入'q'即可退出")
    f_name = input('请输入歌手名字：')
    if f_name == 'q':
        break
    f_song = input('请输入专辑名：')
    if f_song == 'q':
        break
    f_age = input('请输入歌曲数量：')
    if f_age == 'q':
        break
    new_album = make_album(f_name, f_song, f_age)
    print(new_album)