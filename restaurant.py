class Restaurant:
    # Class attribute to store all the restaurant instances
    restaurants = []

    # Constructor method to initialize the Restaurant object with a name and an empty list of reviews
    def __init__(self, name):
        self.name = name  # Initializes the 'name' attribute with the provided name
        self.reviews = []  # Initializes an empty list to store reviews associated with this restaurant

    # Getter method to get the name of the restaurant
    def get_name(self):
        return self.name

    # Class method to retrieve all restaurant instances
    @classmethod
    def all(cls):
        return cls.restaurants  # Used to retrieve all the restaurants

    # Method to calculate the average star rating of the restaurant based on its reviews
    def average_star_rating(self):
        if not self.reviews:
            return 0  # If there are no reviews, it returns 0 as the average rating

        # Calculates the total rating by summing up the ratings of all reviews
        total_rating = sum(review.rating for review in self.reviews)

        # Calculates the average rating by dividing the total rating by the number of reviews
        return total_rating / len(self.reviews)

    # Method to get a list of customers who have reviewed this restaurant
    def customers(self):
        # Constructs a list of unique customers by using a set comprehension
        return list({review.customer for review in self.reviews})

