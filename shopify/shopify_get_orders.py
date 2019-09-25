import shopify
API_KEY = 'XXXXX'
PASSWORD = 'XXXXXX'
SHOP_NAME = 'XXXXX'
shop_url = "https://XXXXX.com/admin" % (API_KEY, PASSWORD, SHOP_NAME)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()

order = shopify.Order()
num = order.count()
if num == 1:
    print "There is %s order currently in your %s shopify store" % (num, SHOP_NAME)
else:
    print "There are %s orders currently in your %s shopify store" % (num, SHOP_NAME)