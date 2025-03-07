# def reverse_comments_queue(comments):
#     stack = []
#     list = []
#     for comment in comments:
#         stack.append(comment)
    
#     while len(stack) != 0:
#         list.append(stack.pop())

#     return list


# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


def clean_post(post):
    if post == '':
        return post
    
    stack = []
    for p in post:
        if stack and stack[-1].lower() == p.lower() and stack[-1] != p:
            # remove p from post
            stack.pop()
        else:
            stack.append(p)
    return ''.join(stack)
            
    

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
print(clean_post("")) 