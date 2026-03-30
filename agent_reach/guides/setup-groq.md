# Groq Whisper Setup Guide

## Feature Overview
When YouTube/Bilibili videos have no subtitles, use Groq's Whisper API for speech-to-text. Groq provides a free tier.

## Steps the Agent Can Complete Automatically

1. Check if already configured:
```bash
agent-reach doctor | grep -i "groq\|whisper"
```

2. If the user provides a key, write the configuration:
```python
from agent_reach.config import Config
c = Config()
c.set("groq_api_key", "USER_PROVIDED_KEY")
```

3. Test (optional):
```bash
curl -s https://api.groq.com/openai/v1/models \
  -H "Authorization: Bearer USER_PROVIDED_KEY" \
  -o /dev/null -w "%{http_code}"
```
Returns 200 = working

## Steps Requiring Manual User Action

Tell the user:

> Video speech-to-text requires a Groq API Key (free).
>
> Steps:
> 1. Open https://console.groq.com
> 2. Sign up with a Google account or email
> 3. Click "API Keys" in the left sidebar
> 4. Click "Create API Key"
> 5. Copy the generated key and send it to me
>
> Groq provides a free tier that is more than sufficient for everyday use.

## Agent Actions After Receiving the Key

1. Write configuration: `config.set("groq_api_key", key)`
2. Test API availability
3. Report back: "✅ Speech-to-text enabled! Now I can extract content even from videos without subtitles."
