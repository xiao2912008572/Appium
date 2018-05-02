a = {
    "meta": {
        "approved": "true",
        "has_account": "null",
        "page_size": 10,
        "total": 2
    },
    "products": [
        {
            "archives": [],
            "category_id": 35173,
            "category_name": "无",
            "description": "null",
            "files": [
                {
                    "file_id": 155730,
                    "id": 61852,
                    "name": "null"
                }
            ],
            "goods_type": "null",
            "guarantee_tags": [
                {
                    "description": "消费者在满足7天内无理由退换货的申请条件下，可以提出",
                    "key": "return_within_7days",
                    "name": "7天无理由退换"
                },
                {
                    "description": "商家在48小时内发货",
                    "key": "fast_delivery",
                    "name": "极速发货"
                }
            ],
            "id": 55693,
            "name": "接口测试商品",
            "organization_id": 5114,
            "prices": [
                {
                    "amount": "1000.0",
                    "id": 62699,
                    "money": "1.00",
                    "properties": []
                }
            ],
            "properties": [
                {
                    "children": [],
                    "id": "null",
                    "name": "功能/用途",
                    "product_property_id": 6,
                    "quotes": [],
                    "value": "null"
                },
                {
                    "children": [],
                    "id": "null",
                    "name": "外观/形状",
                    "product_property_id": 7,
                    "quotes": [],
                    "value": "null"
                },
                {
                    "children": [],
                    "id": "null",
                    "name": "原料/用料",
                    "product_property_id": 9,
                    "quotes": [],
                    "value": "null"
                },
                {
                    "children": [],
                    "id": "null",
                    "name": "工艺/设备",
                    "product_property_id": 8,
                    "quotes": [],
                    "value": "null"
                }
            ],
            "state": "editing"
        },
        {
            "archives": [],
            "category_id": 35169,
            "category_name": "公路运输",
            "description": "null",
            "files": [
                {
                    "file_id": 151230,
                    "id": 61583,
                    "name": "null"
                }
            ],
            "goods_type": "null",
            "guarantee_tags": [],
            "id": 55465,
            "name": "xjy商品",
            "organization_id": 5114,
            "prices": [
                {
                    "amount": "2.0",
                    "id": 62386,
                    "money": "0.01",
                    "properties": []
                }
            ],
            "properties": [],
            "state": "published"
        }
    ]
}

x = a["products"][0]["guarantee_tags"][0]["key"]
y = a["products"][0]["guarantee_tags"][0]["name"]
print(x)
print(y)