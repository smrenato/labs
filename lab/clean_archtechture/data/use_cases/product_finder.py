from ...domain.use_cases.product_finder import ProductFinder as ProductFinderInterface


class ProductFinder(ProductFinderInterface):
    def find(self, name) -> dict:
        return {"Product": [name]}
