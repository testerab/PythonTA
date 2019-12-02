from termcolor import colored
asia_destinations = {"Azerbaijan" : [300.00, 300.00, 0.00], "Georgia" : [270.00, 270.00, 0.00], "Japan" : [600.00, 600.00, 0.00], "Malaysia" : [625.00, 625.00, 0.00], "Myanmar" : [590.00, 590.00, 0.00], "Singapore" : [625.00, 652.00, 0.00], "Tajikistan" : [495.00, 495.00, 0.00], "Turkmenistan" : [495.00, 495.00, 0.00], "Bangladesh" : [525.00, 525.00, 0.00], "Cambodia" : [550.00, 550.00, 0.00], "India" : [465.00, 465.00, 0.00], "Kazakhstan" : [495.00, 495.00, 0.00], "Kyrgyzstan" : [480.00, 480.00, 0.00], "Maldives": [750.00, 750.00, 0.00], "Nepal" : [525.00, 525.00, 0.00], "Sri Lanka" : [725.00, 725.00, 0.00], "Thailand" : [800.00, 800.00, 0.00], "Uzbekistan" : [615.00, 615.00, 0.00], "Bhutan" : [530.00, 530.00, 0.00], "China" : [790.00, 790.00, 0.00], "Indonesia" : [680.00, 680.00, 0.00], "North Korea" : [618.00, 618.00, 0.00], "Laos" : [634.00, 634.00, 0.00], "Mongolia" : [678.00, 678.00, 0.00], "Philippines" : [698.00, 698.00, 0.00], "Taiwan" : [790.00, 790.00, 0.00], "Timor Leste" : [725.00, 725.00, 0.00], "Vietnam" : [693.00, 693.00, 0.00]}
australasia_destinations = {"Australia" : [824.00, 824.00, 0.00], "Cook Islands" : [798.00, 798.00, 0.00], "Fiji" : [796.00, 796.00, 0.00], "French Polynesia" : [725.00, 725.00, 0.00], "Kiribati" : [798.00, 798.00, 0.00], "New Caledonia" : [698.00, 698.00, 0.00], "New Zealand" : [823.00, 823.00, 0.00], "Papua New Guinea" : [724.00, 724.00, 0.00], "Samoa" : [713.00, 713.00, 0.00], "Tonga" : [711.00, 711.00, 0.00], "Vanuatu" : [705.00, 705.00, 0.00]}

def welcome_message():
  print(colored("/////////////////////////////////////////////////////////////", "blue"))
  print("\n")
  print(colored("             Welcome to SKYs UR Limit", "green"))
  print("\n")
  print(colored("/////////////////////////////////////////////////////////////", "blue"))
  print("\n")

def destination_flight():
  region_choice_valid = "N"
  region = ""
  while region_choice_valid == "N":
    try:
      region_choice = int(input("\n \n Please choose which region you want to visit \n\n 1) Asia \n 2) Australasia \n\n Choice: "))
      if region_choice == 1:
          region_choice_valid = "Y"
          region = "Asia"
      elif region_choice == 2:
          region_choice_valid = "Y"
          region = "Australasia"
      else:
        region_choice_valid = "N"
        print(colored("\nWe don't fly to that region yet. Please try again!","yellow"))
    except ValueError:
      print(colored("Please enter '1' for Asia or '2' for Australasia.", "yellow")) 

  valid_destination = "N"
  while valid_destination == "N": 
      if region == "Asia":
        print("\n \nHere are our destinations in " + region + ": " + "\n \n" + ', '.join(asia_destinations.keys()))
        destination_choice = input("\nWhere would you like to fly? ")
      elif region == "Australasia":
        print("\n \nHere are our destinations in " + region + ": " + "\n\n" + ', '.join(australasia_destinations.keys())+ "\n") 
        destination_choice = input("Where would you like to fly? ")
      if destination_choice.title() in asia_destinations:
        valid_destination = "Y"
        return asia_destinations.get(destination_choice.title())
      elif destination_choice.title() in australasia_destinations:
        valid_destination = "Y"
        return australasia_destinations.get(destination_choice.title())
      else:
        valid_destination = "N"
        print(colored("We do not fly there yet! (You might need to check your spelling!)", "yellow"))

