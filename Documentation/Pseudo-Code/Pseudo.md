### START the program

### Existing Customer Utility
```text
REPEAT the existing customer condition is not met:
	OUTPUT the string "Are you an existing customer?"
	INPUT user inputs yes or no
	
	IF INPUT is yes THEN:
		OUTPUT the string "please state your membership type"
		INPUT user inputs membership type
	ENDIF
	
	STORE account type of New or Existing customer
UNTIL existing customer condition met
```

### Vehicle Select Utility
```text
REPEAT Ask for user input till input valid == True
	OUTPUT = "Please enter the vehicle you wish to hire - Choice: s - saloon, hp - high performance, v - van"
	INPUT user enters vehicle type

	IF INPUT is a valid type:
		Input valid = True
	ENDIF

	STORE INPUT
UNTIL Input is Valid
```

### Hire Days Utility
```text
REPEAT valid input == True
	OUTPUT = "State how many hire days you need, from 1 - 10 days. If you hire more than 7 days you will receive a 10% discount off the total hire cost"
	INPUT / Validate
	IF input valid:
		SELECT = More than 7 hire days / Less than 7 hire days
		IF > 7 = 10% discount off total hire cost
		ENDIF
		valid input = True
	ENDIF
UNTIL
```

### Insurance Utility
```text
REPEAT
	OUTPUT = "Insurance?"
	INPUT = YES - NO / Validate
	SELECT = YES / NO
	IF INPUT == YES:
		STORE INPUT = add £15.50 to total hire cost
	ENDIF
UNTIL
```

### Return Utility
```text
PROCESS TOTAL
	IF Is existing customer:
		CHECK Loyalty card/Membership type
	ENDIF
	
	IF MEMB = GOLD && Vehicle TYPE = HP:
		ADD additional £18 discount
	ADD Returnable deposit + total hire cost
RETURN TOTAL
```
	

### END the program