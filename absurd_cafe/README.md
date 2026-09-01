# ABSURD-CAFE
## Official User Guide (v1.3.0)

Welcome to the official manual for the **Absurd-Cafe**. This software is a hybrid console tool designed to manage daily cafe logistics, fulfill customer food orders, handle stock inventory, and deploy an automated, paranoid AI Security System to interview suspicious buyers.

---

## System Overview & Requirements

* **Language Platform:** Python 3.14.6
* **Database File:** Automatically creates and syncs with `cafe_data.json` inside the script's directory.
* **Core Dependencies:** Built using standard Python libraries (`json`, `os`, `random`). No external pip installations needed!

---

## How to Run the App

1. Ensure Python is installed on your computer.
2. Place the project file (e.g., `main.py`) inside an independent project folder.
3. Open your terminal/command line, navigate to your folder, and run: python main.py
4. The database JSON file will be generated automatically upon your very first launch.

---

## Core Application Features

The system splits into three main structural entry branches from the **Main Role Selection Screen**:

### 1. The Customer Menu (Ordering System)
Customers interact with an easy-to-navigate command interface to gather carbohydrates under close security surveillance:
* **Display Food Menu:** Shows all current food and beverage options, pricing in RUB, and exact real-time warehouse stock counts.
* **Add Tasty Item to Cart:** Registers chosen items into the session list based on their unique `Food ID`.
* **View Current Shopping Cart:** A specialized diagnostic tool that enumerates every single item chosen by the user and aggregates the exact total cost before checkout.
* **Checkout Order:** Prompts the user for a name protocols and initiates a mandatory security interrogation loop.

### 2. The Absurd Interrogation Engine (Fraud & Spy Monitor)
To protect internal burger resources, any checkout or escape triggers a high-security automated screening checkpoint:
* **Randomized Question Bank:** The engine holds **20 highly unpredictable, abstract, and comedic questions**.
* **Dynamic Selection:** The script samples exactly **2 completely random questions** for every single check, granting extreme replayability.
* **Officer Paranoia Level:** Every answer choice increments or decrements a hidden suspicion ledger. If the score triggers a threshold of **3 points**, the guard immediately consumes the order, cancels the checkout, and wipes the shopping cart.

### 3. The Chef Kitchen Login (Administrative Panel)
Employees can gain access to sensitive back-end controls by submitting the master password: `pizza`.
* **Add New Recipe:** Expands the digital menu by injecting custom parameters (ID, Name, Price, Quantity) directly into the operational database.
* **Restock Inventory:** Allows bulk adjustments of current ingredient counts when new cargo arrivals hit the kitchen docks.
* **View Logs & Staff:** Displays a statistical tally of failed checkout events alongside a ledger of regular personnel database files.
* **The Graveyard Memorial:** A digital monument tracking every single customer who bypassed security **3 times in a row** but unfortunately fell victim to literal **overeating/gluttony**.

---

## Critical Easter Eggs & Narrative Twists

* **Forced Recruitment Program ("You are not leaving!"):** If a user selects option `3` from the main menu (*Leave Hungry*), the guard slams the exit shut. Bypassing this specific exit interrogation activates a compulsory worker registration prompt. The app gathers name and phone logs, drafts the user into a ridiculous job profile (e.g., *Junior Burger Patty Flipper*), saves them into the JSON database, and bounces them back to work at the main menu.
* **The Gluttony Trigger:** Successfully consuming **3 entire checkout orders** back-to-back overloads the customer's structural parameters, archiving their profile directly onto the corporate cemetery records database.

---

## Version Control History (Git Emulation Log)
* **v1.0.0 (Base):** Linear console loop, operational menu display, shopping cart addition, and price calculators.
* **v1.1.0 (Stretch):** Implemented back-end staff privileges, master password validation gates, and dynamic catalog modification variables.
* **v1.2.0 (Blue Sky):** Created persistent external JSON storage frameworks and forced employee database onboarding sheets.
* **v1.3.0 (Hybrid Build):** Expanded the diagnostic core to host 20 randomly distributed detective interrogation arrays and structural gluttony monitors.
