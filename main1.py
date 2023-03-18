import openai
openai.api_key = "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"

engines = openai.Engine.list()
print(engines)
