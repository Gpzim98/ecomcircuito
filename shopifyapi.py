import shopify
shop_url = 'https://o-circuito-da-moda.myshopify.com/'
api_version = '2021-01'
access_token = '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'

session = shopify.Session(shop_url, api_version, access_token)
shopify.ShopifyResource.activate_session(session)

variant = shopify.Variant.find(39498220077243)
current_quantity = variant.attributes['inventory_quantity'] # -195
new = 10
final_quantity = new - current_quantity

shopify.InventoryLevel.adjust(
    location_id=61530800315,
    inventory_item_id=variant.attributes['inventory_item_id'], available_adjustment=final_quantity)

shopify.ShopifyResource.clear_session()