def total_travellers():
  adults = 0
  children = 0
  infants = 0
  adults_valid = "N"
  children_choice_valid = "N"
  children_valid = "N"
  infant_choice_valid = "N"
  infants_valid = "N"

  while adults_valid == "N":
    try:
      adults = int(input("Please enter the number of adults (age 18+) travelling: "))
      if adults >= 1:
        adults_valid = "Y"
    except ValueError:
      print(colored("Oops, please try again!", "yellow"))
  
  while children_choice_valid == "N":
    travelling_with_children = input("\nAre you travelling with children aged 2-17 years of age? (Y/N): ")
    if travelling_with_children.upper() == "Y":
      children_choice_valid = "Y"
      while children_valid == "N":
          try:
              children = int(input("Please enter the number of children travelling: "))
              if children >= 1:
                children_valid = "Y"
          except ValueError:
            print(colored("Oops, please try again!", "yellow"))
    elif travelling_with_children.upper() == "N":
      children_choice_valid = "Y"
      children = 0
    else:
      print(colored("Please enter either 'Y' for yes or 'N' for no.", "yellow"))
      children_choice_valid = "N"
      children = 0
  
  while infant_choice_valid == "N":
    travelling_with_infants = input("\nAre you travelling with infants aged 0-2 years of age? (Y/N): ")
    if travelling_with_infants.upper() == "Y":
      infant_choice_valid = "Y"
      while infants_valid == "N":
        try:
            infants = int(input("Please enter the number of infants travelling: "))
            if infants >= 1:
              infants_valid = "Y"
        except ValueError:
          print(colored("Oops, try again!", "yellow"))
    elif travelling_with_infants.upper() == "N":
      infant_choice_valid = "Y"
      infants = 0
    else:
      print(colored("Please enter either 'Y' for yes or 'N' for no.", "yellow"))
      infant_choice_valid = "N"
      infants = 0
  total = adults + children + infants
  return adults, children, infants, total

def duration_calculator():
  duration_valid = "N"
  while duration_valid == "N":
    try:
      total_duration = int(input("\nPlease enter the number of nights for your trip: "))
      return total_duration
    except ValueError:
      print(colored("\nOops, try again. Please enter a number", "yellow"))

def airport_parking_calculator():
  parking_charge = 0.00
  per_day_parking_cost = 15.00
  num_of_cars = 0
  parking_choice_valid = "N"
  car_num_valid = "N"
  while parking_choice_valid == "N":
    parking_required = input("\nDo you require airport parking? (Y/N): ")
    if parking_required.upper() == "Y":
      parking_choice_valid = "Y"
      while car_num_valid == "N":
        try:
          num_of_cars = int(input("Number of cars (£15 per car, per day): "))
          if num_of_cars >= 1:
            car_num_valid = "Y"
            parking_charge = num_of_cars * per_day_parking_cost
          else:
            car_num_valid = "N"
        except ValueError:
          print(colored("Oops, try again!", "yellow"))
    elif parking_required == "N":
      parking_choice_valid = "Y"
      num_of_cars = 0
    else:
      print(colored("Please enter either 'Y' for yes or 'N' for no.", "yellow"))
      parking_choice_valid = "N"
  return parking_charge, num_of_cars

