import re

EMOJIS = {
    "[微笑]": {"cn": "[微笑]", "zb": "[Smile]"},
    "[撇嘴]": {"cn": "[撇嘴]", "zb": "[Grimace]"},
    "[色]": {"cn": "[色]", "zb": "[Drool]"},
    "[发呆]": {"cn": "[发呆]", "zb": "[Scowl]"},
    "[得意]": {"cn": "[得意]", "zb": "[CoolGuy]"},
    "[流泪]": {"cn": "[流泪]", "zb": "[Sob]"},
    "[害羞]": {"cn": "[害羞]", "zb": "[Shy]"},
    "[闭嘴]": {"cn": "[闭嘴]", "zb": "[Silent]"},
    "[睡]": {"cn": "[睡]", "zb": "[Sleep]"},
    "[大哭] ": {"cn": "[大哭] ", "zb": "[Cry] "},
    "[尴尬]": {"cn": "[尴尬]", "zb": "[Awkward]"},
    "[发怒]": {"cn": "[发怒]", "zb": "[Angry]"},
    "[调皮]": {"cn": "[调皮]", "zb": "[Tongue]"},
    "[呲牙]": {"cn": "[呲牙]", "zb": "[Grin]"},
    "[惊讶]": {"cn": "[惊讶]", "zb": "[Surprise]"},
    "[难过]": {"cn": "[难过]", "zb": "[Frown]"},
    "[酷]": {"cn": "[酷]", "zb": "[Ruthless]"},
    "[冷汗]": {"cn": "[冷汗]", "zb": "[Blush]"},
    "[抓狂]": {"cn": "[抓狂]", "zb": "[Scream]"},
    "[吐] ": {"cn": "[吐] ", "zb": "[Puke] "},
    "[偷笑]": {"cn": "[偷笑]", "zb": "[Chuckle]"},
    "[愉快]": {"cn": "[愉快]", "zb": "[Joyful]"},
    "[白眼]": {"cn": "[白眼]", "zb": "[Slight]"},
    "[傲慢]": {"cn": "[傲慢]", "zb": "[Smug]"},
    "[饥饿]": {"cn": "[饥饿]", "zb": "[Hungry]"},
    "[困]": {"cn": "[困]", "zb": "[Drowsy]"},
    "[惊恐]": {"cn": "[惊恐]", "zb": "[Panic]"},
    "[流汗]": {"cn": "[流汗]", "zb": "[Sweat]"},
    "[憨笑]": {"cn": "[憨笑]", "zb": "[Laugh]"},
    "[悠闲] ": {"cn": "[悠闲] ", "zb": "[Commando] "},
    "[奋斗]": {"cn": "[奋斗]", "zb": "[Determined]"},
    "[咒骂]": {"cn": "[咒骂]", "zb": "[Scold]"},
    "[疑问]": {"cn": "[疑问]", "zb": "[Shocked]"},
    "[嘘]": {"cn": "[嘘]", "zb": "[Shhh]"},
    "[晕]": {"cn": "[晕]", "zb": "[Dizzy]"},
    "[疯了]": {"cn": "[疯了]", "zb": "[Tormented]"},
    "[衰]": {"cn": "[衰]", "zb": "[Toasted]"},
    "[骷髅]": {"cn": "[骷髅]", "zb": "[Skull]"},
    "[敲打]": {"cn": "[敲打]", "zb": "[Hammer]"},
    "[再见] ": {"cn": "[再见] ", "zb": "[Wave] "},
    "[擦汗]": {"cn": "[擦汗]", "zb": "[Speechless]"},
    "[抠鼻]": {"cn": "[抠鼻]", "zb": "[NosePick]"},
    "[鼓掌]": {"cn": "[鼓掌]", "zb": "[Clap]"},
    "[糗大了]": {"cn": "[糗大了]", "zb": "[Shame]"},
    "[坏笑]": {"cn": "[坏笑]", "zb": "[Trick]"},
    "[左哼哼]": {"cn": "[左哼哼]", "zb": "[Bah！L]"},
    "[右哼哼]": {"cn": "[右哼哼]", "zb": "[Bah！R]"},
    "[哈欠]": {"cn": "[哈欠]", "zb": "[Yawn]"},
    "[鄙视]": {"cn": "[鄙视]", "zb": "[Pooh-pooh]"},
    "[委屈] ": {"cn": "[委屈] ", "zb": "[Shrunken] "},
    "[快哭了]": {"cn": "[快哭了]", "zb": "[TearingUp]"},
    "[阴险]": {"cn": "[阴险]", "zb": "[Sly]"},
    "[亲亲]": {"cn": "[亲亲]", "zb": "[Kiss]"},
    "[吓]": {"cn": "[吓]", "zb": "[Wrath]"},
    "[可怜]": {"cn": "[可怜]", "zb": "[Whimper]"},
    "[菜刀]": {"cn": "[菜刀]", "zb": "[Cleaver]"},
    "[西瓜]": {"cn": "[西瓜]", "zb": "[Watermelon]"},
    "[啤酒]": {"cn": "[啤酒]", "zb": "[Beer]"},
    "[篮球]": {"cn": "[篮球]", "zb": "[Basketball]"},
    "[乒乓] ": {"cn": "[乒乓] ", "zb": "[PingPong] "},
    "[咖啡]": {"cn": "[咖啡]", "zb": "[Coffee]"},
    "[饭]": {"cn": "[饭]", "zb": "[Rice]"},
    "[猪头]": {"cn": "[猪头]", "zb": "[Pig]"},
    "[玫瑰]": {"cn": "[玫瑰]", "zb": "[Rose]"},
    "[凋谢]": {"cn": "[凋谢]", "zb": "[Wilt]"},
    "[嘴唇]": {"cn": "[嘴唇]", "zb": "[Lips]"},
    "[爱心]": {"cn": "[爱心]", "zb": "[Heart]"},
    "[心碎]": {"cn": "[心碎]", "zb": "[BrokenHeart]"},
    "[蛋糕]": {"cn": "[蛋糕]", "zb": "[Cake]"},
    "[闪电] ": {"cn": "[闪电] ", "zb": "[Lightning] "},
    "[炸弹]": {"cn": "[炸弹]", "zb": "[Bomb]"},
    "[刀]": {"cn": "[刀]", "zb": "[Dagger]"},
    "[足球]": {"cn": "[足球]", "zb": "[Soccer]"},
    "[瓢虫]": {"cn": "[瓢虫]", "zb": "[Ladybug]"},
    "[便便]": {"cn": "[便便]", "zb": "[Poop]"},
    "[月亮]": {"cn": "[月亮]", "zb": "[Moon]"},
    "[太阳]": {"cn": "[太阳]", "zb": "[Sun]"},
    "[礼物]": {"cn": "[礼物]", "zb": "[Gift]"},
    "[拥抱]": {"cn": "[拥抱]", "zb": "[Hug]"},
    "[强] ": {"cn": "[强] ", "zb": "[ThumbsUp] "},
    "[弱]": {"cn": "[弱]", "zb": "[ThumbsDown]"},
    "[握手]": {"cn": "[握手]", "zb": "[Shake]"},
    "[胜利]": {"cn": "[胜利]", "zb": "[Peace]"},
    "[抱拳]": {"cn": "[抱拳]", "zb": "[Fight]"},
    "[勾引]": {"cn": "[勾引]", "zb": "[Beckon]"},
    "[拳头]": {"cn": "[拳头]", "zb": "[Fist]"},
    "[差劲]": {"cn": "[差劲]", "zb": "[Pinky]"},
    "[爱你]": {"cn": "[爱你]", "zb": "[RockOn]"},
    "[NO]": {"cn": "[NO]", "zb": "[Nuh-uh]"},
    "[OK]": {"cn": "[OK]", "zb": "[OK]"},
    "[嘿哈]": {"cn": "[嘿哈]", "zb": "[Hey]"},
    "[捂脸]": {"cn": "[捂脸]", "zb": "[Facepalm]"},
    "[奸笑]": {"cn": "[奸笑]", "zb": "[Smirk]"},
    "[机智]": {"cn": "[机智]", "zb": "[Smart]"},
    "[皱眉]": {"cn": "[皱眉]", "zb": "[Concerned]"},
    "[耶]": {"cn": "[耶]", "zb": "[Yeah!]"},
    "[吃瓜]": {"cn": "[吃瓜]", "zb": "[Onlooker]"},
    "[加油]": {"cn": "[加油]", "zb": "[GoForIt]"},
    "[汗]": {"cn": "[汗]", "zb": "[Sweats]"},
    "[天啊]": {"cn": "[天啊]", "zb": "[OMG]"},
    "[社会社会]": {"cn": "[社会社会]", "zb": "[Respect]"},
    "[旺柴]": {"cn": "[旺柴]", "zb": "[Doge]"},
    "[好的]": {"cn": "[好的]", "zb": "[NoProb]"},
    "[哇]": {"cn": "[哇]", "zb": "[Wow]"}
}

def unify_emoji(text):
    for label, item in EMOJIS.items():
        for v in item.values():
            text = text.replace(v, label)
    return text
