# Please install OpenAI SDK first: `pip3 install openai`
import argparse
from openai import OpenAI

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    
    # base
    args.add_argument("--api_key", type=str, help="API key",default="sk-7b4PjDNelIdDBaLByb9KCUU1GrvLG9DNSiLQZ7qUhkTHpoDy")
    args.add_argument("--base_url", type=str, default="https://tbnx.plus7.plus/v1", help="API base URL")
    args.add_argument("--model", type=str, default="deepseek-reasoner", help="Model name")
    # content
    args.add_argument("--system_content_file", type=str, help="System content file", default="1_system_content.txt")
    args.add_argument("--setting_content_file", type=str, help="Setting content file", default="2_setting_content.txt")
    args.add_argument("--chat_content_file", type=str, help="Chat content file", default="3_chat_content.txt")
    args.add_argument("--target_content_file", type=str, help="Target content file", default="4_target_content.txt")
    # inference setting
    args.add_argument("--temperature", type=float, default=0.1, help="Temperature for sampling")
    args.add_argument("--top_p", type=float, default=0.5, help="Top-p for sampling")
    args.add_argument("--presence_penalty", type=float, default=0.0, help="Presence penalty for sampling")
    args.add_argument("--seed", type=int, default=42, help="Seed for sampling")
    
    args = args.parse_args()
    
    client = OpenAI(api_key=args.api_key, base_url=args.base_url)
    
    # load text content
    with open(args.system_content_file, "r", encoding="utf-8") as f:
        system_content = f.read()
    
    with open(args.setting_content_file, "r", encoding="utf-8") as f:
        setting_content = f.read()
        
    with open(args.chat_content_file, "r", encoding="utf-8") as f:
        chat_content = f.read()
        
    with open(args.target_content_file, "r", encoding="utf-8") as f:
        target_content = f.read()

    # api request
    response = client.chat.completions.create(
        model=args.model,
        messages=[
            {"role": "system", "content": f"{system_content}"},
            {"role": "user", "content": f"以下是对于聊天背景的设定：{setting_content} 聊天具体内容为：{chat_content} 请回答以下问题：{target_content}"},
        ],
        stream=False,
        temperature=args.temperature,
        top_p=args.top_p,
        presence_penalty=args.presence_penalty,
        seed=args.seed,
    )

    content = response.choices[0].message.content
    
    # divide the content into thinking part and response part
    # thinking part: in <think> and </think>
    # response part: after </think>
    
    thinking_start = content.find("<think>")
    thinking_end = content.find("</think>")
    response_start = content.find("</think>")
    
    # if not found <think>，then the content is naive mode, direct print the content
    if thinking_start == -1:
        print(content)
    else:
        # print the thinking part in grey
        print("\033[30m" + content[thinking_start + 7:thinking_end] + "\033[0m", end="")
        # print the response part in white
        print(content[response_start + 8:])