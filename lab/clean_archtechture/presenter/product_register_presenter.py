from ..domain.use_cases.product_register import ProductRegister
from ..data.use_cases.product_register import ProductFinderA


class ProductRegisterPresenter:
    # dependency injection
    def __init__(self, use_case: ProductRegister) -> None:
        self.use_case = use_case

    def handle(self, http_request) -> None:
        self.use_case.registry(http_request)


# obj = ProductRegisterPresenter(ProductFinderA())
