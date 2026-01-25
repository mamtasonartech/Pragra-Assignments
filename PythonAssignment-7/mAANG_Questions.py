"""MAANG Question 1 (Amazon / Google-style)
Problem: Design a class LRUCounter that:
● Has a method hit(key)
● Tracks how many times each key is accessed
● Has a method most_used() that returns the most accessed key """

# Define a class named LRUCounter
class LRUCounter:

# This class will track how many times each key is accessed
# Create a data structure to store keys and their access counts
    def __init__(self):
        self.counter = {}

# Define a method hit(key)
# When this method is called:
#   - Check if the key already exists
#   - If it exists, increase its access count by 1
#   - If it does not exist, add the key with an access count of 1
#   - Update tracking so the most-used key can be identified
    def hit(self, key):
        if key in self.counter:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

# Define a method most_used()
# When this method is called:
#   - Check if any keys exist
#   - Find the key with the highest access count
#   - If multiple keys have the same highest count, apply a chosen rule
#   - Return the most accessed key
    def most_used(self):
        if not self.counter:
            return None
        return max(self.counter, key=self.counter.get)

lru1 = LRUCounter()

lru1.hit("J")
lru1.hit("M")
lru1.hit("M")
lru1.hit("G")
lru1.hit("M")
lru1.hit("M")

print(lru1.most_used())

"""Design a class RateLimiter that: 
● Allows only N requests per user 
● Has method allow_request(user_id)
● Returns True if allowed, False otherwise """

# Define a class named RateLimiter
# This class controls how many requests a user can make
class RateLimiter:

    # Store a maximum allowed request limit (N)
    # Maintain a data structure to track:
    #   - each user_id
    #   - number of requests made by that user
    def __init__(self, limit):
        self.limit = limit
        self.user_requests = {}

    # Define a method allow_request(user_id)
    # When this method is called:
    #   - Check if the user_id exists in the tracking structure
    #   - If the user does not exist, initialize their request count
    #   - If the user exists, check their current request count
    #   - If request count is less than N:
    #       - Increment the request count
    #       - Allow the request (return True)
    #   - If request count has reached N:
    #       - Deny the request (return False)
    def allow_request(self, user_id):

        # Edge case: new user
        if user_id not in self.user_requests:
            self.user_requests[user_id] = 0

        # Allow request if under limit
        if self.user_requests[user_id] < self.limit:
            self.user_requests[user_id] += 1
            return True

        # Deny request if limit reached
        return False

rateLimit = RateLimiter(4)
rateLimit1 =RateLimiter(2)
print(rateLimit.allow_request("userA"))
print(rateLimit.allow_request("userA"))
print(rateLimit.allow_request("userA"))
print(rateLimit.allow_request("userA"))
print(rateLimit1.allow_request("userB"))
print(rateLimit1.allow_request("userB"))
print(rateLimit1.allow_request("userB"))
