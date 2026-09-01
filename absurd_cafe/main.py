import json
import os
import random

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "cafe_data.json")
EMPLOYEE_PASSWORD = "pizza"

DEFAULT_DATA = {
    "products": {
        "1": {"name": "Giga-Burger 'Calorie Explosion'", "price": 20, "stock": 5, "type": "Food"},
        "2": {"name": "Spicy Shawarma (The Taste of Risk)", "price": 15, "stock": 8, "type": "Food"},
        "3": {"name": "Coffee 'Cold Deadline'", "price": 10, "stock": 15, "type": "Drinks"},
        "4": {"name": "Energy Drink 'DevOps Tears'", "price": 5, "stock": 3, "type": "Drinks"}
    },
    "users": {}, 
    "stats": {"total_failed_interrogations": 0},
    "graveyard": []
}

def load_database():
    if not os.path.exists(DB_FILE):
        save_database(DEFAULT_DATA)
        return DEFAULT_DATA
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("[System] Database read error. Loaded default cyber-cafe data.")
        return DEFAULT_DATA

def save_database(current_data):
    try:
        with open(DB_FILE, 'w') as f:
            json.dump(current_data, f, ensure_ascii=False, indent=4)
    except IOError:
        print("[System] Fatal error writing data to file!")

cafe_data = load_database()
shopping_cart = []
successful_meals_counter = 0

