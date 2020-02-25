def user_data(first_name, last_name, year, city, email, phone):
    return print(
        f"First Name - {first_name}; Last Name - {last_name}; Year of Birth - {year}; City - {city}; Email - {email}; Phone - {phone}")


user_data(first_name=input("Your first name is: "), last_name=input("Your last name is: "),
          year=input("Your year of birth is: "), city=input("Your city is: "), email=input("Your email is: "),
          phone=input("Your phone is: "))
