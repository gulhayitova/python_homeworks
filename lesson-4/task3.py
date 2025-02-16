text = str(input())
freed = ['a','e','y','u','o','i']
m_text = str()
dash = 0
for i in range(1, 1+len(text)):
    if (i-dash >= 3) and (text[i-1] not in freed and i != len(text)):
        m_text += text[i-1] + '_'
        freed.append(text[i-1])
        dash = i
    else:
        m_text += text[i-1]
print(m_text)