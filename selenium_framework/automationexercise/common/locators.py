base_url = 'https://automationexercise.com/'


class CommonLocators:

    products_in_cart = '//tbody/tr[contains(@id, "product")]'
    empty_card = '//*[@id="empty_cart"][@style="display: block;"]'

    catalog = '//*[@class="recommended_items"]'
    product = '//*[@class="single-products"]'
    add_cart_btn = '//*[@class="btn btn-default add-to-cart"]'

    cart_modal = '//*[@id="cartModal"]'

    # shop-menu links

    home = '//*[@href="/"]'
    products = '//*[@href="/products"]'
    cart = '//*[@href="/view_cart"]'


common = CommonLocators()
