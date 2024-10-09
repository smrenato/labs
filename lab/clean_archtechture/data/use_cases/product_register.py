from ...domain.use_cases.product_register import (
    ProductRegister as ProductRegisterInterface,
)


class ProductFinderA(ProductRegisterInterface):
    def __init__(self) -> None: ...
    def registry(self, http_request) -> dict:
        return {"registry": "product"}
