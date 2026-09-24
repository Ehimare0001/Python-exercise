print("1. Phone book");
print("2. Messages");
print("3. Chat");
print("4. Call register");
print("5. Tones");
print("6. Settings");
print("7. Call divert");
print("8. Music");
print("9. Games");
print("10. Calculator");
print("11. Reminders");
print("12. Clock");
print("13. Profiles");
print("14. Services");
print("15. SIM services");

number = int(input("Enter number: "))
             
if number == 1:
        
    print("Phone book"); 
    print("1. Search");
    print("2. Service Nos");
    print("3. Add name");
    print("4. Erase");
    print("5. Edit");
    print("6. Copy");
    print("7. Assign tone");
    print("8. Send b'card");
    print("9. Options");
    print("10. Speed dials");
    print("11. Voice tags");
      
    phone_book = int(input("Enter Phone Book number: "))
      
    if phone_book == 1:
        print("Search");
              
    elif phone_book == 2:               
        print("Service Nos");
              
    elif phone_book == 3:               
        print("Add name");
                            
    elif phone_book == 4:               
        print("Erase");
        
    elif phone_book == 5:               
        print("Edit");
        
    elif phone_book == 6:               
        print("Copy");
                      
    elif phone_book == 7:               
        print("Assign tone");
                            
    elif phone_book == 8:               
        print("Send b'card");
            
    elif phone_book == 9:               
        print("Options");
        print("1. Memory in use");
        print("2. Type of view");
        print("3. Memory status");
                      
        options = int(input("Enter Options number: "))
              
        if options == 1:               
            print("Memory");
              
        elif options == 2:               
            print("Type of view");
                          
        elif options == 3:               
            print("Memory status");  
    
        else:
                  
            print("Invalid options number");
                 
    elif phone_book == 10:               
        print("Speed dials");             
             
    elif phone_book == 11:               
        print("Voice tags");             
             
    else:           
        print("Invalid Phone Book number");
      
elif number == 2:
            
        print("Messages") 
        print("1. Write messages");
        print("2. Inbox");
        print("3. Outbox");
        print("4. Picture messages");
        print("5. Templates");
        print("6. Smiley");
        print("7. Message settings"); 
        
        messages = int(input("Enter Messages number: "))
     
        if messages == 1:
            print("Write messages");
            
        elif messages == 2:
            print("Inbox");
        
        elif messages == 3:
            print(" Outbox")            
                
        elif messages == 4:
            print("Picture messages");
            
        elif messages == 5:
            print("Templates")
            
        elif messages == 6:
            print("Smileys")           
                    
        elif messages == 7:
            print("Message settings")        
            print("1. Set 1");
            print("2. Common");         
          
            message_settings = int(input("Enter Message settings number: "))
          
            if message_settings == 1:
                print("Set 1");
                print("1. Message centre number");
                print("2. Message sent as");
                print("3. Message validity"); 
              
                set_1 = int(input("Enter Set 1 number: "))
              
                if set_1 == 1: 
                    print("Message centre number");
                
                elif set_1 == 2:                  
                    print("Message sent as");
                
                elif set_1 == 3:                    
                    print("Message validity");
            
                else:                  
                    print("Invalid Set 1 number");
                          
            elif message_settings == 2:                                
                print("Common");
                print("1. Delivery reports");
                print("2. Reply via same centre");
                print("3. Character support"); 
              
                common = int(input("Enter Common number: "))
              
                if common == 1:             
                    print("Delivery reports");
                    
                elif common == 2:
                    print("Reply via same centre");
                    
                elif common == 3:
                    print("Character support");                    
                    
                else:                
                    print("Invalid Common number");
             
            else:             
                print("Invalid Message Setting number");
         
        elif messages == 8:
            print(" Info service");            
        
        elif messages == 9:
            print("Voice mailbox number");
            
        elif messages == 10:
            print("Service command editor");         
     
        else:     
            print("Invalid Messages number"); 
    
elif number == 3:       
    print("Chat");
      
      
elif number == 4: 
    print("Call register");        
    print("1. Missed calls");
    print("2. Received calls");
    print("3. Dialled numbers");
    print("4. Erased recent call lists");
    print("5. Show call duration");
    print("6. Show call costs");
    print("7. Call cost settings");
    print("8. Prepaid credit");
        
    call_register = int(input("Enter Call register number: "))
    
    if call_register == 1:
        print("Missed calls");
      
    elif call_register == 2:
        print("Received calls");
                    
    elif call_register == 3:
        print("Dialled numbers");
                               
    elif call_register == 4:
        print("Erased recent call lists");
                                   
    elif call_register == 5:
        print("Show call duration");
        print("1. Last call duration");
        print("2. All calls' duration");
        print("3. Received calls' duration");
        print("4. Dialled call's duration");
        print("5. Clear timers");
        
        show_call_duration = int(input("Enter Show call duration number: "))
        
        if show_call_duration == 1:
            print("Last call duration");
                               
        elif show_call_duration == 2:
            print("All calls' duration");
                                         
        elif show_call_duration == 3:
            print("Received calls' duration");
            
        elif show_call_duration == 4:
            print("Dialled calls' duration");  
            
        elif show_call_duration == 5:
            print("Clear timers");
                                                                                
        else:
            print("Invalid Show call duration number");
            
    elif call_register == 6:
        print("Show call cost");
        print("1. Last call cost");
        print("2. All calls' cost");
        print("3. Clear counters");                               
            
        show_call_cost = int(input("Enter Show call cost number: "))
        
        if show_call_cost == 1:
            print("Last call cost");
            
        elif show_call_cost == 2:
            print("All calls' cost");
                        
        elif show_call_cost == 3:
            print("Clear counters");
            
        else: 
            print("Invalid Show call cost number");
                
    elif call_register == 7:
        print("Call cost settings");
        print("1. Call cost limit");
        print("2. Show costs in");
                
        call_cost_settings = int(input("Enter Call cost settings number: "))
        
        if call_cost_settings == 1:
            print("Call cost limits");
            
        elif call_cost_settings == 2:
            print("Show costs in");
            
        else:
            print("Invalid Call cost settings number");
            
    elif call_register == 8:
        print("Prepaid credit");
                