question_bank = [
    {
        "question": "Why do you want this burger? Answer honestly, who are you working for?!",
        "answers": [
            {"text": "1. I'm just hungry, I swear!", "score": 2, "reply": "\nHmph... Too simple. You must be a spy for a secret nutritionist cult!"},
            {"text": "2. My cat ordered me to buy it.", "score": 0, "reply": "\nAh, feline orders are legally binding. Question dismissed."},
            {"text": "3. To feed it to my left foot.", "score": 1, "reply": "\nAn unusual biological experiment. Fair enough."}
        ]
    },
    {
        "question": "Quick answer: are pineapples on pizza a crime against humanity?",
        "answers": [
            {"text": "1. Yes, it deserves immediate prison time!", "score": 0, "reply": "\nExcellent! Our security algorithms fully agree with you."},
            {"text": "2. No, it is sophisticated and delicious.", "score": 3, "reply": "\nCritical threat level detected! You are a potential culinary terrorist!"},
            {"text": "3. I prefer pizza topped with dumplings.", "score": 1, "reply": "\nThe security officer is shocked, but it's not illegal."}
        ]
    },
    {
        "question": "Prove you are human. What is 'Capybara' plus 'Two Dollars'?",
        "answers": [
            {"text": "1. That's impossible to add, it makes no sense.", "score": 2, "reply": "\nRobots always seek logic. A real human would say something silly!"},
            {"text": "2. One very wealthy and fluffy capybara.", "score": 0, "reply": "\nCaptcha passed. You are definitely human."},
            {"text": "3. It equals approximately 42.", "score": 1, "reply": "\nThe ultimate answer to life, the universe, and everything."}
        ]
    },
    {
        "question": "Our laser scanner shows you blinked 3 times in the last 10 seconds. What are you hiding?",
        "answers": [
            {"text": "1. I just have a speck of dust in my eye!", "score": 2, "reply": "\nThe classic excuse used by professional hackers!"},
            {"text": "2. I was sending a soup recipe using Morse code.", "score": 0, "reply": "\nThe officer writes down the recipe... Proceed."},
            {"text": "3. I wasn't blinking, I was sleeping on my feet.", "score": 1, "reply": "\nUnderstandable, DevOps life is tough."}
        ]
    },
    {
        "question": "If a tomato is a fruit, then is ketchup technically a smoothie?",
        "answers": [
            {"text": "1. Yes, and fries are just giant dipping straws.", "score": 0, "reply": "\nBrilliant mind. You are cleared of all suspicion."},
            {"text": "2. No, that's disgusting to think about.", "score": 2, "reply": "\nNo imagination. Exactly what an undercover spy would say."},
            {"text": "3. My lawyer advised me not to answer this question.", "score": 1, "reply": "\nFair enough. Moving on."}
        ]
    },
    {
        "question": "Which parallel universe did you arrive from today?",
        "answers": [
            {"text": "1. The one where Python codes itself.", "score": 0, "reply": "\nTake me with you, please! Next question."},
            {"text": "2. I am from this universe, the normal one.", "score": 2, "reply": "\n'Normal' is exactly what an alien invaders' manual suggests saying!"},
            {"text": "3. Earth-616, but my visa expired.", "score": 1, "reply": "\nI will have to inform the multiversal customs later."}
        ]
    },
    {
        "question": "What is the airspeed velocity of an unladen swallow?",
        "answers": [
            {"text": "1. What do you mean? An African or European swallow?", "score": 0, "reply": "\nAh, a person of culture! You pass this step automatically."},
            {"text": "2. 11 meters per second.", "score": 1, "reply": "\nToo precise. Did you look that up on your phone?!"},
            {"text": "3. Birds are not real, they are government drones.", "score": 0, "reply": "\nFinally, someone who knows the truth!"}
        ]
    },
    {
        "question": "Why is the sky blue instead of neon pink?",
        "answers": [
            {"text": "1. Rayleigh scattering of light in the atmosphere.", "score": 2, "reply": "\nToo smart! Stop hacking our atmosphere with physics!"},
            {"text": "2. Because developers forgot to change the default CSS theme.", "score": 0, "reply": "\nTrue. The universe is badly optimized anyway."},
            {"text": "3. Pink was out of stock during creation.", "score": 1, "reply": "\nLogically illogical. Approved."}
        ]
    },
    {
        "question": "Do you swear to eat your meal with dignity and not throw fries at other citizens?",
        "answers": [
            {"text": "1. I swear, I am a highly civilized person.", "score": 2, "reply": "\nHighly civilized people are the most dangerous hackers."},
            {"text": "2. I can make no promises if a fry-fight breaks out.", "score": 0, "reply": "\nHonesty is the best policy. I respect your chaotic nature."},
            {"text": "3. I only throw burgers, never fries.", "score": 1, "reply": "\nA waste of budget, but legally acceptable."}
        ]
    },
    {
        "question": "Spell 'Python' backwards while standing on one imaginary leg!",
        "answers": [
            {"text": "1. nohtyP! Done.", "score": 0, "reply": "\nImpressive micro-processing skills for a human."},
            {"text": "2. This is a text-based game, you can't see my leg.", "score": 2, "reply": "\nDo not break the immersion! +2 suspicion points!"},
            {"text": "3. P-Y-T-H-O-N... Wait, backwards?", "score": 1, "reply": "\nAt least you didn't crash the system."}
        ]
    },
    {
        "question": "Our database shows you haven't rated this cafe 5 stars yet. Explain yourself.",
        "answers": [
            {"text": "1. I will do it right now, please don't deport me!", "score": 1, "reply": "\nGood, but I'm watching you closely."},
            {"text": "2. Give me my food first, then we talk stars.", "score": 0, "reply": "\nA true capitalist negotiator. Accepted."},
            {"text": "3. Stars are just giant balls of burning gas.", "score": 2, "reply": "\nDon't get philosophical with me, criminal!"}
        ]
    },
    {
        "question": "If you mix hot chocolate and cold milk, do you get lukewarm chaos?",
        "answers": [
            {"text": "1. No, you get a delicious drink.", "score": 2, "reply": "\nYour lack of poetic vision is highly suspicious."},
            {"text": "2. You get a temporal anomaly that could tear the kitchen apart.", "score": 0, "reply": "\nExactly! The Chef will be warned."},
            {"text": "3. You get a dirty glass.", "score": 1, "reply": "\nPractical, but overly depressing."}
        ]
    },
    {
        "question": "Press Alt+F4 to receive a free secret sauce. Will you do it?",
        "answers": [
            {"text": "1. Nice try, I know it closes the application.", "score": 0, "reply": "\nAnti-phishing test passed. Good job."},
            {"text": "2. Let me type it into the console right now...", "score": 2, "reply": "\nPlease do not touch things you don't understand."},
            {"text": "3. What is an 'Alt' and why are there 4 of them?", "score": 1, "reply": "\nHarmless to the server, proceed."}
        ]
    },
    {
        "question": "Are you currently dreaming, or is this game your actual reality now?",
        "answers": [
            {"text": "1. This is definitely a dream, I will wake up soon.", "score": 1, "reply": "\nWake up, Neo... The burger has you."},
            {"text": "2. This is real life and I am genuinely trapped here.", "score": 0, "reply": "\nAcceptance is the first step to becoming a good customer."},
            {"text": "3. I am a script running inside a computer simulation.", "score": 3, "reply": "\nIntruders! An artificial entity is trying to steal our carbs!"}
                ]
    },
    {
        "question": "Choose a weapon to defend your burger from space pirates:",
        "answers": [
            {"text": "1. A plasma rifle from the year 3000.", "score": 2, "reply": "\nToo aggressive. You might damage the tables."},
            {"text": "2. A stale French baguette from last Tuesday.", "score": 0, "reply": "\nUltimate blunt force weapon. Approved by the Chef."},
            {"text": "3. Loud, high-pitched screaming.", "score": 1, "reply": "\nEffective, but the other guests will complain."}
        ]
    },
    {
        "question": "Is it true that you secretly prefer tea over coffee?",
        "answers": [
            {"text": "1. Yes, tea is superior and peaceful.", "score": 1, "reply": "\nFine, but coffee keeps the economy moving."},
            {"text": "2. No, coffee runs through my veins like electricity.", "score": 0, "reply": "\nWelcome to the club. One of us!"},
            {"text": "3. I drink boiled water to feel nothing.", "score": 2, "reply": "\nOkay, that is dark. Stay away from the knives."}
        ]
    },
    {
        "question": "If I give you a free donut, will you forget everything that happened here?",
        "answers": [
            {"text": "1. What happened where? I see no donut.", "score": 0, "reply": "\naster of espionage. The bribe worked perfectly."},
            {"text": "2. No, I will still tell the authorities about this interrogation!", "score": 3, "reply": "\nNo food for snitches! Lock him up!"},
            {"text": "3. Can I have two donuts instead?", "score": 1, "reply": "\nCorruption at its finest. I like your style."}
        ]
    },
    {
        "question": "How many lines of code are required to fix your life?",
        "answers": [
            {"text": "1. Just one: import happiness.", "score": 0, "reply": "\nWow. That actually brought a tear to my cybernetic eye."},
            {"text": "2. System cannot be fixed, total rewrite needed.", "score": 1, "reply": "\nHard reset initiated. Proceed."},
            {"text": "3. print('Hello World') and hope for the best.", "score": 2, "reply": "\nLazy coding architecture. Highly suspicious."}
        ]
    },
    {
        "question": "Where do you see yourself in 5 seconds?",
        "answers": [
            {"text": "1. Eating a burger right here.", "score": 0, "reply": "\nGood vision. Let's make it happen."},
            {"text": "2. Still stuck in this infinite loop of questions.", "score": 1, "reply": "\nShhh, don't spoil the code mechanics."},
            {"text": "3. In jail for assaulting an AI security guard.", "score": 2, "reply": "\nDon't test me, human."}
        ]
    },
    {
        "question": "Final check: Are you a good cop or a bad cop?",
        "answers": [
            {"text": "1. I am a hungry cop.", "score": 0, "reply": "\nThe best kind. Go get your snacks."},
            {"text": "2. I am the law!", "score": 2, "reply": "\nHey! Only Sylvester Stallone can say that!"},
            {"text": "3. I am just a guy who wanted a simple soda.", "score": 1, "reply": "\nSimplicity is a mask for professional criminals. Approved anyway."}
        ]
    }
]

