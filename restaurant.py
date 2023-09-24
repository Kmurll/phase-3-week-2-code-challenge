class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []

    def get_name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.restaurants

    def average_star_rating(self):
        if not self.reviews:
            return 0

        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)

    def customers(self):
        return list({review.customer for review in self.reviews})
