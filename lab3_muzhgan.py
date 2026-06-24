# Muzhgan Bakhtyar | Lab 3 | Intro to Python

# Ticket 1.
# PREDICT: 4
username = "Leah"
print(len(username)) 
# EXPLAIN: The len() function did count the number of characters in the string "leah" which is 4 not 16.

# Ticket 2.
# PREDICT: L, h
username = "Leah"
print(username[0]) # L
print(username[3]) # h
# EXPLAIN: The first print started at index 0 and printed the first character which is L. The second print stated at index 3 and printed the fourth charachter which was h.

# Ticket 3.
# PREDICT: welcome to loop, leah.
print("Welcome to Loop, " + username)
print(f"Welcome to Loop, @{username}!")
# EXPLAIN: None of them were easy to do.

# Ticket 4.
# PREDICT: I think it will give me a error 
# username[0] = "X" : Gave me an error because strings are immutable.
username = "leah"
print(username.upper()) # LEAH
# EXPLAIN: immutable means that the string cannot be changed.

# Ticket 5.
# PREDICT: the count will print 3 and the first print will print "I love watching movies"
feed = [
    "I love watching movies",
    "I love to sleep",
    "I love to eat",
]

print(len(feed))
print(feed[0])
# EXPLAIN: I used index 0 because lists start counting at 0.

# Ticket 6.
# PREDICT:  the new post will be at index 3.
feed.append("I love to design")
print(feed)
# EXPLAIN:  The fourth post is at index 3 because lists start at 0.

# Ticket 7.
# PREDICT: "I love watching movies" will be removed.
feed.pop(0)
feed.sort()
print(feed)
# EXPLAIN: pop(0) removed the first item.

# Ticket 8.
# This will break on purpose. (profile [0])
# key error: 0
# I must use "followers" isted of 0.
# PREDICT: follower will print 100
profile = {
    "username": "leah",
    "followers": 100,
    "verified": False,
}
print(profile["followers"])
# EXPLAIN: I used the key "followers" to get the value of 100.

# Ticket 9.
# PREDICT: the profile will print the new bio and age will print none.
profile["followers"] = profile["followers"]
profile["bio"] = "student at loop"
print(profile)
print(profile.get("age"))
# EXPLAIN: I used the get method to get the value of age which id not in the dictionary so it will print none.

# Ticket 10.
# PREDICT: @leah has 100 followers and 3 posts. Top post: I love to eat
print(
    f'@{profile["username"]} has {profile["followers"]} followers and {len(feed)} posts. Top post:{feed[0]}'
)
# EXPLAIN: I used dictionary called profile, I also used a list called feed, I used len to count the posts and I used an f-string to combine everything into one sentence.