def holiday_pricer():
  welcome_message()
  travellers = total_travellers()
  flight = destination_flight()
  days = duration_calculator()
  basic_cost_adults = (flight[0] * travellers[0])
  basic_cost_children = (flight[1] * travellers[1])
  basic_cost_total = basic_cost_adults + basic_cost_children
  def baggage_calculator():
    standard_15kg_bag = 25.00
    standard_23kg_upgrade_bag = 30.00
    excess_15kg_bag = 25.00
    excess_23kg_bag = 30.00
    number_of_standard_15kg_bags = 0
    number_of_upgrade_23kg_bags = 0
    number_of_excess_15kg_bags = 0
    number_of_excess_23kg_bags = 0 
    total_cost_standard = 0
    total_cost_upgrade = 0
    total_cost_excess_standard = 0
    total_cost_excess_upgrade = 0
    standard_allowance = travellers[0] + travellers[1] 
    standard_choice_valid = "N"
    upgrade_choice_valid = "N"
    extra_standard_choice_valid = "N"
    extra_upgrade_choice_valid = "N"
    standard_number_valid = "N"
    upgrade_number_valid = "N"
    extra_standard_number_valid = "N"
    extra_upgrade_number_valid = "N"
    
      
    print(colored("\nAdults and children (excluding infants) are entitled to one standard 15kg bag each at a cost of £{:0,.2f} per bag. You may opt to upgrade your standard baggage to a 23kg bag at the cost of £{:0,.2f} per bag. Additional bags are charged at £{:0,.2f} for a standard bag or £{:0,.2f} for a upgraded bag. \n".format(standard_15kg_bag, standard_23kg_upgrade_bag, excess_15kg_bag, excess_23kg_bag), "magenta"))
    
    while standard_choice_valid == "N":
        standard_baggage_required = input("\nDo you require standard baggage? (Y/N): ")
        if standard_baggage_required.upper() == "Y":
          standard_choice_valid = "Y"
          while standard_number_valid == "N":
            try:
              number_of_standard_15kg_bags = int(input("Please enter the number of standard 15kg bags that you require: "))
              if number_of_standard_15kg_bags >= 1 and number_of_standard_15kg_bags <= standard_allowance:
                standard_number_valid = "Y"
                standard_allowance = standard_allowance - number_of_standard_15kg_bags
                total_cost_standard = (number_of_standard_15kg_bags * standard_15kg_bag)
              elif number_of_standard_15kg_bags > standard_allowance:
                print(colored("You are only entitled to one bag per adult or child. Infants do not have a baggage allowance.", "yellow"))
                standard_number_valid = "N"
              else:
                standard_number_valid = "N"
            except ValueError:
              print(colored("Oops! Please enter a number!", "yellow"))
        elif standard_baggage_required.upper() == "N":
          standard_choice_valid = "Y"
        else:
          print(colored("Please enter 'Y' for yes or 'N' for no.", "yellow"))
          standard_choice_valid = "N"

    while upgrade_choice_valid == "N":
        standard_upgrade_baggage_required = input("\nDo you require any upgraded 23kg bags? (Y/N): ")
        if standard_upgrade_baggage_required.upper() == "Y":
          upgrade_choice_valid = "Y"
          while upgrade_number_valid == "N":
            try:
              number_of_upgrade_23kg_bags = int(input("Please enter the number of upgraded suitcases that you require: "))
              if number_of_upgrade_23kg_bags >= 1 and number_of_upgrade_23kg_bags <= standard_allowance:
                  upgrade_number_valid = "Y"
                  total_cost_upgrade = (number_of_upgrade_23kg_bags * standard_23kg_upgrade_bag)
              elif number_of_upgrade_23kg_bags > standard_allowance:
                  print(colored("You are only entitled to one bag per adult or child. Infants do not have a baggage allowance.", "yellow"))
                  standard_number_valid = "N"
              else:
                  upgrade_number_valid = "N"
            except ValueError:
                  print(colored("Oops! Please enter a number!", "yellow"))
        elif standard_upgrade_baggage_required.upper() == "N":
          upgrade_choice_valid = "Y"
        else:
          standard_number_valid = "N"
          print(colored("Please enter 'Y' for yes or 'N' for no.", "yellow"))
          upgrade_choice_valid = "N"

    while extra_standard_choice_valid == "N":
        extra_standard_baggage_required = input("\nDo you require extra 15kg baggage? (Y/N): ")
        if extra_standard_baggage_required.upper() == "Y":
          extra_standard_choice_valid = "Y"
          while extra_standard_number_valid == "N":
            try:
              number_of_excess_15kg_bags = int(input("Please enter the number of extra 15kg suitcases requires: "))
              if number_of_excess_15kg_bags >= 1:
                extra_standard_number_valid = "Y"
                total_cost_excess_standard = (number_of_excess_15kg_bags * excess_15kg_bag)
              else:
                extra_standard_number_valid = "N"
            except ValueError:
              print(colored("Oops! Please enter a number!", "yellow"))
        elif extra_standard_baggage_required.upper() == "N":
          extra_standard_choice_valid = "Y"
        else:
          print(colored("Please enter 'Y' for yes or 'N' for no.", "yellow"))
          extra_standard_choice_valid = "N"

    while extra_upgrade_choice_valid == "N":
        extra_upgrade_baggage_required = input("\nDo you require extra 23kg baggage? (Y/N): ")
        if extra_upgrade_baggage_required.upper() == "Y":
          extra_upgrade_choice_valid = "Y"
          while extra_upgrade_number_valid == "N":
            try:
              number_of_excess_23kg_bags = int(input("Please enter the number of upgraded extra suitcases: "))
              if number_of_excess_23kg_bags >= 1:
                extra_upgrade_number_valid = "Y"
                total_cost_excess_upgrade = (number_of_excess_23kg_bags * excess_23kg_bag)
              else:
                extra_upgrade_number_valid = "N"
            except ValueError:
              print(colored("Oops! Please enter a number!", "yellow"))
        elif extra_upgrade_baggage_required.upper() == "N":
          extra_upgrade_choice_valid = "Y"
        else:
          print(colored("Please enter 'Y' for yes or 'N' for no.", "yellow"))
          extra_upgrade_choice_valid = "N"
    
     
    return number_of_standard_15kg_bags, total_cost_standard, number_of_upgrade_23kg_bags, total_cost_upgrade, number_of_excess_15kg_bags, total_cost_excess_standard, number_of_excess_23kg_bags, total_cost_excess_upgrade
  baggage = baggage_calculator()
  total_baggage_cost = (baggage[1] + baggage[3] + baggage[5] + baggage[7])
  parking = airport_parking_calculator()
  def travel_insurance_calculator():
    cost_7_days = 25.00
    cost_7_to_21_days = 50.00
    cost_over_21_days = 70.00
    duration = days
    insurance_choice_valid = "N"
    insurance_number_valid = "N" 

    while insurance_choice_valid == "N":
        travel_insurance_required = input("\nDo you require travel insurance?(Y/N): ")
        if travel_insurance_required.upper() == "Y":
          insurance_choice_valid = "Y"
          while insurance_number_valid == "N": 
            try:
              if duration >= 1 and duration <= 7:
                insurance_number_valid = "Y" 
                insurance_cost = cost_7_days * travellers[3]
              elif duration > 7 and duration < 21:
                insurance_number_valid = "Y"
                insurance_cost = cost_7_to_21_days * travellers[3]
              else:
                insurance_number_valid = "Y"
                insurance_cost = cost_over_21_days * travellers[3]
            except ValueError:
              print(colored("Oops, please enter a number.", "yellow"))
        elif travel_insurance_required.upper() == "N":
              insurance_choice_valid = "Y"    
        else:
          print(colored("Please enter either 'Y' for yes or 'N' for no.", "yellow"))
          insurance_choice_valid = "N"
    return insurance_cost 
  insurance = travel_insurance_calculator()
  parking_price = (parking[0] * parking[1]) * days
  number_of_cars = parking[1]
  commission_cost = basic_cost_total + total_baggage_cost + insurance
  commission = commission_cost * 0.01
  total_price = basic_cost_total + total_baggage_cost + insurance + parking_price + commission
  def budget_checker():
    budget = input("\nWhat is your overall budget for this trip? £")
    budget_fixed = float(budget.replace(",",""))
    budget_choice_valid = "N"
    if total_price <= budget_fixed:
      print("\033[1m\nYour holiday is within budget!\033[0m")
    else:
      print("\033[1m\nYour chosen destination is not in budget\033[0m")
    while budget_choice_valid == "N":
        see_suggestions = input("\nWould you like to see a list of other destinations that are in your budget? (Y/N): ")
        if see_suggestions.upper() == "Y":
            budget_choice_valid = "Y" 
            in_budget_destinations_asia = []
            out_of_budget_destinations_asia = []
            in_budget_destinations_australasia = []
            out_of_budget_destinations_australasia = []
            for destination in asia_destinations:
              cost = (asia_destinations.get(destination)[0] * travellers[0]) + (asia_destinations.get(destination)[1] * travellers[1]) + total_baggage_cost + insurance + parking_price + commission
              if cost <= budget_fixed:
                in_budget_destinations_asia.append(destination)
              else:
                out_of_budget_destinations_asia.append(destination)
            for destination in australasia_destinations:
              cost = (australasia_destinations.get(destination)[0] * travellers[0]) + (australasia_destinations.get(destination)[1] * travellers [1]) + total_baggage_cost + insurance + parking_price + commission
              if cost <= budget_fixed:
                in_budget_destinations_australasia.append(destination)
              else:
                out_of_budget_destinations_australasia.append(destination)
            return print( "\n \033[1mHere is a list of other destinations in your budget in Asia:\033[0m \n \n {}".format(", ".join(in_budget_destinations_asia)) + "\n \n \033[1mHere is a list of destinations in your budget in Australasia:\033[0m \n \n {}".format(", ".join(in_budget_destinations_australasia)))
        elif see_suggestions.upper() == "N":
          print("Please come again")
          budget_choice_valid = "Y"
        else:
          budget_choice_valid = "N"
          print(colored("Please enter either 'Y' for yes or 'N' for no.", "yellow"))
  budget_checker()
  def summary_printer():
      print("\n" + "\033[1mHoliday summary: \033[0m" + "\n")  
      print("\n" + "\033[1mPlease see below for a breakdown of your holiday costs: \033[0m" + "\n")
      print("\033[1mTotal flight cost:                             £{:0,.2f}\033[0m".format(basic_cost_total))
      print("  Price per adult:                               £{:0,.2f}".format(flight[0]))
      print("  Number of Adults:                                    {}".format(travellers[0]))
      print("  Price per child:                               £{:0,.2f}".format(flight[1]))
      print("  Number of Children:                                  {}".format(travellers[1]))
      print("  Price per infant:                                £0.00")
      print("  Number of Infants:                                   {}".format(travellers[2]))
      print("\033[1mTotal baggage cost:                              £{:0,.2f}\033[0m".format(total_baggage_cost))
      print("  No. of standard 15kg bags:                           {}".format(baggage[0]))
      print("  Cost of standard baggage:                       £{:0,.2f}".format(baggage[1]))
      print("  No. of upgraded standard 23kg bag                    {}".format(baggage[2]))
      print("  Cost of upgraded baggage:                       £{:0,.2f}".format(baggage[3]))
      print("  No. of extra 15kg bags:                              {}".format(baggage[4]))
      print("  Cost of extra 15kg baggage:                     £{:0,.2f}".format(baggage[5]))
      print("  No. of extra 23kg bags:                              {}".format(baggage[6]))
      print("  Cost of extra 23kg baggage:                     £{:0,.2f}".format(baggage[7]))
      print("\033[1mTotal Insurance cost:                            £{:0,.2f}\033[0m".format(insurance))
      print("\033[1mTotal Parking Charge:                            £{:0,.2f}\033[0m". format(parking_price))
      print("  Duration(nights):                                    {} ".format(days))
      print("  No.of cars:                                          {}".format(number_of_cars))
      print("\033[1mCommission Charge:                                £{:0,.2f}\033[0m".format(commission))
      print("(parking not included)")
      print(colored("\n \033[1mYour total cost is:                            £{:0,.2f}\033[0m","red").format(total_price) + "\n")
  summary_printer()
     
  
holiday_pricer()

Initial versionJD
