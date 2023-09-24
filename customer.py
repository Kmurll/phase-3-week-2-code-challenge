from review import Review  # Import the Review class from the review module

class Customer:
    # Class attribute to store all the customer instances
    customers = []

    # Constructor method to initialize the Customer object with given_name, family_name, and an empty list of reviews
    def __init__(self, given_name, family_name):
        self.given_name = given_name  # Initializes the 'given_name' attribute with the provided given name
        self.family_name = family_name  # Initializes the 'family_name' attribute with the provided family name
        self.reviews = []  # Initializes an empty list to store reviews associated with this particular customer

    # Getter method to get the given name of the customer
    def get_given_name(self):
        return self.given_name

    # Getter method to get the family name of the customer
    def get_family_name(self):
        return self.family_name

    # Method to return the full name of the customer by concatenating given_name and family_name
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    # Class method to retrieve all customer instances
    @classmethod
    def all(cls):
        return cls.customers  # Used to retrieve all customers

    # Method to get a list of restaurants associated with this customer's reviews
    def restaurants(self):
        # Constructs a list of unique restaurants by using a set comprehension
        return list({review.restaurant for review in self.reviews})

    # Method to add a new review for a restaurant associated with this customer
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)  # Creates a new review instance
        self.reviews.append(review)  # Adds the review to the customer's list of reviews
        restaurant.reviews.append(review)  # Adds the review to the restaurant's list of reviews
