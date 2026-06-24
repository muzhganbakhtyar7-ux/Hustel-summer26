# Muzhgan Bakhtyar | Lab 3 | Intro to Python

# Ticket 1.
username = "Leah"
print(len(username)) 
# PREDICT: 4
# EXPLAIN: The len() function did count the number of characters in the string "leah" which is 4 not 16.

# Ticket 2.
username = "Leah"
print(username[0]) # L
print(username[3]) # h
# PREDICT: L, h
# EXPLAIN: The first print started at index 0 and printed the first character which is L. The second print stated at index 3 and printed the fourth charachter which was h.

# Ticket 3.
print("Welcome to Loop, " + username)
print(f"Welcome to Loop, @{username}!")
# PERDICT: welcome to loop, leah.
# EXPLAIN: None of them were easy to do.

# Ticket 4.
username = "leah"
print(username.upper()) # LEAH
# PREDICT: I think it will give me a error 
# EXPLAIN: immutable means that the string cannot be changed.

# Ticket 5.
feed = [
    "I love watching movies",
    "I love to sleep",
    "I love to eat",
]

print(len(feed))
print(feed[0])
# PREDICT: the count will print 3 and the first print will print "I love watching movies"
# EXPLAIN: I used index 0 because lists start counting at 0.

# Ticket 6.
feed.append("I love to design")
print(feed)
# PREDICT:  the new post will be at index 3.
# EXPLAIN:  The fourth post is at index 3 because lists start at 0.

# Ticket 7.
feed.pop(0)
feed.sort()
print(feed)
# PREDICT: "I love watching movies" will be removed.
# EXPLAIN: pop(0) removed the first item.

# Ticket 8.
# This will break on purpose. (profile [0])
# key error: 0
# I must use "followers" isted of 0.
profile = {
    "username": "leah",
    "followers": 100,
    "verified": False,
}
print(profile["followers"])
# PREDICT: follower will print 100
# EXPLAIN: I used the key "followers" to get the value of 100.

# Ticket 9.
profile["followers"] = profile["followers"]
profile["bio"] = "student at loop"
print(profile)
print(profile.get("age"))
# PREDICT: the profile will print the new bio and age will print none.
# EXPLAIN: I used the get method to get the value of age which id not in the dictionary so it will print none.

# Ticket 10.
print(
    f'@{profile["username"]} has {profile["followers"]} followers and {len(feed)} posts. Top post:{feed[0]}'
)
# PREDICT: @leah has 100 followers and 3 posts. Top post: I love to eat
# EXPLAIN: I used dictionary called profile, I also used a list called feed, I used len to count the posts and I used an f-string to combine everything into one sentence.