def display_shopping_cart():
    print("\n" + "=" * 30)
    print("       YOUR SHOPPING CART     ")
    print("=" * 30)
    
    if not shopping_cart:
        print("[Empty] You haven't added any tasty items yet.")
        print("-" * 30)
        return 0

    current_total = 0
    for index, prod_id in enumerate(shopping_cart, 1):
        item = cafe_data["products"][prod_id]
        print(f"{index}. {item['name']} — {item['price']} euro")
        current_total += item['price']
    
    print("-" * 30)
    print(f"Total price so far: {current_total} euro")
    print("=" * 30 + "\n")
    return current_total

def run_interrogation(target_name):
    print("\n" + "!" * 60)
    print(f" CAFE SECURITY DETECTED SUSPICIOUS ACTIVITY!")
    print(f"Target '{target_name}' is currently being scrutinized.")
    print("Initiating maximum paranoia interrogation mode!")
    print("!" * 60 + "\n")

    suspicion = 0
    chosen_questions = random.sample(question_bank, 2)

    for index, q_data in enumerate(chosen_questions, 1):
        print(f"--- Absurd Question №{index} ---")
        print(q_data["question"])
        
        for ans in q_data["answers"]:
            print(ans["text"])
        
        while True:
            user_input = input(">> Choose your action (1-3): ").strip()
            if user_input in ["1", "2", "3"]:
                break
            print("Invalid input. Type 1, 2, or 3!")

        selected_ans = q_data["answers"][int(user_input) - 1]
        print(selected_ans["reply"])
        suspicion += selected_ans["score"]
        print(f"[Officer's Paranoia Level: {suspicion}/3]\n")

    print("--- INTERROGATION COMPLETED ---")
    if suspicion >= 3:
        return False  
    return True  

