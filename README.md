# ra-amazon-clone-be

Backend for Amazon Clone Project (Marketing Research Propose)

## 项目介绍

本项目是市场研究所使用的样板购物网站的后端程序，
实现了提供商品信息、用户注册与登录、下单、购买等功能的接口。

## 代码特色介绍

### 完全REST风格的接口设计

本后台程序的url设计极其简单明了：

```
urlpatterns = [
    path('good', views.good, name='good'),
    path('user', views.user, name='user'),
    path('cart', views.cart, name='cart'),
    path('label', views.good_label, name='label'),
    path('category',views.category, name='category'),
    path('generate-suggestions',views.generateSuggestions),
    path('suggestion', views.suggestion, name='suggestion')
]
```

几个接口的设计直接对应数据模型的几个Model,
一切的操作都可以使用HTTP动词（GET，POST等）以及参数（?key=value）来进行明确
这简化了前后端对接成本。

比如，获取全部的商品：
```
[GET].../good?list_all=true
```
而要获取某个具体商品的详细信息：
```
[GET].../good?gid=3
```
