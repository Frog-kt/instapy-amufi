# imports
import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = '' # ユーザー名の入力
insta_password = '' # パスワードの入力

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

tag_list = ["部屋紹介", "旅行", "海外旅行", "一人暮らし", "引っ越し", "ヘヤウルルーム", "ひとり暮らし", "インテリア", "賃貸", "賃貸インテリア","ひとり暮らし部屋", "大学生一人暮らし", "ヒュッゲな暮らし", "ワンルーム", "海外インテリア", "家具", "6畳", "12畳", "同居", "角部屋","イケア", "ikea", "IKEA", "無印良品", "収納部屋", "部屋作り", "マイルーム", "部屋掃除", "へや掃除", "秘密基地", "一人暮らし女子","一人暮らし部屋", "男子部屋", "女子部屋", "間接照明", "模様替え", "ニトリ", "同棲生活", "カップル", "北欧インテリア", "おしゃれ部屋","デザイナーズ住宅", "デザイナーズ物件"]

target_tags = random.sample(tag_list, len(tag_list))

print(target_tags)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    # session.set_dont_include(["friend1", "friend2", "friend3"])
    # session.set_do_follow(enabled=True, percentage=10, times=2)
    session.like_by_tags(target_tags, amount=10)