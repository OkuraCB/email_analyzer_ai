# <span style="color: #4361ee">Email Meaningfulness Analyzer API

This API, made using `python` and it's `FlaskAPI` is called exclusively to register logs of usage and call the actual AI that does the text analysis.

## <span style="color: #f72585">How to setup the .env for the API

There are 2 variables that need to be included and 1 other that's optional.

```sh
OPENROUTER_API_KEY={YOUR_AI_API_KEY}
AI_MODEL={YOUR_AI_MODEL}

OPENNROUTER_API_URL=https://openrouter.ai/api/v1 #Optional
```

The `OPENROUTER_API_KEY` and `AI_MODEL` are your KEY and AI Model of choice, respectively. My key comes from Open Router and my model of choice is the DeepSeek R1, and so it is used to analyze all incoming text.

The listen port of the API default to 5000, but it can be changed based on your `WSGI` of choice. In my case that will be `gunicorn`.

## <span style="color: #f7b801">Prompt logic

Just standard practice when prompting AI for a solution. We will send 2 messages, onde for the system and another one for the user.

The system message will be specific about the purpose of the analysis, in this case, check emails for meaningfulness and return a valid JSON in response.

The user message, besides the actual email body, also will contain all the requirements of the json, as follows:

```json
{
    "score": Integer in the range(0,100),
    "meaningful_label": String classification of the meaningfulness,
    "topics": Integer count of topics discussed,
    "actions": Integer count of actions to take,
    "sentiment": String. Analysis of intent of the message,
    "length": String classification of the email length,
    "accuracy": Integer. Percentage of confidence that the model has,
    "suggestion": String. Short, appropriate response.
}
```

# <span style="color: #4cc9f0">How can I reach you to get support with this project?

If you need help with this project or to discuss the use of one technology over another, you can email me with:

- arthur-illa@hotmail.com
