### START the program

### Existing Customer Utility
```text
REPEAT the existing customer condition is not met:
	OUTPUT the string "Are you an existing customer?"
	INPUT user inputs yes or no
	
	IF INPUT is yes THEN:
		OUTPUT the string "please enter your email"
		INPUT user inputs the email
	ELSE INPUT not yes THEN:
		OUTPUT the string "create an account by entering your email"
		INPUT users inputs their email to make a new account.
	ENDIF
	
	STORE account type of New or Existing customer
UNTIL existing customer condition met
```

### Vehicle Select Utility
```text
REPEAT Ask for user input
	OUTPUT = "Input vehicle type"
	INPUT user enters vehicle type

	IF INPUT is a valid type:
		Input is valid
	ELSE:
		continue
	ENDIF

	STORE INPUT
UNTIL Input is Valid
```

### Hire Days Utility
```text
REPEAT
	OUTPUT = "State how many hire days you need, from 1 - 10 days. If you hire more than 7 days you will receive a 10% discount off the total hire cost"
	INPUT / Validate
	SELECT = More than 7 hire days / Less than 7 hire days
	IF > 7 = 10% discount off total hire cost
UNTIL
```

### Insurance Utility
```text
REPEAT
	OUTPUT = "Insurance?"
	INPUT = YES - NO / Validate
	SELECT = YES / NO
	IF YES = STORE INPUT = add £15.50 to total hire cost
	ELSE CONTINUE
UNTIL
```

### Return Utility
```text
PROCESS TOTAL
	SELECT  = Is new / Is existing customer
	IF YES = CHECK Loyalty card/Membership type

	IF MEMB = GOLD && Vehicle TYPE = HP:
		ADD additional £18 discount
	ADD Returnable deposit + total hire cost
RETURN TOTAL
```
	

### END the program