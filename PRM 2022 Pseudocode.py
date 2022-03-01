#https://www.youtube.com/channel/UC9S3DDVJNbN1ILrV0HTUn6w
#-Awab Aqib

#################### PSEUDOCODE ############################
#Task 1
tkt_type <- 	  ["0. One adult","1. One child","2. One senior","3. Family","4. Group ><-6"]
type_counts <- 	  [		0,				0,				0,			0,				0]

DECLARE ticketprice : REAL
DECLARE bookingnum, rpt, famcount : INTEGER

rpt <- 1
famcount <- 1
ticketprice <- 0.00
bookingnum <- 0

day1_cost <- [		20.00,			12.00,			16.00,		60.00, 			15.00]
day2_cost <- [		30.00,			18.00,			24.00,		90.00,			22.50]

attraction <- ["0. Lion feeding","1. Penguin Feeding","2. Barbecue(2Day)" ]
att_cost <-  	[2.50, 				2.00, 				5.00, 				]
attraction_count <- [0,					0,					0 			]



WHILE(rpt <> 0)
	#summary of tickets
	PRINT("Ticket Type($)     Day One Cost($)     Day Two Cost($)")
	FOR index <- 1 TO 5
		PRINT(tkt_type[index])
  		PRINT(day1_cost[index])
		PRINT(day2_cost[index])
	NEXT index
	ENDFOR

	#printing attractions
	PRINT("Extra attraction      Cost($)")
	FOR index <- 1 TO 3
		PRINT(attraction[index]
		PRINT(att_cost[index])
	NEXT index
	ENDFOR

	#printing available days
	day <- INPUT("Enter today's day (1-31) ")
	WHILE(day<1 OR day>31)
		day <- INPUT("Enter today's day (1-31) ")
	ENDWHILE

	PRINT("Tickets are available on days ")
 
 	startday <- day 

	FOR j <- 1 TO 7
		IF(day = 31)
			day <- 0
		ENDIF
		day <- day + 1
		PRINT(day)

	NEXT j
	ENDFOR

	endday <- day

	bookingday <- INPUT("Enter a booking day available above ")
	WHILE(bookingday < startday OR bookingday > endday )
		bookingday <- INPUT("Enter a booking day available above ")
	ENDWHILE

	#############Task 2################

	#selecting the day
	daycount <- INPUT("Enter 1 for 1-day booking or 2 for 2-day booking ")
	WHILE(daycount <> 1 AND daycount <> 2)
 		PRINT("Invalid day selected!")
		daycount <- INPUT("Enter 1 for 1-day booking or 2 for 2-day booking ")
	ENDWHILE

	#booking the tickets
	tkt_INPUT <- INPUT("Select options from 0 - 4 to book ticket(s) or -1 to end booking ")
	WHILE(tkt_INPUT <> -1)
		IF(tkt_INPUT = 0)
			adultcount <- INPUT("Count of adults ")
			PRINT(tkt_type[0])
			type_counts[0] <- type_counts[0] + adultcount

		ELSEIF(tkt_INPUT = 1)
			IF(type_counts[0] <= 0):
				PRINT("You can't buy a ticket without an adult!")
			
			ELSE
				maxchallowed <- type_counts[0] * 2
				PRINT("Maximum count of children allowed:", maxchallowed)
				childcount <- INPUT("Count of children: ")
				
				WHILE(maxchallowed > childcount)
					PRINT("Maximum count of children allowed:", maxchallowed)
					childcount <- INPUT("Count of children: ")

				type_counts[1] <- type_counts[1] + childcount
			ENDIF

		ELSEIF(tkt_INPUT = 2)
			sencount <- INPUT("Count of seniors ")
			PRINT(tkt_type[2])
			type_counts[2]<- type_counts[2] + sencount

		ELSEIF(tkt_INPUT = 3 OR tkt_INPUT = 4)
			adultmax <- 0
			childmax <- 0

			totalcount <- INPUT("Enter total number of tickets needed ")
			IF(totalcount >= 6 )
				type_counts[4] <- type_counts[4] + totalcount
			
			IF(tkt_INPUT = 3)
				famcount <- INPUT("Enter how many family tickets you want ")
				type_counts[3] <- type_counts[3] + famcount

				adultmax <- famcount * 2
				childmax <- famcount * 3

				PRINT("Max adults allowed",adultmax)
				PRINT("Max children allowed",childmax)

				adultcount <- INPUT("Count of adults/seniors ")
				childcount <- INPUT("Count of children ")
				totalcount <- adultcount + childcount
			
				WHILE(adultcount > adultmax OR childcount > childmax)
					adultcount <- INPUT("Count of adults/seniors ")
					childcount <- INPUT("Count of children ")
				ENDWHILE


			IF(tkt_INPUT = 4)
				adultcount <- INPUT("Count of adults/seniors ")
				childcount <- INPUT("Count of children ")
				totalcount <- adultcount + childcount
				
				WHILE(totalcount<6)
					adultcount <- INPUT("Count of adults/seniors ")
					childcount <- INPUT("Count of children ")
					totalcount <- adultcount + childcount
				ENDWHILE
				
				type_counts[3] <- type_counts[3] + (totalcount/5)


		ELSE
			PRINT("Only select an option between 0 and 4.")

		ENDIF

		#selecting whether user wants extra attractions or not
		extra <- INPUT("\nEnter 1. if you want extra attractions or 0 if you don't ")
		WHILE(extra <> 0 and extra <> 1)
			extra <- INPUT("Enter 1. if you want extra attractions or 0 if you don't ")
		ENDWHILE

		IF(extra = 1)
			attchoice <- INPUT("Select options from 0 - 2 to buy extra attraction ")
			WHILE(attchoice <0 and attchoice>2)
				attchoice <- INPUT("Select options from 0 - 2 to buy extra attraction ")
			ENDWHILE

			WHILE(daycount =1 and (attchoice<>0 AND attchoice<>1))
				PRINT("You are only allowed options 0. and 1. for Day 1.")
				attchoice <- INPUT("Select options 0 or 1 to buy extra attraction ")
			ENDWHILE

			WHILE(daycount=2 AND (attchoice<0 AND attchoice>2)
				PRINT("You must selected 0,1 or 2 options.")
				attchoice <- INPUT("Select option 2 to buy extra attraction ")
			ENDWHILE

			IF(tkt_INPUT = 3)
				extrascost <- totalcount * att_cost[attchoice]			
				attraction_count[attchoice] <- attraction_count[attchoice] + totalcount
			
			ELSE
				extrascost <- type_counts[tkt_INPUT] * att_cost[attchoice]			
				attraction_count[attchoice] <- attraction_count[attchoice] + type_counts[tkt_INPUT]

			ENDIF

		ELSE
			extrascost <- 0

		ENDIF


		#finding the ticketprice based on the counts of ticket and the costs
		IF(daycount = 1)
			currtotal <- (type_counts[tkt_INPUT] * day1_cost[tkt_INPUT]) + extrascost

		ELSE
			currtotal <- (type_counts[tkt_INPUT] * day2_cost[tkt_INPUT]) + extrascost
		ENDIF	

		
		ticketprice <- ticketprice + currtotal	
		PRINT("****CURRENT TICKET PRICE****",ticketprice)

		altprice <- 0
		IF(tkt_input = 3 or tkt_input = 4)
			IF(tkt_input = 3):
				altprice = (type_counts[4] * day1_cost[4]) + extrascost
				print("****ALTERNATE TICKET PRICE****:",altprice)

			ELSEIF(tkt_input = 4):
				altprice = (type_counts[3] * day1_cost[3]) + extrascost
				print("****ALTERNATE TICKET PRICE****:",altprice)
			ENDIF

			choice = input("Enter 1. to accept alternate price or 0. to not: ")
			IF(choice = 1):
				ticketprice = altprice
			ENDIF

		tkt_INPUT <- INPUT("\nSelect options from 0 - 4 to book ticket(s) or -1 to end booking ")

	################################3

	bookingnum <- bookingnum + 1
	PRINT("Unique Booking Number",bookingnum)
	
	#same for printing other arrays
	FOR index <- 1 TO 5
		PRINT(tkt_type)
	NEXT index 
	ENDFOR


	PRINT("Total ticket price",ticketprice)

	rpt <- INPUT("\nEnter 1. if you want to book another or 0. to exit ")

ENDWHILE