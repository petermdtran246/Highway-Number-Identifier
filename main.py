# Initialize input for interstate highways
interstate_highways = int(input())

# Check if interstate highways are from 1 to 99 (inclusive)
if 1 <= interstate_highways <= 99:
    # Nested if statement to check whether interstate highways are even or odd numbers.
    if interstate_highways % 2 == 0:
        print(f'I-{interstate_highways} is the primary, going to east/ west.')
    else:
        print(f'I-{interstate_highways} is the primary, going to north/ south.')
# Check if interstate highways are from 100 to 999 (inclusive)
elif 100 <= interstate_highways <= 999:
    # Nested if to check when interstate highways are 405.
    if interstate_highways == 405:
        print(f'I-{interstate_highways} is auxiliary, serving I-5, going east/west.')
    # Nested if to check when interstate highways are 290
    elif interstate_highways == 290:
        print(f'I-{interstate_highways} is auxiliary, serving I-90, going east/west.')
    # Nested if to check when interstate highways are 200
    elif interstate_highways == 200:
        print(f'{interstate_highways} is not a valid interstate highway number.')
# Check if interstate highways are neither 1 - 99 nor 100 - 999.
else:
    print(f'{interstate_highways} is not a valid interstate highway number.')