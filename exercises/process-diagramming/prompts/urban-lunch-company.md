# "Urban Lunch Company"

## Business Prompt

The Urban Lunch Company runs lunch service each weekday
 from multiple store-front locations in cities across the United States.

The company employs
 executives, regional managers, order preparers, and payment station attendants
 to operate lunch service at each location.
 Company executives organize each location into a single geographic region
 and delegate operational responsibilities
  of all regional locations
  to a regional manager.
 Most regions have multiple locations,
  but some regions at some times only have one location.
  The same employee may manage multiple regions at the same time.

A few times per year,
 the manager of each region
  is responsible for designing a seasonal menu to feature salads and healthy lunch options
  made from locally-sourced and organic ingredients.
  All regional locations serve the same lunch menu for a specified period of time, until the new seasonal menu replaces the old one.
  A region need not change seasons at the same time as another region,
   and need not change seasons at the same time each year.

Each menu contains a list of food options. The options are organized into visual display categories like "Salads", "Grains", "Soups", "Beverages", and "Custom".
 Each non-custom menu option is represented on the menu with a name, brief description, caloric content, gluten-free categorization, and vegan-friendly categorization.
 For custom orders, the menu specifies the list of available ingredients and indicates the maximum number of ingredients from each ingredient family that may be added without causing a price overage.

The menu does not include prices for individual items or ingredients, however the company does specify an internal base price for each menu item and ingredient. The company is not required to charge for the same menu item the same base price across regions or seasons. Sometimes the company adjusts regional item prices mid-season. Executives use a separate system to track ingredient procurement and usage information.

Before serving a menu for the first time,
 the company is required by its board of directors
  to publish the caloric and allergen content
    of each individual menu option and ingredient. The company is not required to publish menu pricing information.

During lunch service at any location,
 customers have the option to order in-person
 or online. Customers who order in person communicate their order to a food preparer.  Customers who order online first must fill out a profile,
   which includes their name and dietary preferences/restrictions.
   Each customer may associate one or more credit cards with their profile. Online orders, upon payment authorization, trigger a printer in the kitchen of the order pickup location to print the order details, which are then read by a food preparer.

The food preparer prepares the order according to the customer's instructions.

Each customer must pay for his/her order before picking it up from the payment attendant.

Customers may present payment in cash, credit card, gift card, loyalty rewards card, or mobile application QR code.
 A customer may pay for an order using only one method.
 If one payment method is denied, the customer has an opportunity to present an alternate method.

If the customer presents enough cash,
 the payment attendant authorizes the transaction.

If the customer presents a gift card,
   the payment attendant scans the card, and the system checks the balance.
   If the balance is sufficient, the system authorizes the transaction and updates the gift card balance, else the system denies the transaction.
   Regardless of the outcome, after making the payment transaction authorization decision, the system indicates the current gift card balance.

If the customer presents a credit card,
 the payment station attendant scans the card and waits from a transaction authorization decision from an external authority.

If the customer presents a mobile phone,
 the payment attendant scans the customer's QR code, and the system checks to see if the code matches an existing customer profile. The system authorizes the transaction if there is a match, else it rejects the transaction. A customer needs to create an online profile and associate at least one credit card before the system will recognize that customer's QR code.

If the customer presents a loyalty rewards card,
 the payment station only authorizes the transaction if the card has 13 loyalty stamps.
 The company has decided to stop issuing loyalty rewards cards in favor of online customer profiles, but the company still honors legacy rewards cards. Each time a customer pays for an order, the payment station attendant stamps the card once.

<hr>

## Business Process Descriptions

### Menu Update Process

After the regional manager creates a new menu and executives sign-off on the menu, the company prints thousands of paper copies to be distributed to customers in each location, as well as two sets of wall-sized menu boards (one primary and one back-up) to be hung in each location.

After printing, the company arranges for a rental van to transport the menu boards to each location, and pays employees overtime to receive and install the new menu.

Sometimes the office supply company misprints the menus, in which case, the employees alert an executive to coordinate re-printing.

### Lunch Service Process

#### Customer Intake Phase

Customers enter the store through two glass doors.

Customers wait in line to order a salad, unless there is no line.

#### Salad Ordering Phase

Customers pass a printed menu hanging on the wall as they move through the queue.
  The menu lists all available salad options, including a number of seasonal salads and signature salads, as well as the option to create a custom salad from a number of listed ingredients.

Upon reaching the front of the queue, a salad-maker/salad-preparer prompts the customer for a salad order.

Some customers order a single salad. Others place an order for multiple salads (i.e. ordering on behalf of co-workers).

Usually a single salad-maker will prepare all the salads for a single customer before attending to the next customer. Sometimes multiple salad-makers operate simultaneously.

Some customers order pre-prepared signature salads or non-salad items (e.g. soft serve yogurt, bottled water, hard-boiled eggs, and soft drinks). Customers who do not require salad preparation are not required to wait in the salad preparation line, and either wait in a different line, or skip to the payment phase.

#### Salad Preparation Phase

The salad-maker prepares a salad to fulfill the order.

Some customers continue to glance behind their shoulders at the menu during salad preparation.

Customers who order a signature salad sometimes choose to make substitutions and additions to their order during the preparation phase. For each substitution or addition, the salad-preparer notifies the customer of any price overages (e.g. "cauliflower costs $1.60 extra, is that OK?" and "you have two items remaining").

Customers who order custom salads participate in a similar process of
 providing verbal preparation instructions to the salad-maker
 and responding to information about price overages.

#### Payment Phase

When the salad-maker is done preparing the salad, the customer proceeds to the payment phase.

There are two payment stations,
 each represented by a computer with barcode-scanning and credit-card processing hardware,
 and each operated by a separate attendant.

The salad-preparer communicates the price and nature of each salad to the payment station attendant, who enters the data into the computer.

After an invoice is prepared by the computer, the payment attendant communicates the total price to the customer and prompts the customer to choose a payment method.

Some customers pay with cash, some with credit cards, and some with a mobile app that contains pre-registered credit card information.

The customer presents payment to the payment attendant, and upon authorization of successful payment, the attendant hands a printed invoice to the customer.

#### Customer Exit Phase

After paying for their salad(s), the customer(s) either
 sit down inside the store to eat,
 sit outside to eat,
 or leave the premises.
