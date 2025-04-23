def check_voting_eligibility(age):
    """Determine voting eligibility for three fictional countries"""
    countries = [
        ("Peturksbouipo", 16),
        ("Stanlau", 25),
        ("Mayengua", 48)
    ]
    
    results = []
    for country, voting_age in countries:
        if age >= voting_age:
            results.append(f"You can vote in {country} where the voting age is {voting_age}.")
        else:
            results.append(f"You cannot vote in {country} where the voting age is {voting_age}.")
    
    return '\n'.join(results)

def main():
    age = int(input("How old are you? "))
    print(check_voting_eligibility(age))

if __name__ == '__main__':
    main()