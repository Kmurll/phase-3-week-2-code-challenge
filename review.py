class Review:
    # Class attribute to store all the review instances
    reviews = []

    # Constructor method to initialize the Review object with a customer, restaurant, and a rating
    def __init__(self, customer, restaurant, rating):
        self.customer = customer  # Initializes the 'customer' attribute with the provided customer object
        self.restaurant = restaurant  # Initializes the 'restaurant' attribute with the provided restaurant object
        self.rating = rating  # Initializes the 'rating' attribute with the provided rating value

    # Getter method to get the rating value of the review
    def get_rating(self):
        return self.rating

    # Class method to retrieve all review instances
    @classmethod
    def all(cls):
        return cls.reviews  # Used to retrieve all the reviews

    # Method to get the customer associated with this review
    def get_customer(self):
        return self.customer

    # Method to get the restaurant associated with this review
    def get_restaurant(self):
        return self.restaurant
