# Report Bot

This project reads sales data from a CSV file, analyzes it, and sends a daily summary to Telegram. It is designed to be simple for local use and can also be triggered by Windows Task Scheduler for automatic delivery.

## Install

```bash
pip install -r requirements.txt
```

## Set Up `.env`

Create a `.env` file in the project root with:

```env
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```

## Run

Run the project manually with:

```bash
python main.py
```

If you want to use the old in-process Python scheduler, run:

```bash
python main.py --loop
```

## Windows Scheduled Run

To run automatically without keeping Python open all day, create a Windows Task Scheduler task that runs:

```bash
python e:\DEVELOPING\projects\report_bot\main.py
```

Recommended Task Scheduler settings:

- Trigger: Daily at your report time
- Action: Start a program
- Program/script: path to `python.exe`
- Add arguments: `e:\DEVELOPING\projects\report_bot\main.py`
- Start in: `e:\DEVELOPING\projects\report_bot`
- Enable: Run whether user is logged on or not
- Enable: Wake the computer to run this task

Important: if the laptop or PC is fully powered off, Windows Task Scheduler cannot run the task. For sending reports while the computer is off, the bot must be hosted on an always-on machine such as a VPS, cloud server, or another computer that stays running.

## Screenshot

Add a screenshot of the Telegram message here after you capture it.
