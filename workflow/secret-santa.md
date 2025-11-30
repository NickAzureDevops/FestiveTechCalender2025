# Christmas Secret Santa Multi-Agent Workflow

## Overview

Celebrate the holiday season with a collaborative, automated Secret Santa exchange using multiple agents in Microsoft Foundry! This workflow enables seamless wishlist collection, random Secret Santa assignment, notifications, and (optional) virtual gift sharing—all orchestrated by Foundry’s agent blocks.

## Agents & Roles

- **Wishlist & Preferences Agent**  
  Collects interests, favorite items, or holiday wishes from each participant.  
  Summarizes hints for assigned gifters.

- **Assignment Agent**  
  Randomly assigns each Secret Santa a recipient, ensuring fairness and no self-assignment.

- **Notification Agent**  
  Notifies each gifter of their recipient and shares the "gift idea" collected from their recipient's wishlist.

- *(Optional)* **Gift Exchange Agent**  
  Allows gifters to share virtual gifts, messages, or files with their recipients.

## Workflow Steps

1. **Collect Wishlists**  
   Each participant submits a wishlist via Foundry forms or chat.

2. **Random Assignment**  
   Participants are randomly paired so each Secret Santa has one recipient (no duplicates or self-assignment).

3. **Notify Gifters**
   Each gifter receives a private message or notification with their assigned recipient and hint.

4. *(Optional)* **Gift Exchange**
   Gifters deliver their virtual gifts, or schedule a reveal.

## Recommendations

- Use Foundry's UI to add agent blocks representing each workflow step.
- For randomization, embed a script (Python, JS, etc.) in the Assignment Agent, or leverage built-in Foundry functions.
- For notifications, use chat, email, or integrated notification features.
- Collect wishlists before running the assignment step to ensure maximum holiday magic!

## Example Agent Definitions

### Wishlist & Preferences Agent

> Prompts: "What are your favorite holiday treats, hobbies, or dream gifts?"

### Assignment Agent

> Script Example (Python):
> ```python
> import random
> participants = ["Alice", "Bob", "Charlie", "Diana"]
> recipients = participants.copy()
> random.shuffle(recipients)
> # Ensure assignments
> assignments = dict(zip(participants, recipients))
> ```

### Notification Agent

> Message Example:  
> "Hi Alice! You're the Secret Santa for Bob. Gift idea: 'Loves books and hot cocoa.'"

### Gift Exchange Agent (Optional)

> Prompts gifters to send a virtual gift, message, or file.

## Customization Tips

- Add or remove agent roles as required.
- Integrate holiday themes in messages and notifications.
- Use additional workflow steps for organizing a group gift reveal event or feedback.

## Sample Participant List

- Alice
- Bob
- Charlie
- Diana

---

Happy holidays and enjoy your Foundry-powered Secret Santa exchange!