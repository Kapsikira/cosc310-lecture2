"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu


class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    pass


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        # TODO: validate FIRST, then mutate.
        #   if qty < 1:                 raise ValueError(...)
        if (qty < 1):
            raise ValueError("Quantity must be at least 1")
        #   if not item["available"]:   raise OutOfStockError(...)
        if (item["available"]==False):
            raise OutOfStockError("Item is out of stock")
        checker:bool = False
        new_dic={"item_id": item["id"], "name": item["name"], "price": item["price"], "qty": qty}
        for i in self.lines:
            if (i["item_id"]==item["id"]):
                checker=True
                i["qty"]=i["qty"]+qty
                break
        if(checker==False):
            self.lines.append(new_dic)

        

    def remove_item(self, item_id: int) -> None:
        # TODO: raise KeyError if the item is not in the cart
        checker:bool=False
        for line in self.lines:
            if line["item_id"] == item_id:
                checker = True
                self.lines.remove(line)
                break

        if checker == False:
            raise KeyError(item_id)
            
        

    def total(self) -> float:
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()

    # TODO: demonstrate each rejection with try/except and a readable message.
    # Example:
    try:
        cart.add_item(gyoza, 0)
    except ValueError as e:
       print(f"Rejected: {e}")

    try:
        cart.add_item(miso,3)
    except OutOfStockError as e:
        print(f"Not available :{e}")

    try:
        cart.remove_item(67)
    except KeyError as e:
        print(f"Not in the cart :{e}")


