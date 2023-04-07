email = input("Please enter your email address: ")
location_one = ""
location_two = ""
count = 0

for i in email:
    count += 1
    if i == "@":
        location_one = count
    if i == ".":
        location_two = count

company_name = email[int(location_one):(int(location_two)-1)]

print("Your email provider is " + str(company_name))
