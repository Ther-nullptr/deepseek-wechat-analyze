import json
import requests
import argparse

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    
    # base
    args.add_argument("--api_key", type=str, help="API key",default="sk-kspglmdctluqdthuirgbtzkjfmakhzkmahnqwovzgigivejv")
    args.add_argument("--base_url", type=str, default="https://api.siliconflow.cn/v1/chat/completions", help="API base URL")
    args.add_argument("--model", type=str, default="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B", help="Model name")
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
    
    # load text content
    with open(args.system_content_file, "r", encoding="utf-8") as f:
        system_content = f.read()
    
    with open(args.setting_content_file, "r", encoding="utf-8") as f:
        setting_content = f.read()
        
    with open(args.chat_content_file, "r", encoding="utf-8") as f:
        chat_content = f.read()
        
    with open(args.target_content_file, "r", encoding="utf-8") as f:
        target_content = f.read()

    payload = {
        "model": f"{args.model}",
        "messages": [
            {
                "role": "system",
                "content": f"{system_content}"
            },
            {
                "role": "user",
                "content": f"以下是对于聊天背景的设定：{setting_content} 聊天具体内容为：{chat_content} 请回答以下问题：{target_content}"
            }
        ],
        "stream": False,
        "stop": ["null"],
        "temperature": args.temperature,
        "top_p": args.top_p,
        "frequency_penalty": args.presence_penalty,
        "n": 1,
        "response_format": {"type": "text"},
        "timeout": 1000
    }
    headers = {
        "Authorization": f"Bearer {args.api_key}",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", args.base_url, json=payload, headers=headers)
    # convert the response to json
    response_json = json.loads(response.content)
    reasoning_content = response_json['choices'][0]['message']['reasoning_content']
    answer_content = response_json['choices'][0]['message']['content']
    
    # print reasoning part as grey
    print("\033[30m" + reasoning_content + "\033[0m")
    print(answer_content)