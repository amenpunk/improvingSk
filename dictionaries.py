def itemList():
    wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
    for key,val in wardrobe.items():
        for item in val:
            print("{} {}".format(key,item))

def email_list(domains):
    emails = []
    for domain, users in domains.items() :
        for user in users:
            emails.append("{}@{}".format(user,domain))
    return(emails)

# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        for user in users:
            if not user in user_groups:
                user_groups[user] = [group]
            else:
                user_groups[user].append(group)

    return(user_groups)

# print(groups_per_user({"local": ["admin", "userA"], "public":  ["admin", "userB"], "administrator": ["admin"] }))

def add_prices(basket):
    total = 0
    for item, price in basket.items():
        total += price
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

