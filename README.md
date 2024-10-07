# Alert Sorting Bot

## Description
This bot is designed for sorting incoming notifications and distributing them among users. The bot receives updates from channels it has been added to (text, video, photo). Only channels specified in the `Channels` table are processed. For each channel, it's necessary to provide a name (any) and its Telegram ID.

All received updates are checked for matches with records in the `Tickets` table, which associates users (by name and Telegram ID) with specific key text substrings. If matches are found, the bot forwards the relevant notification to users whose tickets contain substrings from the update text.

## Technologies Used
- **Django** – for administration and interaction with the database.
- **aiogram** – for creating the bot and handling notifications.
- **PostgreSQL** – as the database.

## Models
- **MatchingStrings** (accessible through the Django admin panel) – an entity for storing strings used for matching with notifications.
- **Tickets** (accessible through the Django admin panel) – an entity displaying the relationship between users and strings for searching.
- **Channels** (accessible through the Django admin panel) – an entity for storing information about Telegram channels from which the bot receives updates.

## Commands

- **Start Django server**:
  ```bash
  python manage.py runserver
  ```
  Used to start the admin panel.

- **Start the bot**:
  ```bash
  python manage.py startbot
  ```
  Command to start the bot. This command is sufficient to get started.

## Configuration
You can change the text parameters and other constants related to the bot's interface in the `App/Bot/constants.py` file.
Bot configuration variables (such as the interval between sending messages) can be changed in the `App/Bot/properties.py` file.


## Environment Variables

For the project to function correctly, the following environment variables must be configured:
- `TOKEN` – the token for the Telegram bot.
- `POSTGRES_PASS` – the password for the PostgreSQL database.
- `POSTGERS_DB_NAME`
- `POSTGERS_USER`
- `POSTGERS_PORT`
- `POSTGERS_HOST`

