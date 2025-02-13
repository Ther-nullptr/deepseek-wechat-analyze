import os
import json
import tools
import argparse
from tools import load_config
from collections import defaultdict


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", '-c', type=str, default="./data/config.yaml")
    parser.add_argument('--name', '-n', type=str, required=True, help='WeChat nickname of the contact, note that it is not the WeChat ID or remark name')
    parser.add_argument('--date', '-d', type=str, default=None, help='Set date to yyyy-mm-dd to filter messages on a specific date')
    args = parser.parse_args()
    args = load_config(args)
    return args


if __name__ == "__main__":
    args = parse_args()
    contacts, messages = tools.load_data(args)

    total_message, fullname = tools.filter_by_name(messages, args.name)

    # Assume total_message is a Pandas DataFrame
    messages_by_date = defaultdict(list)
    previous_sender = None

    # Iterate through each message
    for sender, content, timestamp in zip(total_message["Sender"], total_message["StrContent"], total_message["StrTime"]):
        date = timestamp.split(' ')[0]  # Extract the date part
        
        # If there are already messages for the current date and the sender is the same as the previous one, append to the last message
        if messages_by_date[date] and sender == previous_sender:
            messages_by_date[date][-1]["StrContent"] += "\n" + content
        else:
            # Otherwise, create a new message entry
            messages_by_date[date].append({"Sender": sender, "StrContent": content})
        
        previous_sender = sender  # Update the previous sender

    # Format all date-based data into the final JSON structure
    result = [{"Date": date, "Messages": messages} for date, messages in messages_by_date.items()]

    # Convert to JSON string format
    json_output = json.dumps(result, ensure_ascii=False, separators=(',', ':'))

    # Print JSON result
    print(json_output)

    # If you want to save it to a file
    if args.date:
        # Retrieve chat records for a specific date
        if args.date in messages_by_date:
            chat_records = messages_by_date[args.date]
            with open(f"messages_{args.name}_{args.date}.json", "w", encoding="utf-8") as f:
                f.write(json.dumps(chat_records, ensure_ascii=False, separators=(',', ':')))
        else:
            print(f"No chat records found for {args.date}")
    else:
        with open(f"messages_{args.name}.json", "w", encoding="utf-8") as f:
            f.write(json_output)

