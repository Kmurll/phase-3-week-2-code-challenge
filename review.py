class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def get_rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.reviews

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant
