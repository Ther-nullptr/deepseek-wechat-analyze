# Deepseek Wechat Analyze

Deepseek Wechat Analyze is an open-source project that leverages the Deepseek API to analyze WeChat chat records. This tool provides insights into your chat data, including message analysis and role playing. 


## Installation

```bash
$ git clone https://github.com/Ther-nullptr/deepseek-wechat-analyze.git
$ pip install -r requirements.txt
```

## Usage

### 1. Extract your WeChat chat records.

* Refer to the [WeChatMsg](https://github.com/LC044/WeChatMsg) repository for the steps and recommend downloading the exe files directly from their Release.
* Export the contact information file `contacts.csv` and the chat log file `messages.csv` and place them in the `./data` directory.
* Note that this step can only be exported in Windows environment, Mac is not supported at the moment.

### 2. Select certain private chat records to analyze.

This command will extract all the private messages between you and your friend, and a json file `messages_{args.name}_{args.date}.json` will be generated:

```bash
python3 extract_private_message.py -c ./data/config.yaml -n <your friend's wechat name> 
```

This command will extract all the private messages between you and your friend on a specific date, and a json file `messages_{args.name}_{args.date}.json` will be generated:

```bash
python3 extract_private_message.py -c ./data/config.yaml -n <your friend's wechat name> -d <yyyy-mm-dd>
```

### 3(1). Analyze the chat records.

Organize different types of prompts in different files:

```txt
1_system_content.txt: System prompts.
2_setting_content.txt: The context in which the dialogue takes place, the personalities of the two parties to the dialogue, etc.
3_chat_content.txt: Chat records dumped in step 2.
4_target_content.txt: Your questions or the content you want to analyze.
```

The prompts will be contacted in the order of 1-2-3-4 layer.

We provide the available deepseek API providers in [api.md](./api.md). You can choose one of them to analyze the chat records.

For OpenAI-like API:

```bash
python3 analyze_openai_api.py \
    --api_key <your_api_key> \
    --base_url <your_base_url> \
    --model <your_model_name> \
    --system_content_file <your_system_content_file> \
    --setting_content_file <your_setting_content_file> \
    --chat_content_file <your_chat_content_file> \
    --target_content_file <your_target_content_file> \
    --temperature <temperature> \
    --top_p <top_p> \
    --presence_penalty <presence_penalty> \
    --seed <seed>
```

For SiliconFlow-like API:

```bash
python3 analyze_siliconflow_api.py \
    --api_key <your_api_key> \
    --base_url <your_base_url> \
    --model <your_model_name> \
    --system_content_file <your_system_content_file> \
    --setting_content_file <your_setting_content_file> \
    --chat_content_file <your_chat_content_file> \
    --target_content_file <your_target_content_file> \
    --temperature <temperature> \
    --top_p <top_p> \
    --presence_penalty <presence_penalty> \
    --seed <seed>
```

### 3(2). Role playing.

User can interact with the chat records by role playing just like in wechat. The command is as follows:

```bash
python3 dialogue_openai_api.py \
    --api_key <your_api_key> \
    --base_url <your_base_url> \
    --model <your_model_name> \
    --system_content_file <your_system_content_file> \
    --setting_content_file <your_setting_content_file> \
    --chat_content_file <your_chat_content_file> \
    --target_content_file <your_target_content_file> \
    --temperature <temperature> \
    --top_p <top_p> \
    --presence_penalty <presence_penalty> \
    --seed <seed> \
    --max_dialogue_length <max_dialogue_length> \
    --print_thinking False
```

## TODO

- [x] Analyze
- [x] Role playing
- [ ] Group chat analysis support
- [ ] RAG
- [ ] LoRA fine-tuning for WeChat chat records

## Acknowledgement

This project is inspired by the following repositories:

* [WeChatMsg](https://github.com/LC044/WeChatMsg)
* [WechatAnnualReport](https://github.com/chenyifanthu/WechatAnnualReport)