def enroll_forced_employee():
    print("\n" + "="*50)
    print("FORCED EMPLOYEE REGISTRATION SYSTEM")
    print("Since you cleared security, you are perfect for us.")
    print("Fill out the profile, you work here now!")
    print("="*50)
    
    emp_name = input("Enter your Name: ").strip()
    if not emp_name: emp_name = "Former Customer"
    emp_phone = input("Enter your Phone: ").strip()
    
    print("\nSelect your new ridiculous job title:")
    print("1. Junior Burger Patty Flipper\n2. Senior Expert in Mop Cleaning\n3. Director of Eating Leftovers")
    job_choice = input(">> Select position (1-3): ").strip()
    
    jobs = {"1": "Junior Burger Patty Flipper", "2": "Senior Expert in Mop Cleaning", "3": "Director of Eating Leftovers"}
    final_job = jobs.get(job_choice, "Unpaid Intern-Slave")

    cafe_data["users"][emp_phone] = {"name": emp_name, "purchases": 0, "address": f"Job: {final_job}"}
    save_database(cafe_data)

    print("\n")
    print(f"\nCONGRATULATIONS, {emp_name.upper()}! You are now a {final_job}! MARCH TO WORK!\n")
    print("\n")

def checkout_shopping_cart():
    global successful_meals_counter
    if not shopping_cart:
        print("Your cart is empty! Pick some food first.")
        return False

    display_shopping_cart()
    
    buyer_name = input("Enter your name for the official protocol: ").strip()
    if not buyer_name: buyer_name = "Suspicious Anonymous"

    passed = run_interrogation(buyer_name)

    if passed:
        for prod_id in shopping_cart:
            cafe_data["products"][prod_id]["stock"] -= 1
        print(f"\n🎉 SUCCESS! Your order is paid. Bon appétit, {buyer_name}!")
        shopping_cart.clear()
        successful_meals_counter += 1
        
        if successful_meals_counter >= 3:
            print("\n" +  f"\nOH NO! {buyer_name.upper()} ATE TOO MUCH FOOD!\nCause of death: Gluttony.\n" + "\n")
            cafe_data["graveyard"].append(buyer_name)
            successful_meals_counter = 0  
            save_database(cafe_data)
            return True  
        
        save_database(cafe_data)
    else:
        cafe_data["stats"]["total_failed_interrogations"] += 1
        shopping_cart.clear()
        save_database(cafe_data)
    return False


