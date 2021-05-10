def emoji_conv(msg):
    words=msg.split("")
    emojis={
        ":)":"happy",
        ":(":"sad"
    }
    output=''
    for word in words:
        output += emojis.get(word,words)+ " "
        return output

msg=input(">")
print(emoji_conv(msg))
