# Telegram Creator Marketplace Bot

Telegram-based creator marketplace bot with user orders, performer profiles, internal wallet, referrals, rewards, and admin moderation.

This project is a marketplace-style Telegram bot where users can request personalized digital services from creators, while admins manage users, orders, balances, and platform activity. The focus of the project is on marketplace logic, role-based flows, monetization mechanics, and Telegram UX.

## Key Features

### User Side

* Telegram onboarding flow
* User profile and balance
* Browse available creators/services
* Create custom service requests
* Track order status
* Receive updates and notifications
* Referral rewards
* Internal wallet and reward balance

### Creator / Performer Side

* Creator profile flow
* Receive and manage assigned orders
* Accept or decline requests
* Update order progress
* Track completed tasks
* Receive internal rewards or balance updates

### Admin Side

* User management
* Creator management
* Order moderation
* Balance and wallet control
* Referral tracking
* Platform statistics
* Broadcast messages
* Manual review and support workflows

## Marketplace Logic

The bot includes core marketplace mechanics:

* Multi-role system: users, creators, admins
* Order lifecycle management
* Internal wallet and reward accounting
* Referral-based growth mechanics
* Admin moderation for safety and quality control
* Status-based notifications
* Task and request tracking

## Tech Stack

* Python
* Aiogram
* SQLite
* Telegram Bot API
* Async handlers
* Role-based command flows

## Architecture Overview

The project is organized around Telegram bot flows and marketplace logic:

* `bot.py` — main Telegram bot entry point
* `handlers/` — user, creator, admin, order, and wallet flows
* `keyboards/` — inline and reply keyboards
* `database/` — database access and storage logic
* `config.py` — configuration and environment variables
* `states/` — finite-state-machine flows for multi-step actions

## Why I Built It

I built this project to practice building a real marketplace product inside Telegram.

The main challenge was not just creating a bot, but designing a complete flow with different user roles, order states, referrals, internal monetization, moderation, and admin tools. It helped me understand how to structure Telegram products that go beyond simple commands and behave more like lightweight platforms.

## What I Learned

* Building multi-role Telegram bot systems
* Designing user, creator, and admin flows
* Managing order states and marketplace logic
* Implementing internal wallet mechanics
* Creating referral and reward systems
* Handling moderation and admin workflows
* Structuring larger Aiogram-based projects

## Example Use Cases

* Creator marketplace MVP
* Digital service order platform
* Telegram-based task marketplace
* Referral-driven community product
* Internal reward and monetization system
* Prototype for creator economy workflows

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/unchangedfeatures/telegram-creator-marketplace-bot.git
cd telegram-creator-marketplace-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
BOT_TOKEN=your_telegram_bot_token
ADMIN_ID=your_telegram_admin_id
```

### 5. Run the bot

```bash
python bot.py
```

## Security and Privacy Notes

* Do not commit bot tokens or private credentials
* Remove real user data before publishing
* Keep moderation tools enabled in production
* Use clear platform rules for users and creators
* Restrict admin commands to trusted Telegram IDs

## Project Status

This is a portfolio version of a Telegram marketplace bot. The public version is focused on demonstrating marketplace architecture, role-based bot flows, order management, referral mechanics, internal wallet logic, and admin moderation.

## Future Improvements

* Add PostgreSQL support
* Add web admin panel
* Add automated tests for order and wallet logic
* Add creator ratings and reviews
* Add payment provider integration
* Add analytics dashboard
* Improve moderation and reporting tools
