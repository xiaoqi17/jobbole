# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Field,Item

class JobboleItem(Item):

    title = Field()  #标题
    create_date = Field()  #发布时间
    url = Field()  #文章链接
    praise_nums = Field()  #点赞
    fav_nums = Field()   #收藏
    comment_nums = Field()  #评论
    tag = Field()  #标签
    content = Field()  # 内容