while True:
    print("="*40)
    print("||""      WELCOME TO ABSURD-CAFE        ""||")
    print("="*40)
    print("||"" 1. Menu (Order Food)               ""||")
    print("||"" 2. Kitchen Login (Admin Panel)     ""||")
    print("||"" 3. Leave Hungry (Exit Application) ""||")
    print("="*40)
    
    main_choice = input("Select an option (1-3): ").strip()
    
    if main_choice == "1":
        while True:
            print("\n"+"="*40)
            print("1. Menu\n2. Add Item to Cart\n3. View Current Shopping Cart\n4. Checkout Order (WARNING: SECURITY AHEAD!)\n5. Back to Main Menu")
            action = input("Action: ").strip()
            
            if action == "1":
                print("\n--- TODAY'S MENU ---")
                for prod_id, info in cafe_data["products"].items():
                    print(f"[{prod_id}] {info['name']} — {info['price']} euro (In Stock: {info['stock']})")
            elif action == "2":
                prod_id = input("Enter Food ID: ").strip()
                if prod_id in cafe_data["products"] and cafe_data["products"][prod_id]["stock"] > 0:
                    shopping_cart.append(prod_id)
                    print(f"'{cafe_data['products'][prod_id]['name']}' thrown into your cart!")
                else:
                    print("Item out of stock or wrong ID.")
            elif action == "3":
                should_kick_out = checkout_shopping_cart()
                if should_kick_out:
                    break
            elif action == "4":
                break

    elif main_choice == "2":
        if input("Enter secret Chef password: ").strip() != EMPLOYEE_PASSWORD:
            print("The kitchen is off-limits! Wrong password.")
            continue

        while True:
            print("\n--- KITCHEN BACKEND PANELS ---")
            print("1. Add New to Menu\n2. Restock Food Inventory\n3. View Security Logs & Staff\n4. GRAVEYARD: Dead from Overeating\n5. Back")
            admin_action = input("Action (1-5): ").strip()
            if admin_action == "1":
                new_id = input("Create unique ID for new item: ")
                cafe_data["products"][new_id] = {
                    "name": input("Food Name: "), "price": int(input("Price (euro): ")),
                    "stock": int(input("Portions prepared: ")), "type": "Food"
                }
                save_database(cafe_data)
                print("Recipe added successfully!")
            elif admin_action == "2":
                restock_id = input("Enter Food ID to restock: ")
                if restock_id in cafe_data["products"]:
                    cafe_data["products"][restock_id]["stock"] += int(input("How many portions delivered: "))
                    save_database(cafe_data)
                    print("Inventory restocked!")
            elif admin_action == "3":
                print(f"\n[Stats]: Kicked out without food: {cafe_data['stats']['total_failed_interrogations']} time(s).\n\n[Forced Cafe Staff List]:")
                for phone, user_info in cafe_data["users"].items():
                    if "Job:" in user_info["address"]:
                        print(f"- {user_info['name']} (Phone: {phone}) | {user_info['address']}")
            elif admin_action == "4":
                print("\n" + "\n     THE MEMORIAL OF FALLEN GLUTTONS\n")
                if not cafe_data["graveyard"]:
                    print("No one has died yet. Our food is safe.")
                for idx, dead_name in enumerate(cafe_data["graveyard"], 1):
                    print(f"{idx}. {dead_name} — died fighting burgers.")
                print("-" * 30)
            elif admin_action == "5":
                break

    elif main_choice == "3":
        print("\n THE GUARD SLAMS THE DOOR WITH HIS FIST!")
        print("Guard: YOU ARE NOT LEAVING THAT EASILY! Entering a cafe and buying nothing?!")
        
        can_exit = run_interrogation("Suspicious Escapee")
        
        if can_exit:
            enroll_forced_employee()
            break
        else:
            print("\nGuard: Aha! Caught you! March back to the terminal and order something!")
            print("[Security blocked the exit. You are sent back to the main menu.]")