elif number == 5:                
    print("Tones");
    print("1. Ringing tone");
    print("2. Ringing volume");
    print("3. Incoming call alert");
    print("4. Message alert tone");
    print("5. Keypad tones");
    print("6. Warning tones");
    print("7. Vibrating alert");
    print("8. Screen saver");
    
    tones = int(input("Enter Tones number: "))
    
    if tones == 1:
        print("Ringing tone");
        
    elif tones == 2:
        print("Ringing volume");
      
    elif tones == 3:
        print("Incoming call alert");
        
    elif tones == 4:
        print("Message alert tone");        
        
    elif tones == 5:
        print("Keypad tones");
        
    elif tones == 6:
        print("Warning tones");    
        
    elif tones == 7:
        print("Vibrating alert");          
        
    elif tones == 8:
        print("Screen saver");           
        
    else:       
        print("Invalid Tones number"); 
        
elif number == 6:
    print("Settings");
    print("1. Call settings");
    print("2. Phone settings")
    print("3  Security settings");
    print("4. Restore factory settings");   
      
    settings = int(input("Enter Settings number: "))
          
    if settings == 1:
        print("Call settings");
        print("1. Automatic redial");
        print("2. Speed dialling");
        print("3. Call waiting options");
        print("4. Own number sending");
        print("5. Phone line in use");
        print("6. Automatic answer");
          
        call_settings = int(input("Enter Call settings number: "))
          
        if call_settings == 1:
            print("Automatic redial");
            
        elif call_settings == 2:
            print("Speed dialling");
                        
        elif call_settings == 3:
            print("Call waiting options");   
            
        elif call_settings == 4:
            print("Own number sending");  
            
        elif call_settings == 5:
            print("Phone line in use");
            
        elif call_settings == 6:
            print("Automatic answer");
            
        else:            
            print("Invalid call_settings number"); 
             
    elif settings == 2:                 
        print("Phone settings");
        print("1. Language");
        print("2. Cell info display");
        print("3. Welcome note");
        print("4. Network selection");
        print("5. Confirm SIM service action");         
        
        phone_settings = int(input("Enter Phone settings number: "))
          
        if phone_settings == 1:          
            print("Language");
                
        elif phone_settings == 2:          
            print("Cell info display");    
            
        elif phone_settings == 3:          
            print("Welcome note");    
                        
        elif phone_settings == 4:          
            print("Network selection");    
                        
        elif phone_settings == 5:          
            print("Confirm SIM service action"); 
            
        else:
            print("Invalid Phone settings number");
                
    elif settings == 3:               
        print("Security settings");
        print("1. PIN code request");
        print("2. Call barring service");
        print("3. Fixed dialling");
        print("4. Closed user group");
        print("5. Security level");  
        print("6. Change access codes");             
          
        security_settings = int(input("Enter Security settings number: "))
        
        if security_settings == 1:          
            print("PIN code request");
           
        elif security_settings == 2:           
            print("Call barring service");
                
        elif security_settings == 3:           
            print("Fixed dialling");
            
        elif security_settings == 4:           
            print("Closed user group");
            
        elif security_settings == 5:           
            print("Security level");
            
        elif security_settings == 6:           
            print("Change access codes");
            
        else:
            print("Invalid Security settings number"); 
            
    elif settings == 4:               
        print("Restore factory setting");
         
elif number == 7:  
    print("call divert");
    
elif number == 8:
    print("Music");
    print("1. Music player");
    print("2. Radio");
    print("3  Recorder");
    print("4. Track list");   
      
    music = int(input("Enter Music number: "))
    
    if music == 1:
        print("Music player");
     
    elif music == 2:
        print("Radio");
        
    elif music == 3:
        print("Recorder");

    elif music == 4:
        print("Track list");

    else:
        print("Invalid Music number"); 
        
elif number == 9:  
    print("Games");        
        
elif number == 10:  
    print("Calculator");        
        
elif number == 11:  
    print("Reminders");    
    
elif number == 12:  
    print("Clock");    
    print("1. Alarm clock");
    print("2. Clock setting");
    print("3. Data setting");
    print("4. Stopwatch");
    print("5. Countdown timer");  
    print("6. Auto update of date and time");             
          
    clock = int(input("Enter Clock number: "))
     
    if clock == 1:
        print("Alarm clock");
    
    elif clock == 2:
        print("Clock setting");
        
    elif clock == 3:
        print("Data setting");
                  
    elif clock == 4:
        print("Stopwatch");
     
     
    elif clock == 5:
        print("Countdown timer");
                    
    elif clock == 6:
        print("Auto update and time");
                      
    else:                
        print("Invalid Clock number"); 
       
elif number == 13:  
    print("Profiles");        
        
elif number == 14:  
    print("Services");        
        
elif number == 15:  
    print("SIM services");   

else:
    print("Invalid number");


        
                          
      
